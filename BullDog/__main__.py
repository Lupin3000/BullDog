#!/usr/bin/env python3

import argparse
import os.path
from sys import exit
from time import sleep

from BullDog.Report import WriteReport

debug = False
delay = 0


def main():
    """
    Main function to assign user arguments
    and to set default variables
    """
    global debug
    global delay
    filename = None

    # set argument description/epilog
    description = 'OTG USB HID'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    # set optional arguments
    parser.add_argument('-d', '--delay', help="default delay between all inputs, default is 0", default=0)
    parser.add_argument('-t', '--test', help='just debug input file ', default=False, action='store_true')

    # set mandatory arguments
    parser.add_argument('bark', help='your bark script')

    # read arguments by user
    args = parser.parse_args()

    # set default delay
    if args.delay and float(args.delay) > 0:
        delay = float(args.delay)

    #  set debug mode
    if args.test:
        debug = True

    # set filename
    if len(args.bark.strip()) == 0:
        print('You did not provide any bark script?')
        exit(1)
    else:
        filename = args.bark

    if not os.path.isfile(filename):
        print("{} not found".format(filename))
        exit(1)
    else:
        read_file(filename)


def read_file(barking_file):
    """
    Read file by line, provided by user as argument
    and call next method '__process_file_line'
    """
    with open(barking_file, 'r') as file_handler:

        for line in file_handler:
            line_string = line.rstrip("\n")

            if not line_string.strip():
                continue
            else:
                process_barking_file(line_string)


def process_barking_file(line_string):
    """
    Parse each line of the file
    and split into commands, delays or character

    :param line_string: line of file
    :type line_string: str
    """
    if not (line_string.startswith('#')):

        if line_string.__contains__('[CMD]'):
            line = line_string.replace('[CMD]', '').strip()

            report = WriteReport(delay=delay, debug=debug)
            report.report_command(line)

        elif line_string.__contains__('[DELAY]'):
            value = float(line_string.replace('[DELAY]', '').strip())
            sleep(value)

        else:
            report = WriteReport(delay=delay, debug=debug)
            report.report_string(line_string)


if __name__ == '__main__':
    main()
