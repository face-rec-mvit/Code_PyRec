#<This script is the frame work part, structures the images in one particular frame work .>
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


"""

 Usage : python frame_work.py "path to directory of images"
 Return values : This script returns 6 values in the following order 
 
 return order : train_data_set,entire_train_data_as_list,no_of_classes,no_of_images_per_class,test_data_set,flag_for_testing
	
	train_data_set = list of all training images as an 2-d array
	entire_train_data_as_list = list of all training images as a single list
	no_of_classes = total number of classes in the given input database
	test_data_set=list of training images as a 1-array ( In case user wants, can be typecasted to list in his script using this return value )
	count_of_dots_original_path : contains number of dots the original path has, this +1 gives number of dots to be replaced to get modified names
	flag_for_testing=This is the flag which says about the directory directory structure. 
	                 flag_for_testing = 1 , means the directory structure is flat, means modifications of path names is necessary to extract class names
  			 flag_for_testing = 0 , means the directory structure is hierarchical which means modifcations is not necessary for extracting class names

This is usually called from the "main" script of the algorithm i.e for eg. if PCA is the algorithm we are using we have to call this from PCA_main as follows 

	 train_data_set,entire_train_data_as_list,no_of_classes,no_of_images_per_class,test_data_set,flag_for_testing=frame_work.pre_process(images_path)
 	
Then using the above return values the training part and testing part is called in the PCA_main in our example taken
		
 Note  : The code works for irrespetive of any directory structure. But as far as possible try to avoid underscores and dots in the names of the directory.	

"""

#! /usr/bin/python

#############################################################importing all the required modules#############################################################

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

########################################################### all the required modules imported ##################################################################

########################################################## Function to return_split_file_names #################################################################

# This function takes list which contains all image paths as elements as input and it splits the file names on os path seperator and returns the new list 
# which contains split file names as the elements
# Input : list of image names
# Output : list of image names with split filenames, every element in the returned list is the list of split file name

def return_split_file_names(images_list):
	split_image_names_def=[]
	no_of_images_def=len(images_list)
	for i in range(no_of_images_def):
		temp_image=images_list[i].split(os.sep)
		split_image_names_def.append(temp_image)
	return split_image_names_def,no_of_images_def


######################################################### End of the function to return__split_file_names #######################################################

######################################################### Function to do all preprocessing work #################################################################

def pre_process(pathtoimages):
	
	################################################# Declarations of all lists which are to be initialised ####################################
	
	images_abs_names=[] # variable contains all the paths to file
	total_img_vect=[]   # variable to contain total images in vector form
	mean_img_vect=[]   # variable  for containing mean of all images
	sum_img_vect=[]   # variable  for containing sum of all images
	mean_for_subtraction=[] # variable contains clones of mean used for subtracting
	norm_list = [] # variable to hold all the norm values during testing phase
	split_image_names=[]  # variable to hold split image files to group into classes
	class_names=[] #Variable to hold  the class names
	each_class=[] # variable to hold names of each class
	entire_class=[] # variable to hold entire class
	test_data_set=[] #variable for storing test images
	train_data_set=[] #variable for storing train images
	entire_train_data_as_list=[] #variable for storing train images as list
	images_name_modified=[] # variable to hold modified images names

	######################################################## End of Declarations  #############################################################

	######### get_files method in the module get_abs_names is called to get the absolute path names of all the images in input directory #######

	src_img_dir=pathtoimages  # Taking the backup of the directory path
	images=lslR.get_files(src_img_dir) #returns all the absolute image names as a list   

	################# Uncomment following 2-lines to print all the absolut path names in the order given by get_abs_names
	
	#print "printing absolute path file names as given by get_abs_names"
	#print images


	images_abs_names=images # Taking backup of absolute path names of the images 
	images.sort() # Sorting the image files so that images of each class are grouped together

	################# Uncomment following 2-lines to print all the absolut path names in the order given by get_abs_names

	#print "printing absolute path file names after sorting"
	#print images
	
	#_________________________________________________________________________________________________________________________________________#	
	 # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   For initialising mean_image_vect and sum_image_vect, $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
	 # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     its required to know the dimension of each image,  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
	 # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     so one test image is read and then all the      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
         # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      required values are found out.           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
	#_________________________________________________________________________________________________________________________________________#

	shape_image=Image.open(images[0]) # Any imge can be open, here we are opening 1st image
	shape_image_array=numpy.asarray(shape_image) # Dimension of the image is to be known so converting to numpy array
	shape=shape_image_array.shape # Getting the dimensions of the image convertedd array 

	################################### Uncomment following two-lines to know the dimension of the image 

	#print "printing shape or the dimension of the image"
	#print shape 
	
	total_dimensions_per_image=shape[0]*shape[1] # Multiplying rows * columns of array to know total dimensions
	
	################################### Uncomment following two-lines to know the total_dimensions of the image 

	#print "printing total dimensions of the image"
	#print total_dimensions_per_image 
	

	#######################################initialising all the required values such as mean_img_vect, sum_img_vect

	for i in range(total_dimensions_per_image):
		mean_img_vect.append(0) # initialising with zeros 
		sum_img_vect.append(0)  # initialising with zeros 

	######## Calling the function which returns the split file names 
	###### The function return_split_file names take one argument and returns two arguments
	#### Input Arguments : images : contains the sorted list of absolute path names of all the images in the input directory
	## Return values : return 1: split_image_names : Has the list of split image names
	# Return Values : return 2: no_of_images : This contains the total number of input images

	split_image_names,no_of_images=return_split_file_names(images) 

	####################################### Uncomment following 2 lines to see the split file names 

	#print "printing split file names"
	#print split_image_names

	#######################This part is to find the length of the path of each image to extract class name 
	
	single_image_to_find_length=split_image_names[0]
	length_split_image_name=len(single_image_to_find_length)

	################################ Code to extract the class names of the database

	for i in range(no_of_images):
		temp_class_name=split_image_names[i][length_split_image_name-2]  #extracting class names
		class_names.append(temp_class_name)  # creating a list of class names 

	###################### Uncomment following 2 lines to know all the different classes with repetitions
	
	#print "printing all class names"
	#print class_names

	set_of_class_names=set(class_names)  #removing the repetitions using set so it contains only unique classes
	
	##################### Converting back to list coz set doesnt support indexing #######

	unique_class_names=list(set_of_class_names)
	unique_class_names.sort()

	###################### Uncomment following 2 lines to know all different classes without repetitions

	#print "printing unique set of class names"
	#print set_of_class_names

	no_of_classes=len(set_of_class_names)  #getting the count of no of classes

	# If the directory structure is different (flat), some change to be done to the path names of the files. 
	# Every database has more then one class, this is obvious, coz if there are more then one class 
	# only then face recogniton on that database makes some sense

	#Checking if the classes are partitioned properly.
	
	flag_for_testing=0 # flag required to be set to 1 if in case if the directory structure is flat
	count_of_dots_original_path=0
	if(no_of_classes<=1): # if number of classes is 1 it means that partition has not happend 
		flag_for_testing=1  # setting  the flag indicating flat architecture
		temp_str_for_checking_if_underscore_is_present=images[0] 
		temp_index_if_present=temp_str_for_checking_if_underscore_is_present.find('_') # to check if '_' is present find returns the position of the '_' in the string or else return -1 if not present

		if(temp_index_if_present>=0): # if present 
			flag_for_changing_file_name=1 # set this flag to 1 which means that seperator is '_'
		else: # if not present 
			flag_for_changing_file_name=0 # set this flag to 0 which means that seperator is '.' or any other symbol

		# Modifying the images names so that it that seperator remains os.sep through out
                count_of_dots_original_path=pathtoimages.count('.')
		for i in range(no_of_images):
			if(flag_for_changing_file_name==0):
				temp_image_name_modified=images[i].replace('.',os.sep,count_of_dots_original_path+1)
			else:
				temp_image_name_modified=images[i].replace('_',os.sep)
			images_name_modified.append(temp_image_name_modified)

		#Uncomment following 2-lines to see the modified file names
	
		#print "printing modified images names"
		#print images_name_modified


		########## To obtain the split image names
		######## Calling the function which returns the split file names 
		###### The function return_split_file names take one argument and returns two arguments
		#### Input Arguments : images : contains the sorted list of absolute path names of all the images in the input directory
		## Return values  : return 1: split_image_names : Has the list of split image names
		#  Return values  : return 2: no_of_images : This contains the total number of input images


		split_image_names,no_of_images=return_split_file_names(images_name_modified)

		########### Uncomment following 2 lines to know the split file names

		#print " printing list of split file names : "	
		#print split_image_names


		#This part is to find the length of the path of each image to extract class name
	
		single_image_to_find_length=split_image_names[0]
		length_split_image_name=len(single_image_to_find_length)

		#Code to extract the class names of the database

		class_names=[]  # making class_names to empty string which other wise contains some junk values

		for i in range(no_of_images):
			temp_class_name=split_image_names[i][length_split_image_name-2]  #extracting class names '-2' because class names lies in last second position of list
			class_names.append(temp_class_name)  # creating a list of class names 

		########## Uncomment following two lines to know all the different classes with repetitions
	
		#print "printing all class names"
		#print class_names

		set_of_class_names=set(class_names)  #removing the repetitions using set so it contains only unique classes

		# Uncomment to know all the different classes without repetitions

		#print "printing unique set of class names"
		#print set_of_class_names

		no_of_classes=len(set_of_class_names)  #getting the count of no of classes
		
		####Converting back to list so coz set doesnt support indexing

		unique_class_names=list(set_of_class_names)
		unique_class_names.sort()

	
	#################arranging the input directory of images into the order of class

	img_counter=0
        num_of_images_each_class=[]
	for  i in range(no_of_classes):
		each_class=[]
		num_of_images_each_class.append(class_names.count(unique_class_names[i]))
		for j in range(class_names.count(unique_class_names[i])):
			#print "img=%d" %(img_counter)
			#print images[img_counter]
			each_class.append(images[img_counter])
			img_counter=img_counter+1
		entire_class.append(each_class)  #contains all the images arranged according to the class
	
	entire_class_backup=entire_class

	#print "imagecounter=%d" %(img_counter)
	
	#print "number of images =%d" %(len(images))
	#print entire_class
	#print "printing number of images per class"
	#print num_of_images_each_class
	#print "total number of images = %d" %(sum(num_of_images_each_class))

	#code to  create trainset and testset 
	#one random image selected in one class will be added in testset and all other remaining (no_of_images_per_class) will be added to trainset

	for i in range(no_of_classes):
		image_no_for_test=random.random()*num_of_images_each_class[i]	
		image_no_for_test=int(image_no_for_test)
		test_data_set.append(entire_class[i][image_no_for_test])
		temp_train=entire_class[i]
		temp_train.remove(entire_class[i][image_no_for_test])
		train_data_set.append(temp_train)

	# Uncomment following lines in order to know the details of the train_data_set
	
	#print "Printing type of train dataset 	
	#print type(train_data_set)
	#print "printing training data set"
	#print train_data_set

	# Uncomment following lines in order to know the details of the test_data_set
	#print "Printing type of test dataset 	
	#print type(test_data_set)
	#print "printing test data set"
	#print test_data_set
	
			
	################### we need the entire training data set as a single list

	entire_train_data_as_list=[]
	for r in  range(no_of_classes):
		entire_train_data_as_list.extend(train_data_set[r])
	print "Total number of trained images = %d " %(len(entire_train_data_as_list))
	
	return (train_data_set,entire_train_data_as_list,no_of_classes,test_data_set,count_of_dots_original_path,flag_for_testing)

#Copy paste this piece of code to know how many images are present in each class, The corresponding count will be present in list named num_of_images_each_class
#	for  i in range(no_of_classes):
#		num_of_images_each_class.append(class_names.count(unique_class_names[i]))

## Or else in the run time user can use the property of len of list as 
#	class_count=0
#	for i in test_data_set:
#		print "The number of images in %d class is  %d " %(class_count,len(i)) 
#		class_count=class_count+1



if __name__=='__main__':
	arg=sys.argv
	pre_process(sys.argv[1])

