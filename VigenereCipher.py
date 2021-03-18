#!/usr/bin/env python3
# coding: utf-8


"""
    Blaise de Vigenère (1523–1596) mathematician, developed encryption scheme,
    VigenereCipher algorithm  is implemented based on his work, with a utility
    of relative strength index for encryption and decryption.

    VERSION : 1.0
    LICENSE : GNU GPLv3
    STYLE   : PEP 8
    AUTHOR  : AKULA.S.S.S.R.Krishna
    Date    : 05/11/2020

    PURPOSE : To encrypt and decrypt text based files
    INPUT   : python3 VingenerCipher -i sample_file.txt -e "sample password"
    OUTPUT  : sample_file.txt will be replaced with encrypted data.
"""


import os
import argparse


class VigenereCipher(object):
    def __init__(self, key):
        print('Vigenere Cipher Encription')
        self.key = key

    def encode(self, text):     # Based on password every character
        key = self.key              # will be encrypted with different bias
        ans = ''
        for index, i in enumerate(text):
            if(ord('!') <= ord(i) <= ord('~')):
                index %= len(key)
                if(ord(i) + ord(key[index]) - ord('!') > ord('~')):
                    ans += (chr(ord('!') + (ord(i) + ord(key[index])
                            - ord('!')) % ord('~') - 1))
                else:
                    ans += (chr(ord(i) + ord(key[index]) - ord('!')))
            else:
                ans += i
        return ans

    def decode(self, text):     # Based on password every character
        key = self.key              # will be decrypted with different bias
        ans = ''
        for index, i in enumerate(text):
            if(ord('!') <= ord(i) <= ord('~')):
                index %= len(key)
                if((ord('!') + ord(i) - ord(key[index])) < ord('!')):
                    ans += (chr(ord('~') + (ord(i) - ord(key[index])) + 1))
                else:
                    ans += (chr(ord('!') + ord(i) - ord(key[index])))
            else:
                ans += i
        return ans


def read_from_file(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data


def write_to_file(file_name, data):
    f = open(file_name, 'w')
    data = f.write(data)
    f.close()


def encode_from_file(file_name, obj):
    data = read_from_file(file_name)
    for _ in range(args.strength):
        data = obj.encode(data)
    write_to_file(file_name, data)      # Replaces file with encrypted data
    print('encode file -> ' + file_name)


def decode_from_file(file_name, obj):
    data = read_from_file(file_name)
    for _ in range(args.strength):
        data = obj.decode(data)
    write_to_file(file_name, data)      # Replaces file with decrypted data
    print('decode file -> ' + file_name)


def encription_form_path(PATH, obj):    # Recursive function (MT-safe)
    try:
        for path in os.listdir(PATH):
            encription_form_path(PATH + '/' + path, obj)
    except(OSError):
        if(args.encode):
            encode_from_file(PATH, obj)
        elif(args.decode):
            decode_from_file(PATH, obj)


"""
    input can be either -i file / -f folder,
    encode -e, decode -d for encryption and decryption respectively,
    strength -s indicates number of times to be encrypted / decrypted.

"""


parser = argparse.ArgumentParser('Description of your program')
parser.add_argument('-i', '--input_file',
                    help='input file name', required=False)
parser.add_argument('-e', '--encode',
                    help='encode password', required=False)
parser.add_argument('-d', '--decode',
                    help='decode password', required=False)
parser.add_argument('-f', '--folder',
                    help='folder name', required=False)
parser.add_argument('-s', '--strength',
                    help='encription strength', type=int,
                    default=1, required=False)
args = (parser.parse_args())

if(args.input_file):
    PATH = args.input_file
elif(args.folder):
    PATH = args.folder
else:
    exit('Need --input_file or --folder\nUse -h for help')

if(args.encode):
    pswd = args.encode
elif(args.decode):
    pswd = args.decode
else:
    exit('Need --encode or --decode\nUse -h for help')


obj = VigenereCipher(pswd)
encription_form_path(PATH, obj)
