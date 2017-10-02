#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:47:39 2017

@author: ubuntu
"""

import os
from shutil import copyfile

import init as config

import glob

def rename(dir=config.merged_dir,
           target='_manual1'):
    for fullpath in glob.glob(dir+'*'+target+'*'):
        os.rename(fullpath,fullpath.replace(target,''))
'''        
def chgname(selected=config.selected,
            tgt='_training',
            dst= ''):
    for fullpath in glob.glob(config.in_dir+'*.jpg'):
        newpath = fullpath.replace(config.in_dir_names[selected],
                                   config.merged_dir_names[selected])
        newpath = newpath.replace(tgt,dst)
        copyfile(fullpath,newpath)       
'''            
def main():
    #chgname()
    rename()
if __name__ == '__main__':
    main()
            