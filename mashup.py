#!/usr/bin/env python

from __future__ import unicode_literals
import json
import pprint
import sys
import argparse


def key_factory(field):
    def get_key(item):
        return item['properties'][field]
    return get_key

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sort', help="specify sort field.")
    parser.add_argument('amount', type=int, help="specify #.")
    parser.add_argument('direction', help="if reverse sort, specify reverse.")
    args = parser.parse_args()

    if args.direction == ' reverse':
        direction = 'by reverse'
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
    message = 'Sorting {} items by: {} field{}.'.format(args.amount,
                                                        sort_field,
                                                        direction)
    print(message)

    with open('my_map.json', 'r') as data_file:
        data = json.load(data_file)
    data_list = data['features']
    get_key = key_factory(sort_field)
    sorted_list = sorted(data_list, key=get_key, **kargs)
    pprint.pprint(sorted_list)

    data = {'features': data_list}
    with open('my_map.json', 'w') as data_file:
        data = json.dump(sorted_list)