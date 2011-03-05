#! /usr/bin/python

from src import lpp
import numpy as np
import time
import os
import sys

res = {0: 's1', 1: 's2', 2: 's3', 3: 's4', 4: 's5', 5: 's6', 6: 's7', 7: 's8', 8: 's9', 9: 's10', 10: 's11', 11: 's12', 12: 's13', 13: 's14', 14: 's15', 15: 's16', 16: 's17', 17: 's18', 18: 's19', 19: 's20', 20: 's21', 21: 's22', 22: 's23', 23: 's24', 24: 's25', 25: 's26', 26: 's27', 27: 's28', 28: 's29', 29: 's30', 30: 's31', 31: 's32', 32: 's33', 33: 's34', 34: 's35', 35: 's36', 36: 's37', 37: 's38', 38: 's39', 39: 's40'}
types = ["pgm"]
#following path contains only the 1st 9 face images of each person in the orl database
testRes = {'s1': 0, 's34': 33, 's35': 34, 's28': 27, 's31': 30, 's12': 11, 's22': 21, 's5': 4, 's10': 9, 's2': 1, 's37': 36, 's27': 26, 's9': 8, 's30': 29, 's36': 35, 's21': 20, 's14': 13, 's39': 38, 's8': 7, 's13': 12, 's18': 17, 's33': 32, 's6': 5, 's24': 23, 's29': 28, 's7': 6, 's20': 19, 's4': 3, 's11': 10, 's40': 39, 's19': 18, 's26': 25, 's32': 31, 's17': 16, 's23': 22, 's16': 15, 's3': 2, 's15': 14, 's25': 24, 's38': 37}

#for i in range(11)[3:]:
i = int(sys.argv[1])
string = str(i)+".pgm"
print "Processing :"+string
ImageDir=lpp.Image_Directory("/media/backup/kunal/Face-rec/FACE_DATABASES/orl_faces",classKeys=res,ftype=types,exclude=string)
ImageDir.test("/media/backup/kunal/Face-rec/FACE_DATABASES/orl_faces",classKeys=testRes,include=string)
del ImageDir
#time.sleep(20)
os.system("rm /tmp/memmap*")
