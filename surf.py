#encoding:utf-8
import os
import os.path  

rootdir = "E:\\python脚本\\mdTransfer\\Marketdata"
for parent, dirnames, filenames in os.walk(rootdir):  
    #case 1:  
    for dirname in dirnames:  
        print("parent is:" + parent)
        print("dirname is:" + dirname)
    #case 2  
    for filename in filenames:  
        print("parent is:" + parent)
        print("filename with full path :" + os.path.join(parent, filename))