#!/usr/bin/env python

from __future__ import unicode_literals
import json
import pprint

if __name__ == '__main__':
    with open('my_map.json', 'r') as data_file:
        data = json.load(data_file)
    data_list = []
    for x in data['features']:
        data_list.append(x)
    pprint.pprint(data_list)