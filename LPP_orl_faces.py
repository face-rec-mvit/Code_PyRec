#! /usr/bin/python

from src import lpp
import numpy as np

res = {0: 's1', 1: 's2', 2: 's3', 3: 's4', 4: 's5', 5: 's6', 6: 's7', 7: 's8', 8: 's9', 9: 's10', 10: 's11', 11: 's12', 12: 's13', 13: 's14', 14: 's15', 15: 's16', 16: 's17', 17: 's18', 18: 's19', 19: 's20', 20: 's21', 21: 's22', 22: 's23', 23: 's24', 24: 's25', 25: 's26', 26: 's27', 27: 's28', 28: 's29', 29: 's30', 30: 's31', 31: 's32', 32: 's33', 33: 's34', 34: 's35', 35: 's36', 36: 's37', 37: 's38', 38: 's39', 39: 's40'}
types = ["pgm"]
#following path contains only the 1st 9 face images of each person in the orl database
ImageDir=lpp.Image_Directory("/media/backup/kunal/TEMP/orl_faces",res,types)
testRes = {'s1/10.pgm': 0, 's34/10.pgm': 33, 's35/10.pgm': 34, 's28/10.pgm': 27, 's31/10.pgm': 30, 's12/10.pgm': 11, 's22/10.pgm': 21, 's5/10.pgm': 4, 's10/10.pgm': 9, 's2/10.pgm': 1, 's37/10.pgm': 36, 's27/10.pgm': 26, 's9/10.pgm': 8, 's30/10.pgm': 29, 's36/10.pgm': 35, 's21/10.pgm': 20, 's14/10.pgm': 13, 's39/10.pgm': 38, 's8/10.pgm': 7, 's13/10.pgm': 12, 's18/10.pgm': 17, 's33/10.pgm': 32, 's6/10.pgm': 5, 's24/10.pgm': 23, 's29/10.pgm': 28, 's7/10.pgm': 6, 's20/10.pgm': 19, 's4/10.pgm': 3, 's11/10.pgm': 10, 's40/10.pgm': 39, 's19/10.pgm': 18, 's26/10.pgm': 25, 's32/10.pgm': 31, 's17/10.pgm': 16, 's23/10.pgm': 22, 's16/10.pgm': 15, 's3/10.pgm': 2, 's15/10.pgm': 14, 's25/10.pgm': 24, 's38/10.pgm': 37}
ImageDir.test("/media/backup/kunal/TEMP/test_images",testRes)
