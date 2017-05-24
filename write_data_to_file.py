#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AUTHOR: wangchenhao@kedacom.com

import sys
import os

def get_data():
    data = []

    if not os.path.exists(sys.argv[1]):
        while True:
            line = raw_input('(EOF to quit)> ')
            if line == 'EOF':
                break
            data.append(line)

        return data
    else:
        print('%s is already exists') % sys.argv[1]
        sys.exit(1)


def write_data(fname, data):
    fobj = open(fname, 'w')
    fobj.writelines(['%s\n' % item for item in data])
    fobj.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = get_data()
        fname = sys.argv[1]
        write_data(fname, data)
    else:
        print('Usage: %s filename') % sys.argv[0]
