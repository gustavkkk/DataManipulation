# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:23:14 2017

@author: Frank

In:
    (In/Out)/*.*
Out:
    Out/*.*
    
"""

import os
import cv2

import init as config

from argparse import ArgumentParser

#from gooey import Gooey

def resize(height,
           width,
           useOut=False,
           overwrite=False):
    in_dir = config.in_dir
    out_dir = config.out_dir
    if useOut:
        in_dir = out_dir
    for filename in os.listdir(in_dir):
        image = cv2.imread(in_dir + filename)
        resized = cv2.resize(image, (width, height))
        if overwrite:
            cv2.imwrite(in_dir + filename,resized)
        else:
            cv2.imwrite(out_dir + filename,resized)

def resize2(height,
            width,
            in_dir = config.in_dir,
            out_dir= config.out_dir,
            subdir=""):
    if subdir != "":
        in_dir += subdir + '/'
        out_dir += subdir + '/'
    for filename in os.listdir(in_dir):
        image = cv2.imread(in_dir + filename)
        resized = cv2.resize(image, (width, height))
        cv2.imwrite(out_dir + filename,resized)
           
#@Gooey(language='english')
def main():
    parser  = ArgumentParser(add_help=False)#description='Resize') 
    parser.add_argument("-h", "--height", type=int, default=500, dest='height', help="image height")
    parser.add_argument("-w", "--width", type=int, default=500, dest='width', help="image width")
    parser.add_argument("-d", "--subdir", default='001', help="select which directory")
    args = parser.parse_args()
    #if vars(args).get('help'):
    #    exit(0)
    resize2(args.height,
            args.width,
            in_dir = config.merged_dir,
            out_dir= config.merged_dir)
    #args.height
        
if __name__ == '__main__':
    main()
