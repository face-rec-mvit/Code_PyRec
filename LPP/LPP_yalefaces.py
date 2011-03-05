#!/usr/bin/python

from src import lpp
import numpy as np

res = {0: 'subject01', 1: 'subject02', 2: 'subject03', 3: 'subject04', 4:
'subject05', 5: 'subject06', 6: 'subject07', 7: 'subject08', 8: 'subject09', 9:
'subject10', 10: 'subject11', 11: 'subject12', 12: 'subject13', 13: 'subject14',
14: 'subject15'}

ImageDir = \
lpp.Image_Directory("/media/backup/kunal/Face-rec/FACE_DATABASES/yalefaces",res)

