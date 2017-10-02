# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 01:42:45 2017

@author: Frank


Out:
    In/
    Out/
"""

import os

useCustom = True
db_dir = "/media/ubuntu/Investigation/DataSet/Image"
categories = {'UNet':'UNet'}
subcategories = {'Bug':'Bug',
                 'Retina Train':'DRIVE/training',
                 'Retina Test':'DRIVE/test'}

in_dir_names = {'Default':'Data',
               'Retina':'images'}
out_dir_names = {'Default':'Images',
                'Retina':'1st_manual'}
label_dir_names = {'Default':'Labels',
                  'Retina':'mask'}
merged_dir_names = {'Default':'Merged',
                   'Retina':'merged'}

if useCustom:
    selected = 'Retina'
    dataset_dir = db_dir + "/" + categories['UNet'] + "/" + subcategories['Retina Test'] + "/"
else:
    selected = 'Default'
    dataset_dir = os.path.dirname(os.path.abspath(__file__)) + "/"

in_dir = dataset_dir + in_dir_names[selected] + "/"
out_dir = dataset_dir + out_dir_names[selected] + "/"
label_dir = dataset_dir + label_dir_names[selected] + "/"
merged_dir = dataset_dir + merged_dir_names[selected] + "/"

def mkdir(root,makechild=False):
    if not os.path.exists(root):
        os.makedirs(root)
    if makechild:
        for subdir in os.listdir(in_dir):
            if not os.path.exists(root+subdir):
                os.makedirs(root+subdir)       
        

def initialize():
    mkdir(in_dir)
    mkdir(out_dir)
    mkdir(label_dir)
    mkdir(merged_dir)
    
initialize()