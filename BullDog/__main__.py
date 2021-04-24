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

    # set argument description/epilog
    description = 'Python USB OTG Keyboard (Linux)'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    # set optional arguments
    parser.add_argument('-d', '--delay', help="default delay between all inputs, default is 0 seconds", default=0)
    parser.add_argument('-t', '--test', help='just debug input file and report', default=False, action='store_true')
    parser.add_argument('-b', '--barking', help='your barking script location')
    parser.add_argument('--text', help='some string to write directly')
    parser.add_argument('--command', help='some commands to write directly')

    # read arguments by user
    args = parser.parse_args()

    # set default delay
    if args.delay and float(args.delay) > 0:
        delay = float(args.delay)

    #  set debug mode
    if args.test:
        debug = True

    # verify script
    if not args.barking and not args.text and not args.command:
        print('There is nothing for barking provided!')
        exit(1)

    if args.barking:
        read_script_file(args.barking)

    if args.text:
        report = WriteReport(delay=delay, debug=debug)
        report.report_string(args.text)

    if args.command:
        report = WriteReport(delay=delay, debug=debug)
        report.report_command(args.command)


def read_script_file(script_path):
    """
    Read script file by line, provided by user as argument

    :param script_path: script path
    :type script_path: str
    """
    # verify script path
    if not os.path.isfile(script_path):
        print("Could not found your script: {}".format(script_path))
        exit(1)

    # read script file
    with open(script_path, 'r') as file_handler:
        for line in file_handler:
            line_string = line.rstrip("\n")
            if not line_string.strip():
                continue
            else:
                process_barking_file(line_string)


def process_barking_file(line_string):
    """
    Parse each line of the barking script
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
