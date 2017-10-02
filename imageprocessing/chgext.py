# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 02:03:52 2017

@author: Frank

In:
    In/*.*
Out:
    In/*.JPEG
"""

import os

import init as config

from argparse import ArgumentParser

import cv2

from PIL import Image

#from gooey import Gooey

def gif2png(oldname,newname,ext='png'):
	im = Image.open(oldname)
	im.save(newname,'png', optimize=True, quality=70)

def tif2jpg(oldname,newname):
    im = Image.open(oldname)
    im.thumbnail(im.size)
    im.save(newname, "JPEG", quality=100)
    
def chgext(in_dir=config.in_dir,
           out_dir=config.out_dir,
           subdir="",
           in_ext=".jpg",
           out_ext='.png'):
    for filename in os.listdir(in_dir + subdir):
        fullpath = in_dir + subdir + filename
        newpath = out_dir + subdir + filename
        if in_dir == out_dir:
            base = os.path.splitext(fullpath)[0]
        else:
            base = os.path.splitext(newpath)[0]
        newpath = base + out_ext
        if in_ext == '.gif':
            gif2png(fullpath,newpath)
        elif in_ext == '.tif':
            tif2jpg(fullpath,newpath)
        else:
            #img=cv2.imread(fullpath)
            #cv2.imwrite(newpath,img)
            os.rename(fullpath, newpath)
        
#@Gooey(language='english')
def main():
    parser  = ArgumentParser(add_help=False)#description='Resize') 
    parser.add_argument("-s", "--subdir", default='001', help="select which directory")
    #args = parser.parse_args()
    chgext(in_dir=config.in_dir, out_dir=config.merged_dir, in_ext=".tif", out_ext='.jpg')#args.subdir+'/')
        
if __name__ == '__main__':
    main()
