#<Script that performs the histogram based face recognition.>
#    Copyright (C) <2011>  <Authors : Dharini,Guruprasad, Kiran Tej, Kunal Ghosh>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.




#! /usr/bin/python


#importing all the required modules

import random
import numpy
import sys
#import initial_processing as ip
import get_abs_names as lslR
import sys
import Image
import scipy.linalg
import numpy.matlib
from numpy.matlib import zeros
import os
#import train_data
#import test_data
import train_hbs
import frame_work
import test_hbs_L1
import frame_work_v2


#Calling the function pre_process of frame_work, this returns some values in the following order, using those return values the training part and testing part is called by passing the required no of arguments

#return order : train_data_set,entire_train_data_as_list,no_of_classes,no_of_images_per_class,test_data_set,flag_for_testing
#	
# ret1: train_data_set = list of all training images as an 2-d array
# ret2: entire_train_data_as_list = list of all training images as a single list
# ret3:	no_of_classes = total number of classes in the given input database
# ret4:	no_of_images_per_class= Number  of images per class
# ret5:	test_data_set=list of training images as a 1-array ( In case user wants, can be typecasted to list in his script using this return value )
# ret6: flag_for_testing=This is the flag which says about the directory directory structure. 
#	                 flag_for_testing = 1 , means the directory structure is flat, means modifications of path names is necessary to extract class names
# 			 flag_for_testing = 0 , means the directory structure is hierarchical which means modifcations is not necessary for extracting class names

def histmain(images_path):
	
	train_data_set,entire_train_data_as_list,no_of_classes,test_data_set,count_of_dots_original_path,flag_for_testing=frame_work_v2.pre_process(images_path)
	
	
	# Calling the train_images_as_hists of train_hbs which returns the histogram of the trained images 
	
	
	train_hist_list=train_hbs.train_images_as_hists(entire_train_data_as_list)


### Calling the testdb of test_hbs which does the comparison 
	
	
	eff=test_hbs_L1.testdb(test_data_set,entire_train_data_as_list,train_hist_list,count_of_dots_original_path,flag_for_testing)
	
	print "efficiency"
	print eff
	

if __name__=='__main__':
	histmain(sys.argv[1])
