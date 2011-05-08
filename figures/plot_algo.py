#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 11

PCA = (98,78.67,73.33,74.67,85.33,16.67,0.0,100,0.0,68.94,82.72)
HBS_L1 = (97.5,81.33,77.33,77.33,100,30,36.92,98.4,90.8,78.33,80.91)
HBS_L2 = (95.5,74.67,70.69,73.33,100,6.67,3.08,26,86,3.33,4.54)

ind = np.arange(N)    # the x locations for the groups

width = 0.3
width1 = 0.75       # the width of the bars: can also be len(x) sequence
width2 = 0.50
width3 = 0.25

p1 = plt.bar(ind,PCA, width1, color='r')
p2 = plt.bar(ind,HBS_L1, width2, color='g')
p3 = plt.bar(ind,HBS_L2, width3, color='b')

#p1 = plt.bar(ind,HBS_L1, width, color='g')
#p1 = plt.bar(ind,HBS_L2, width, color='g')



plt.ylabel('Efficiency')

#plt.title('Algorithm PCA with all Databases')
#plt.title('Algorithm HBS_L1 with all Databases')
#plt.title('Algorithm HBS_L2 with all Databases')

plt.title('Comparing PCA v/s HBSL1 v/s HBSL2')

plt.xticks(ind+width/2., ('ORL', 'YALE_GIF', 'YALE_PGM', 'YALE_RESIZED', 'UMIST','CAL_ORIG','CAL_CROP','GT_ORIG','GT_CROP','D_MALES','D_FEMALES') )
plt.yticks(np.arange(0,101,5))

plt.legend( (p1[0], p2[0],p3[0]), ('PCA', 'HBS_L1','HBS_L2') )


plt.show()

