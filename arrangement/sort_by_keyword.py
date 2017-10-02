# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 05:00:54 2017

@author: Frank
"""

import os
import glob

autopath = True
if autopath:
    root_dir = os.path.dirname(os.path.abspath(__file__)) + "\\"
else:
    root_dir = '/media/Investigation/'
    
src_root_dir = root_dir + 'A微信平台素材'
dst_root_dir = root_dir + 'Insurance'

classes=['LP','VIN','No']

classname={'LP':'License Plate',
           'VIN':'Vehicle Identification Number',
           'No':'Nothing'}

ch2en={'车架':'VIN',
       '铭牌':'VIN',
       '驾驶员人车':'LP',
       '人车合影':'LP',
       '员合影':'LP',
       '度照片':'LP',
       '度照':'LP',
       '左后':'LP',
       '右后':'LP',
       '左前':'LP',
       '右前':'LP',
       '后部':'LP',
       '正面':'LP',
       '前部':'LP',
       '近照':'LP',
       '受损':'No',
       '现场':'No',
       '受损照片':'No'}

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

def init():
    mkdir(dst_root_dir)
    for dirname in classes:
        mkdir(dst_root_dir + '\\' + dirname)
    
def sort(ext='.jpg'):
    
    lp_count = 0
    vin_count = 0
    no_count = 0
    
    for key in ch2en.keys():
        for fullpath in glob.iglob(src_root_dir + '\\**\\' + '*' + key + '*' + ext, recursive=True):
            #print(fullpath)
            newpath = dst_root_dir+'\\'+ch2en[key] + '\\'
            if ch2en[key]=='LP':
                lp_count += 1
                newpath += str(lp_count) + ext
            elif ch2en[key]=='VIN':
                vin_count += 1
                newpath += str(vin_count) + ext
            else:
                no_count += 1
                newpath += str(no_count) + ext
            os.rename(fullpath,newpath)
            
    for fullpath in glob.iglob(src_root_dir + '\\**\\*' + ext, recursive=True):
        no_count += 1
        newpath = dst_root_dir+'\\No\\' + str(no_count) + ext
        os.rename(fullpath,newpath)
        
if __name__ == '__main__':
    init()
    sort()
                
    