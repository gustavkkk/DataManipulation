#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:10:34 2017

@author: ubuntu
"""

import os
import cv2
from shutil import copyfile

import init as config

import glob

def clr2gray(src_dir=config.in_dir,
             target_ext='.jpg'):
    for fullpath in glob.glob(src_dir+'*'+target_ext):
        img=cv2.imread(fullpath,cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(fullpath,img)
      
def main():
    clr2gray(src_dir=config.merged_dir)
if __name__ == '__main__':
    main()