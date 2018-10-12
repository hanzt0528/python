#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def find_file(path):
    print("cur dir")
    for filename in os.listdir(path):
        print(filename)

if __name__ == '__main__':
    find_file("/Users/hanzhongtao")



