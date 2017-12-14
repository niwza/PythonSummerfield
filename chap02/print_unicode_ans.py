#!/usr/bin/env python3.6

import sys
import unicodedata


def print_unicode_table(words):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        to_be_printed = True
        for word in words:
            if word not in name.lower():
                to_be_printed = False
                break
        if to_be_printed:
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                code, name.title()))
        code += 1


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string1 [string2 [... [stringN]]]".format(sys.argv[0]))
        words = None
    else:
        words = [word.lower() for word in sys.argv[1:]]
if words is not None:
    print_unicode_table(words)


