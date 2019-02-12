# -*- coding: utf-8 -*-
import os
import random


def get_english_name():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    englishname = ''
    for i in range(0, 10):
        englishname += chars[random.randint(0, len(chars)-1)]
        pass
    return englishname
pass

if __name__ == '__main__':
    print get_english_name()
    pass
