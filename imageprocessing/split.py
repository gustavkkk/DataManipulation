# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 04:27:03 2017

@author: Frank

http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
"""


import os
import cv2
import random

import init as config

from argparse import ArgumentParser

#from gooey import Gooey

def split(in_dir = config.in_dir,
          out_dir = config.merged_dir,
          height,
          width,
          subdir=""):
    
    if subdir != "":
        in_dir += subdir + '/'
        out_dir += subdir + '/'
        
    for index,filename in enumerate(os.listdir(in_dir)):
        
        img = cv2.imread(in_dir + filename)
        rows, cols = img.shape[:2]
        if rows  < height or cols < width:
            continue
        
        x_step = cols / width
        y_step = rows / height
        x_step = int(x_step)
        y_step = int(y_step)
        margin_x = cols - x_step * width
        margin_y = rows - y_step * height
        
        for i in range(1,x_step+1):
            for j in range(1,y_step+1):
                x = (i - 1) * width + random.randint(0,margin_x)
                y = (j - 1) * height + random.randint(0,margin_y)
                #x = random.randint(0, x_step) * width + random.randint(0,margin_x)
                #y = random.randint(0,y_step) * height + random.randint(0,margin_y)
                roi =  img[y:y+height,x:x+width]       
                cv2.imwrite(out_dir + str(index+1) + "_" + str(i*j) + ".JPEG",roi)
           
#@Gooey(language='english')
def main():
    parser  = ArgumentParser(add_help=False)#description='Resize') 
    parser.add_argument("-h", "--height", type=int, default=512, dest='height', help="image height")
    parser.add_argument("-w", "--width", type=int, default=512, dest='width', help="image width")
    parser.add_argument("-d", "--subdir", default='001', help="select which directory")
    args = parser.parse_args()
    #if vars(args).get('help'):
    #    exit(0)
    split(args.height,args.width,args.subdir)
    #args.height
        
if __name__ == '__main__':
    main()