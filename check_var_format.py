#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AUTHOR: wangchenhao@kedacom.com

import sys
import string

first_chs = string.letters + '_'
all_chs = string.letters + string.digits + '_'

def check_var(var):
    if var[0] not in first_chs:
        return 'postion 1 is invalid .'

    for i in range(1, len(var)):
        if var[i] not in all_chs:
            return 'postion %s is invalid .' % (i + 1)

    return 'var "%s" is valid !' % var


if __name__ == '__main__':
    if len(sys.argv) == 2:
        var = sys.argv[1]
        print(check_var(var))
    else:
        print('Usage: %s varname') % sys.argv[0]