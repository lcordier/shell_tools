#!/usr/bin/env python

"""
"""
import csv
import datetime
import optparse
import os
from pprint import pprint
# import shlex
import sys

from colorama import Fore, Back, Style, init as colorama_init
import psycopg2

# import util


DSN = 'dbname=  user='

ROOT = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':

    colorama_init()

    parser = optparse.OptionParser()

    parser.add_option('-i',
                      '--input',
                      dest='input',
                      action='store',
                      type='string',
                      default='',
                      help='input CSV file')

    parser.add_option('-o',
                      '--output',
                      dest='output',
                      action='store',
                      type='string',
                      default='',
                      help='output CSV file')

    options, args = parser.parse_args()

    if not (options.input and options.output):
        parser.print_help()
        sys.exit()

    connection = psycopg2.connect(dsn=DSN)
    cursor = connection.cursor()

    input = open(options.input, 'r')
    reader = csv.reader(input)
    header = next(reader)

    output = open(options.output, 'w')
    writer = csv.writer(output, quoting=csv.QUOTE_ALL, lineterminator='\n')



    output.close()

    connection.commit()
    cursor.close()
    connection.close()
