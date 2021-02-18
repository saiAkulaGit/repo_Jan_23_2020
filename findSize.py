#!/usr/bin/env python
# coding: utf-8

# In[36]:


import os
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-i','--input_dir_path', help='input file name', required=True)
parser.add_argument('-e','--every_file', help='gives size of every file', required=False)
args =(parser.parse_args())

class findSize(object):
   
    def __init__(self,):
        self.size=0

    #To get size in human redable format 
    def get_size_hr(self,size_bytes):
        if(size_bytes<1000):
            return size_bytes,'Bytes'
        elif(size_bytes<(10**6)):
            return size_bytes/(10**3),'KB'
        elif(size_bytes<(10**9)):
            return size_bytes/(10**6),'MB'
        else:
            return size_bytes/(10**9),'GB'

    def get_dir_size(self, path):
        for name in sorted(os.listdir(path)):
            try:
                self.get_dir_size(path+'/'+name)
            except:
                file_size=int((os.stat(path+'/'+name).st_size))
                if(args.every_file):
                    print(name," - ",self.get_size_hr(file_size))
                self.size+=file_size
        return self.size

    def get_size(self,):
        print('Total size = ',self.get_size_hr(self.get_dir_size(args.input_dir_path)))

obj=findSize()
obj.get_size()

