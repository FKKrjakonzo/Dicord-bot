#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime


def converttostr(input_seq, reactions):
    final_str = ''
    for i in range(len(input_seq)):
        final_str += reactions[i] + input_seq[i] + '\n'
    return final_str


def get_options(options):
    if len(options) == 2:
        reactions = ['\xe2\x9c\x85', '\xe2\x9d\x8c']
    else:
        reactions = [
            '\N{REGIONAL INDICATOR SYMBOL LETTER A}',
            '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
            "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER E}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
            "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
            ]
    return reactions[:len(options)]


def screensaver():
    now = datetime.datetime.now()
    if now.hour == 18 and now.minute == 0:
        os.system('xscreensaver-command -activate')

    if now.hour == 6 and now.minute == 0:
        os.system('xscreensaver-command -deactivate')
