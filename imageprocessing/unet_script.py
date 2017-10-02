#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:27:21 2017

@author: ubuntu

You should config selected,dataset_dir in init.py, first
/////////////////
if useCustom:
    selected = 'Retina'
    dataset_dir = db_dir + "/" + categories['UNet'] + "/" + subcategories['Retina Train'] + "/"
else:
    selected = 'Default'
    dataset_dir = os.path.dirname(os.path.abspath(__file__)) + "/"
////////////////
"""

import init as config
import chgext as conv
import merge
import chgsize as cz
import chgname as cn
import chgclr as cc

width=500
height=500

needchgext=True
needchgname=False
needchgclr=False
#MERGE PART
#gif-png,tif-png...
#in,out->merged
#in->merged,tif->jpg
#out->merged,gif->png
if needchgext:
    conv.chgext(in_dir=config.in_dir, out_dir=config.merged_dir, in_ext=".tif", out_ext='.jpg')
    conv.chgext(in_dir=config.out_dir, out_dir=config.merged_dir, in_ext=".gif", out_ext='.png')
else:
    merge(selected=config.selected,
          ext1 = '.jpg',
          ext2= '.png')

#RESIZE
cz.resize2(height,
           width,
           in_dir = config.merged_dir,
           out_dir= config.merged_dir)

#Golor2Gray
if needchgclr:
    cc.clr2gray(src_dir=config.merged_dir,
                target_ext='.jpg')

#Threshold

#Change Name
if needchgname:
    cn.rename('_manual1')
    cn.rename('_test')
    cn.rename('_training')