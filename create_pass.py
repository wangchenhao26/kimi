#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AUTHOR: wangchenhao@kedacom.com

import random
import string

all_chs = string.letters + string.digits # + string.punctuation

def create_pass(num=6):
    passwd = ''
    for i in range(num):
        passwd += random.choice(all_chs)

    return passwd


if __name__ == '__main__':
    print(create_pass())
    print(create_pass(10))