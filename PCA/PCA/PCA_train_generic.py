#<This script does training of PCA-Principle Component Analysis .>
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

 Usage : python trainpca.py "path to directory of images"
 Note  : The code works for irrespetive of any directory structure. But as far as possible try to avoid underscores and dots in the names of the directory.	

"""

#! /usr/bin/python

#############################################################importing all the required modules#############################################################

import random
import numpy
import sys
import initial_processing as ip
import get_abs_names as lslR
import sys
import Image
import scipy.linalg
import numpy.matlib
from numpy.matlib import zeros
import os
import train_database
import test_database
import test1_database

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

	###################### Uncomment following 2 lines to know all different classes without repetitions

	#print "printing unique set of class names"
	#print set_of_class_names

	no_of_classes=len(set_of_class_names)  #getting the count of no of classes

	# If the directory structure is different (flat), some change to be done to the path names of the files. 
	# Every database has more then one class, this is obvious, coz if there are more then one class 
	# only then face recogniton on that database makes some sense

	#Checking if the classes are partitioned properly.
	
	flag_for_testing=0 # flag required to be set to 1 if in case if the directory structure is flat
	
	if(no_of_classes<=1): # if number of classes is 1 it means that partition has not happend 
		flag_for_testing=1  # setting  the flag indicating flat architecture
		temp_str_for_checking_if_underscore_is_present=images[0] 
		temp_index_if_present=temp_str_for_checking_if_underscore_is_present.find('_') # to check if '_' is present find returns the position of the '_' in the string or else return -1 if not present

		if(temp_index_if_present>=0): # if present 
			flag_for_changing_file_name=1 # set this flag to 1 which means that seperator is '_'
		else: # if not present 
			flag_for_changing_file_name=0 # set this flag to 0 which means that seperator is '.' or any other symbol

		# Modifying the images names so that it that seperator remains os.sep through out

		for i in range(no_of_images):
			if(flag_for_changing_file_name==0):
				temp_image_name_modified=images[i].replace('.',os.sep,1)
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

	
	no_of_images_per_class=no_of_images/no_of_classes  #getting the count of no of images per class

	# Uncomment to print the know the number of images per class

	#print "number of images per class = %d " %(no_of_images_per_class)
	
	#################arranging the input directory of images into the order of class

	for  i in range(no_of_classes):
		each_class=[]
		for j in range(no_of_images_per_class):
			img_counter=i*no_of_images_per_class+j
			each_class.append(images[img_counter])
		entire_class.append(each_class)  #contains all the images arranged according to the class
	
	entire_class_backup=entire_class

	#code to  create trainset and testset 
	#one random image selected in one class will be added in testset and all other remaining (no_of_images_per_class) will be added to trainset

	for i in range(no_of_classes):
		image_no_for_test=random.random()*no_of_images_per_class	
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
	
			
	test_data_set_matrix=numpy.matrix(test_data_set) # converting to matrix to perform multiplication 
	train_data_set_matrix=numpy.matrix(train_data_set) # converting to matrix to perform multiplication 
	
	#############Uncomment following lines to know the shapes and details of train_data_set and test_data_set

	#print "Printing test data shape 	
	#print test_data_set_matrix.shape
	#print "Printing train data shape 
	#print train_data_set_matrix.shape
	
	################### we need the entire training data set as a single list

	for r in  range(no_of_classes):
		c=0
		for c in range(no_of_images_per_class-1):
			entire_train_data_as_list.append(train_data_set[r][c])

	######### Calling traindb in train_database which actually does the training part and it returns some values which actually is needed during the testing phase.
	####### Input Argument : train_data_set ( set of tranining images )
	##### It returns 3 values
	#### (1) mean_img : contains the mean of all the images, its a 1-d array/list
	### (2) eigen_selected : Usually only the major values of the eigen vector are taken, this contain those major eigen values only
	## (3) signature_images_for_train_set : contains the signatures (mapped images / eigen images ) for the entire training dataset
	
	mean_img,eigen_selected,signature_images_for_train_set=train_database.traindb(train_data_set)

	#### to find number of images trained per class
	## Thas obviously no_of_images_per_class - 1 because one image will be taken for testing part

	no_images_trained_per_class=no_of_images_per_class-1

	#Uncomment following to print signature of the trained images

	#print "Printing the signature/co-relation matrix of the trained image 
	#print signature_images_for_train_set

	####### Uncomment the following lines when any lengths or the types of the signature variable are to be checked
 
	#print "signature type"
	#print type(signature_images_for_train_set)
	#print "signature length"
	#print len(signature_images_for_train_set)

# Calling the testdb in test_database.py which takes in quite a number of arguments, lets explore the arguments

# arg_1 : signature_images_for_train_set :  contains the signatures (mapped images / eigen images ) for the entire training dataset ( which is return by train_database )
# arg_2 : test_data_set : contains the list of test data images which is randomly selected, one from each class
# arg_3 : entire_train_data_as_list : contains entire train data set ( removed test_data_set from original input ) 
# arg_4 : mean_img : contains the mean of all the images, its a 1-d array/list ( which is return by train_database )
# arg_5 : eigen_selected : Usually only the major values of the eigen vector are taken, this contain those major eigen values only ( which is return by train_database )
# arg_6 : no_images_trained_per_class : contains  number of images actually trained per class from the original dataset 
# arg_7 : flag_for_tesing : flag which actually if the given directory structure is flat or hierarchy; It sets the flag if the structure is flat


	r=test_database.testdb(signature_images_for_train_set,test_data_set,entire_train_data_as_list,mean_img,eigen_selected,no_images_trained_per_class,flag_for_testing)
	
	return r
	
	
	

if __name__=='__main__':
	arg=sys.argv
	pre_process(sys.argv[1])

