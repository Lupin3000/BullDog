#!/usr/bin/env python3

from time import sleep
from re import sub


class WriteReport:
    SIMPLE_CHARS = {'a': 0x04, 'b': 0x05, 'c': 0x06, 'd': 0x07, 'e': 0x08, 'f': 0x09, 'g': 0x0A, 'h': 0x0B, 'i': 0x0C,
                    'j': 0x0D, 'k': 0x0E, 'l': 0x0F, 'm': 0x10, 'n': 0x11, 'o': 0x12, 'p': 0x13, 'q': 0x14, 'r': 0x15,
                    's': 0x16, 't': 0x17, 'u': 0x18, 'v': 0x19, 'w': 0x1A, 'x': 0x1B, 'y': 0x1C, 'z': 0x1D, '1': 0x1E,
                    '2': 0x1F, '3': 0x20, '4': 0x21, '5': 0x22, '6': 0x23, '7': 0x24, '8': 0x25, '9': 0x26, '0': 0x27,
                    ' ': 0x2C, '-': 0x2D, '=': 0x2E, '[': 0x2F, ']': 0x30, '\\': 0x31, '#': 0x32, ';': 0x33, '\'': 0x34,
                    '`': 0x35, ',': 0x36, '.': 0x37, '/': 0x38}

    SHIFT_CHARS = {'A': 0x04, 'B': 0x05, 'C': 0x06, 'D': 0x07, 'E': 0x08, 'F': 0x09, 'G': 0x0A, 'H': 0x0B, 'I': 0x0C,
                   'J': 0x0D, 'K': 0x0E, 'L': 0x0F, 'M': 0x10, 'N': 0x11, 'O': 0x12, 'P': 0x13, 'Q': 0x14, 'R': 0x15,
                   'S': 0x16, 'T': 0x17, 'U': 0x18, 'V': 0x19, 'W': 0x1A, 'X': 0x1B, 'Y': 0x1C, 'Z': 0x1D, '!': 0x1E,
                   '@': 0x1F, '#': 0x20, '$': 0x21, '%': 0x22, '^': 0x23, '&': 0x24, '*': 0x25, '(': 0x26, ')': 0x27,
                   '_': 0x2D, '+': 0x2E, '{': 0x2F, '}': 0x30, '|': 0x31, '~': 0x32, ':': 0x33, '"': 0x34, '<': 0x36,
                   '>': 0x37, '?': 0x38}

    COMMAND_KEYS = {'ENTER': 0x28, 'ESCAPE': 0x29, 'BACKSPACE': 0x2A, 'TAB': 0x2B, 'SPACE': 0x2C, 'CAPS_LOCK': 0x39,
                    'F1': 0x3A, 'F2': 0x3B, 'F3': 0x3C, 'F4': 0x3D, 'F5': 0x3E, 'F6': 0x3F, 'F7': 0x40, 'F8': 0x41,
                    'F9': 0x42, 'F10': 0x43, 'F11': 0x44, 'F12': 0x45, 'PRINT': 0x46, 'SCROLL_LOCK': 0x47,
                    'PAUSE': 0x48, 'INSERT': 0x49, 'HOME': 0x4A, 'PAGE_UP': 0x4B, 'DELETE': 0x4C, 'END': 0x4D,
                    'PAGE_DOWN': 0x4E, 'RIGHT_ARROW': 0x4F, 'LEFT_ARROW': 0x50, 'DOWN_ARROW': 0x51, 'UP_ARROW': 0x52,
                    'LEFT_CONTROL': 0xE0, 'LEFT_SHIFT': 0xE1, 'LEFT_ALT': 0xE2, 'LEFT_GUI': 0xE3, 'RIGHT_CONTROL': 0xE4,
                    'RIGHT_SHIFT': 0xE5, 'RIGHT_ALT': 0xE6, 'RIGHT_GUI': 0xE7}

    ##################################################################
    # not all are in use yet (just prepared for further development) #
    ##################################################################
    MODIFIER_KEY = {'LEFT_CONTROL': 0x01, 'LEFT_SHIFT': 0x02, 'LEFT_ALT': 0x04, 'LEFT_GUI': 0x08, 'RIGHT_CONTROL': 0x10,
                    'RIGHT_SHIFT': 0x20, 'RIGHT_ALT': 0x40, 'RIGHT_GUI ': 0x80}

    def __init__(self, delay=0, debug=False):
        """
        Class constructor to assign user arguments
        and to set default variables

        :param delay: default delay after each keystroke
        :type delay: float
        :param debug: enable debug output (no report to /dev/hidg0
        :type debug: bool
        """
        self.__DELAY = float(delay)
        self.__DEBUG = bool(debug)

    def report_command(self, commands):
        """
        Keystroke commands for keyboard

        :param commands: keystrokes commands
        :type commands: str
        """
        characters = str(commands.strip())
        self.__process_command(characters)

    def report_string(self, text):
        """
        Keystroke text for keyboard

        :param text: keystrokes text
        :type text: str
        """
        characters = str(text.strip())
        list_string = list(characters)
        for character in list_string:
            self.__process_character(character)

    def __process_command(self, line):
        """
        Check for non-modified or modified commands
        and convert commands to bytearray

        :param line: commands to convert
        :type line: str
        """
        # create empty report (8 bytes)
        report = bytearray(8)

        # replace modifier
        # currently all modifiers are replaced by left-*
        line = sub('(.*)CONTROL', 'LEFT_CONTROL', line)
        line = sub('(.*)CTRL', 'LEFT_CONTROL', line)
        line = sub('(.*)SHIFT', 'LEFT_SHIFT', line)
        line = sub('(.*)ALT', 'LEFT_ALT', line)
        line = sub('(.*)GUI', 'LEFT_GUI', line)
        line = sub('(.*)WIN', 'LEFT_GUI', line)

        # count words
        word_count = len(line.split())

        #########################################################
        # @ToDo: check for a maximum of simultaneous keystrokes #
        #########################################################

        # single command
        if word_count == 1 and line in self.COMMAND_KEYS:
            report[2] = self.COMMAND_KEYS[line]

            if self.__DEBUG:
                print("CMD: {:<25} DEC: {:<7} {}".format(line, self.COMMAND_KEYS[line], report))
            else:
                self.__write_report_to_dev(report)
                self.__release_all_keys()

        # double command (modifier)
        if word_count == 2:
            dec1 = dec2 = None
            word_list = ' '.join([line]).split()

            if word_list[0] in self.MODIFIER_KEY:
                dec1 = self.MODIFIER_KEY[word_list[0]]
                report[0] = dec1

            if word_list[1] in self.SIMPLE_CHARS:
                dec2 = self.SIMPLE_CHARS[word_list[1]]
                report[2] = dec2

            if word_list[1] in self.COMMAND_KEYS:
                dec2 = self.COMMAND_KEYS[word_list[1]]
                report[2] = dec2

            if self.__DEBUG:
                print("CMD: {:<12} {:<12} DEC: {:<3} {:<3} {}".format(word_list[0], word_list[1], dec1, dec2, report))
            else:
                self.__write_report_to_dev(report)
                self.__release_all_keys()

        ##########################################
        # @ToDo: triple and quadruple keystrokes #
        ##########################################
        if word_count >= 3:
            pass

        # default delay
        sleep(self.__DELAY)

    def __process_character(self, character):
        """
        Check for non-shifted or shifted character
        and convert character to bytearray

        :param character: character to convert
        :type character: str
        """
        # create empty report (8 bytes)
        report = bytearray(8)

        # default characters
        if character in self.SIMPLE_CHARS:
            report[2] = self.SIMPLE_CHARS[character]

            if self.__DEBUG:
                print("CHR: {:<25} DEC: {:<7} {}".format(character, self.SIMPLE_CHARS[character], report))
            else:
                self.__write_report_to_dev(report)
                self.__release_all_keys()

        # modified characters
        if character in self.SHIFT_CHARS:
            report[0] = self.MODIFIER_KEY['LEFT_SHIFT']
            report[2] = self.SHIFT_CHARS[character]

            if self.__DEBUG:
                print("CHR: {:<25} DEC: {:<7} {}".format(character, self.SHIFT_CHARS[character], report))
            else:
                self.__write_report_to_dev(report)
                self.__release_all_keys()

        # default delay
        sleep(self.__DELAY)

    @classmethod
    def __release_all_keys(cls):
        """
        Release all keys by empty bytearray (8 bytes)
        """
        empty_key = bytearray(8)
        WriteReport.__write_report_to_dev(empty_key)

    @staticmethod
    def __write_report_to_dev(report):
        """
        Write report to /dev/hidg0 device

        :param report: bytearray to type on keyboard
        :type report: bytearray
        """
        with open('/dev/hidg0', 'rb+') as file_handler:
            file_handler.write(report)
