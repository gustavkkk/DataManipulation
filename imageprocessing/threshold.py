#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:48:19 2017

@author: ubuntu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:23:14 2017

@author: Frank

In:
    (In/Out)/*.*
Out:
    Out/*.*

# Basic threhold example 
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY)

# Thresholding with maxValue set to 128
ret, dst = cv2.threshold(src, 0, 128, cv2.THRESH_BINARY)

# Thresholding with threshold value set 127 
ret, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY)

# Thresholding using THRESH_BINARY_INV 
ret, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY_INV)

# Thresholding using THRESH_TRUNC 
ret, dst = cv2.threshold(src,127,255, cv2.THRESH_TRUNC)

# Thresholding using THRESH_TOZERO 
ret, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO)

# Thresholding using THRESH_TOZERO_INV 
ret, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO_INV)

# Thresholding using THRESH_OTSU
ret,dst = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
"""

import os
import cv2

from argparse import ArgumentParser

import init as config

import glob
#from gooey import Gooey

def threshold(in_dir = config.in_dir,
              out_dir = config.out_dir,
               subdir=""):
   
    if subdir != "":
        in_dir += subdir + '/'
        out_dir += subdir + '/'
    for filename in os.listdir(in_dir):
        img = cv2.imread(in_dir + filename, cv2.IMREAD_GRAYSCALE)
        ret, dst = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
        cv2.imwrite(out_dir + filename,dst)

def threshold2(src_dir=config.merged_dir,
               target_ext='.png'):
    for fullpath in glob.glob(src_dir+'*'+target_ext):
        img = cv2.imread(fullpath, cv2.IMREAD_GRAYSCALE)
        ret, dst = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
        cv2.imwrite(fullpath,dst)          
#@Gooey(language='english')
def main():
    parser  = ArgumentParser(add_help=False)
    parser.add_argument("-d", "--subdir", default='001', help="select which directory")
    args = parser.parse_args()
    #threshold(args.subdir)#"001")
    threshold2()   
if __name__ == '__main__':
    main()
