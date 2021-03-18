#!/usr/bin/env python3
# coding: utf-8

"""
    To find the size of a directory in human  readable format,
    as a utility gives each file size.

    VERSION : 1.0
    LICENSE : GNU GPLv3
    STYLE   : PEP 8
    AUTHOR  : AKULA.S.S.S.R.Krishna
    DATE    : 15/01/2021
    
    PURPOSE : To find size of a directory, along with all the hidden file sizes
    INPUT   : python3 findSize.py -i ./sample_folder -e 1
    OUTPUT  : List of each file with their respective size
"""

import os
import argparse

parser = argparse.ArgumentParser('Description of your program')
parser.add_argument('-i', '--input_dir_path',
                    help='input file name', required=True)
parser.add_argument('-e', '--every_file',
                    help='gives size of every file', required=False)
args = parser.parse_args()


class findSize(object):
    def __init__(self,):
        self.size = 0

    def get_size_hr(self, size_bytes):   # To get size in human readable format
        if(size_bytes < 1000):
            return size_bytes, 'Bytes'
        elif(size_bytes < (10**6)):
            return size_bytes / (10**3), 'KB'
        elif(size_bytes < (10**9)):
            return size_bytes / (10**6), 'MB'
        else:
            return size_bytes / (10**9), 'GB'

    def get_dir_size(self, path):   # Recursive function (MT-safe)
        for name in sorted(os.listdir(path)):
            try:
                self.get_dir_size(path + '/' + name)
            except(OSError):
                file_size = int((os.stat(path + '/' + name).st_size))
                if(args.every_file):
                    print(name, " - ", self.get_size_hr(file_size))
                self.size += file_size
        return self.size

    def get_size(self, ):
        print('Total size = ', self.get_size_hr(
             self.get_dir_size(args.input_dir_path)))


obj = findSize()
obj.get_size()
