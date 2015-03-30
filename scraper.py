#!/usr/bin/env python
from __future__ import unicode_literals
import requests
import io
from bs4 import BeautifulSoup
import sys
import string
import re



INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'H'
}


def get_inspection_page(**kwargs):
    """get inspection page"""
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    resp = requests.get(url, params=params)
    resp.raise_for_status() # <- This is a no-op if there is no HTTP error
    # remember, in requests `content` is bytes and `text` is unicode
    return resp.content, resp.encoding


def write_html():
    """query for a business and write results to a file"""
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98109'
    }
    request = get_inspection_page(**kwargs)
    # request = get_inspection_page(Business_Name='Plum Bistro')
    request_text = request[0].decode('utf-8')
    outfile = io.open('inspection_page.html', 'w')
    outfile.write(request_text)
    outfile.close()
    return request


def load_inspection_page(text):
    """load page from a file and put into request form"""
    request_text = b''
    f = io.open(text)
    request_text = f.read().encode('utf-8')
    return request_text, b'utf-8'


def parse_source(html, encoding='utf-8'):
    """Parse response into DOM for scraping"""
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed


def extract_data_listings(html):
    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)


def has_two_tds(elem):
    is_tr = elem.name == 'tr'
    td_children = elem.find_all('td', recursive=False)
    has_two = len(td_children) == 2
    return is_tr and has_two

if __name__ == '__main__':
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98109'
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = load_inspection_page('inspection_page.html')
    else:
        html, encoding = get_inspection_page(**kwargs)
    doc = parse_source(html, encoding)
    # print doc.prettify(encoding=encoding)
    # listings = extract_data_listings(doc) # add this line
    # print len(listings)                   # and this one
    # print listings[0].prettify()          # and this one too

    listings = extract_data_listings(doc)
    for listing in listings:  # <- add this stuff here.
        metadata_rows = listing.find('tbody').find_all(
            has_two_tds, recursive=False
        )
        print len(metadata_rows)
