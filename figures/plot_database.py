#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 3
ORL = (98.0,97.5,95.5)
YALE_GIF = (78.67, 81.332,74.67)
YALE_PGM = (73.33,77.33,70.69)
YALE_RESIZED = (74.67,77.33,73.33)
UMIST = (85.33,100,100)
CALTECH_ORIG = (16.67,30,6.67)
CALTECH_CROP = (0,36.92,3.08)
GEORGIA_ORIG = (100,98.4,26)
GEORGIA_CROP = (0,90.8,86)
DBASE_MALES = (68.94,78.33,3.33)
DBASE_FEMALES = (82.72,80.91,4.54)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, ORL, width, color='b')
#p1 = plt.bar(ind, YALE_GIF, width, color='b')
#p1 = plt.bar(ind, YALE_PGM, width, color='b')
#p1 = plt.bar(ind, YALE_RESIZED, width, color='b')
#p1 = plt.bar(ind, UMIST, width, color='b')
#p1 = plt.bar(ind, CALTECH_ORIG, width, color='b')
#p1 = plt.bar(ind, CALTECH_CROP, width, color='b')
#p1 = plt.bar(ind, GEORGIA_ORIG, width, color='b')
#p1 = plt.bar(ind, GEORGIA_CROP, width, color='b')
#p1 = plt.bar(ind, DBASE_MALES, width, color='b')
#p1 = plt.bar(ind, DBASE_FEMALES, width, color='b')


plt.ylabel('Efficiency')

plt.title('ORL_EFFICIENCY')
#plt.title('YALE_GIF_EFFICIENCY')
#plt.title('YALE_PGM_EFFICIENCY')
#plt.title('YALE_RESIZED_EFFICIENCY')
#plt.title('UMIST_EFFICIENCY')
#plt.title('CALTECH_ORIG_EFFICIENCY')
#plt.title('CALTECH_CROP_EFFICIENCY')
#plt.title('GEORGIA_ORIG_EFFICIENCY')
#plt.title('GEORGIA_CROP_EFFICIENCY')
#plt.title('DBASE_MALES_EFFICIENCY')
#plt.title('DBASE_FEMALES_EFFICIENCY')



plt.xticks(ind+width/2., ('PCA', 'HBS_L1', 'HBS_L2') )
plt.yticks(np.arange(0,101,5))

plt.show()

