#!/usr/bin/env python

from __future__ import unicode_literals
import json
import pprint
import sys
import argparse


def key_factory(field):
    """Returns a get_key for a field"""
    def get_key(item):
        return item['properties'][field]
    return get_key

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sort', help="specify sort field. Legal fields: address, averagescore, businessname, highscore, totalinspections")
    parser.add_argument('amount', nargs='?', type=int, help="specify number of items.")
    parser.add_argument('direction', nargs='?', help="to reverse sort, specify reverse (must have an amount for reverse to work).")
    args = parser.parse_args()

    if args.direction == 'reverse':
        direction = ' by reverse'
        kargs = {'reverse': True}
    else:
        direction = ''
        kargs = {}

    legal_args = ['address',
                  'averagescore',
                  'businessname',
                  'highscore',
                  'totalinspections']

    legal_fields = ['Address',
                    'Average Score',
                    'Business Name',
                    'High Score',
                    'Total Inspections']

    if args.sort not in legal_args:
        print 'Not a sortable field. Could not sort.'
        sys.exit()
    else:
        sort_field = legal_fields[legal_args.index(args.sort)]
    if args.amount is not None:
        amount = args.amount
    else:
        amount = 'all'

    with open('my_map.json', 'r') as data_file:
        data = json.load(data_file)
    data_list = data['features']
    get_key = key_factory(sort_field)
    sorted_list = sorted(data_list, key=get_key, **kargs)

    # use only specified number of items
    if args.amount is not None:
        sorted_list = sorted_list[-args.amount:]

    # creat geojson object
    sorted_result = {'type': 'FeatureCollection', 'features': []}
    for item in sorted_list:
        sorted_result['features'].append(item)
    pprint.pprint(sorted_result)

    file_name = 'end_map.json'
    with open(file_name, 'w') as data_file:
        data = json.dump(sorted_result, data_file)

    message = '\nSorted {} items by {} field{}.'.format(amount,
                                                        sort_field,
                                                        direction)
    print(message)
    print("\nWrote json object file to: {}".format(file_name))
