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

    if args.direction == 'reverse':
        direction = 'by reverse'
    else:
        direction = ''


    message = 'Sort {} items by: {} field {}.'.format(args.amount,
                                                      args.sort,
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