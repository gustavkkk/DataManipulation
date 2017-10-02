# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 01:39:24 2017

@author: Frank

In:
    In/001/*.*
    In/002/*.*
Out:
    Out/*.JPEG
"""

import os
from shutil import copyfile

import init as config

import glob

def merge(src_dir1=config.in_dir,
          src_dir2=config.out_dir,
          dst_dir=config.merged_dir,
          selected=config.selected,
          ext1 = '.jpg',
          ext2= '.png'):
    if ext1 == ext2 and src_dir1 == src_dir2:
        index = 0
        for subdir_name in os.listdir(config.in_dir):
            subpath = config.in_dir + subdir_name + '/'
            for filename in os.listdir(subpath):
                index += 1
                src = subpath + filename
                dst = dst_dir + str(index) + ext1
                copyfile(src, dst)
    else:
        for fullpath in glob.glob(src_dir1+'*'+ext1):
            newpath = fullpath.replace(config.in_dir_names[selected],
                                       config.merged_dir_names[selected])
            copyfile(fullpath,newpath)
        for fullpath in glob.glob(src_dir2+'*'+ext2):
            newpath = fullpath.replace(config.out_dir_names[selected],
                                       config.merged_dir_names[selected])
            copyfile(fullpath,newpath)
        
def main():
    merge()
if __name__ == '__main__':
    main()
            