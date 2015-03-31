#!/usr/bin/env python

from __future__ import unicode_literals
import json
import pprint
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sort', help="specify sort field.")
    parser.add_argument('amount', type=int, help="specify #.")
    parser.add_argument('direction', help="if reverse sort, specify reverse.")
    args = parser.parse_args()

    if args.direction == ' reverse':
        direction = 'by reverse'
    else:
        direction = ''

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

    # try:
    #     arg = sys.argv[1]
    # except IndexError():
    #     print('Exiting, no argument specified.')
    #     sys.exit()
    # with open('my_map.json', 'r') as data_file:
    #     data = json.load(data_file)
    # data_list = []
    # for x in data['features']:
    #     data_list.append(x)
    # pprint.pprint(data_list)