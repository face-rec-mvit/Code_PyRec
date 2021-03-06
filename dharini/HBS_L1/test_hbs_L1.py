#<This script does testing of HBS - Histogram Based Similarity of face recognition .>
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

import numpy
import Image
import sys
import os

### get_histogram : Function that takes image as a input and returns histogram of the image
# Input : image
#Output/return : histogram of the image


def get_histgram(image):
	image_array=numpy.asarray(image)
	image_array_flat=image_array.flatten()
	image_histogram=numpy.histogram(image_array_flat,10,(0,255))
	return image_histogram[0]

## return_recognized : method takes two arguments test_image_hist,trained_image_hists, it compare's test_image_hist with each of trained_image_hists and then returns the #nearest image to test_image_hist in the list trained_image_hists. 
# Input :  
#     arg_1 : test_image_hist - histogram of the image being tested
#     arg_2 : trained_image_hists - histogram of the set of trained images
		
def return_recognized(test_image_hist,trained_image_hists):
	temp_diff=[]
	for i in range(len(trained_image_hists)):
		itest_image_hist=numpy.array(test_image_hist)
		taken=numpy.array(trained_image_hists[i]) 		

		## Uncomment following to print the furthur details while processing 

		#print "test_image"
		#print test_image_hist
		#print "printing comparing image "
		#print taken

		t=test_image_hist-taken

		## Uncomment following to print the furthur details while processing 

		#print "printing difference"
		#print t


		temp_diff_temp=sum(abs(t))

		## Uncomment following to print the furthur details while processing 

		#print "prining sum"
		#print temp_diff_temp
	
		temp_diff.append(temp_diff_temp)

	## Uncomment following to print the furthur details while processing 

	#print "printing temp diff"
	#print temp_diff
	#print "printing length of difference list"
	#print len(temp_diff)
        #print "Minimum difference image index"
        #print temp_diff.index(min(temp_diff))
	
	return temp_diff.index(min(temp_diff))


### testdb takes some arguments and returns the efficiency of the database
# arg_1 : test_data_set - this list contains test data set ,( one image per class )
# arg_2 : entire_train_data_as_list - entire train dataset 
# arg_3 : train_hist_list - histogram of the trained data
# arg_4 : count_of_dots_original_path - number of dots in the original given path
# arg_5 : flag_for_testing - This is the flag which says about the directory directory structure. 
#	                 flag_for_testing = 1 , means the directory structure is flat, means modifications of path names is necessary to extract class names
# 			 flag_for_testing = 0 , means the directory structure is hierarchical which means modifcations is not necessary for extracting class names


def testdb(test_data_set,train_data_set,train_hist_list,count_of_dots_original_path,flag_for_rename):

	sucess=0
	for i in test_data_set:
		temp_norm_list=[]
		print "testing undergoing for the image: " +i
		temp_test_image=Image.open(i)
		temp_test_histogram=get_histgram(temp_test_image)
		recognized_index=return_recognized(temp_test_histogram,train_hist_list)
		recognized=train_data_set[recognized_index]
	
				
########## code of checking if the algorithm identified correctly or not
		if(flag_for_rename==1):
			index_of_underscore=i.find('_')
			if(index_of_underscore>=0):
				new_i=i.replace('_',os.sep)
				new_recognized=recognized.replace('_',os.sep)
			else:
				new_i=i.replace('.',os.sep,count_of_dots_original_path+1)
				new_recognized=recognized.replace('.',os.sep,count_of_dots_original_path+1)
		else: 
			new_i=i
			new_recognized=recognized
			
		temp_split_taken_name=new_i.split(os.sep)
		temp_split_recognized_name=new_recognized.split(os.sep)
		len_of_split_file_name=len(temp_split_recognized_name)

		
		if(temp_split_taken_name[len_of_split_file_name-2]==temp_split_recognized_name[len_of_split_file_name-2]):
	
			print "taken class : " + temp_split_taken_name[len_of_split_file_name-2]
			print "recognized class : " +temp_split_recognized_name[len_of_split_file_name-2] 
			print "success"
			sucess=sucess+1
		else :
			print "taken class : " + temp_split_taken_name[len_of_split_file_name-2]
			print "recognized class : " +temp_split_recognized_name[len_of_split_file_name-2] 
			print "failure"
			

	print "printing success"
	print " identified %d images out of %d images "  %(sucess,len(test_data_set))
	return (float(sucess)/len(test_data_set))*100

		

	

#if __name__=='__main__':
#	arg=sys.argv
#	train(sys.argv[1])
	
