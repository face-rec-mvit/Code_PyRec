#<This script does training of PCA-Principle Component Analysis .>
#    Copyright (C) <2011>  <Authors : Dharani,Guruprasad, Kiran Tej, Kunal Ghosh>
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

"""

#! /usr/bin/python

""" importing all the required modules"""
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

def train(pathtoimages):
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

# get_files method in the module get_abs_names is called 
	src_img_dir=pathtoimages
	images=lslR.get_files(src_img_dir)    
	images_abs_names=images

#we might have to initialise mean_image_vect and sum_image_vect,
#so we might required to know the dimension of each image,
#so one test image is read and then all the required values are found out

	shape_image=Image.open(images[0])
	shape_image_array=numpy.asarray(shape_image)
	shape=shape_image_array.shape
	total_dimensions_per_image=shape[0]*shape[1]


#initialising all the required values such as mean_img_vect, sum_img_vect

	for i in range(total_dimensions_per_image):
		mean_img_vect.append(0)
		sum_img_vect.append(0)

#the code which actually partitions the entire database of images into trainset and testset goes here
	no_of_images=len(images)
	for i in range(no_of_images):
		temp_image=images[i].split(os.sep)
		split_image_names.append(temp_image)

#this part is to find the length of  the path of each image to extract class name
	
	single_image_to_find_length=split_image_names[0]
	length_split_image_name=len(single_image_to_find_length)

#Code to extract the class names of the database

	for i in range(no_of_images):
		temp_class_name=split_image_names[i][length_split_image_name-2]  #extracting class names
		class_names.append(temp_class_name)  # creating a list of class names 
	#print class_names
	set_of_class_names=set(class_names)  #removing the repetitions using set so it contains only unique classes
	#print set_of_class_names
	no_of_classes=len(set_of_class_names)  #getting the count of no of classes
	no_of_images_per_class=no_of_images/no_of_classes  #getting the count of no of images per class
	#print no_of_images_per_class
	
#arranging the input directory of images into the order of class

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
	
	#print type(train_data_set)
	#print "printing training data set"
	#print train_data_set
			
	test_data_set_matrix=numpy.matrix(test_data_set)
	train_data_set_matrix=numpy.matrix(train_data_set)
	
	#print test_data_set_matrix.shape
	#print train_data_set_matrix.shape
	
	#print "printing one individual image in training data set"
	
	#print train_data_set

# we need the entire training data set as a single list
	for r in  range(no_of_classes):
		c=0
		for c in range(no_of_images_per_class-1):
			entire_train_data_as_list.append(train_data_set[r][c])
	
	mean_img,eigen_selected,signature_images_for_train_set=train_database.traindb(train_data_set)

	#print signature_images_for_train_set
	print "signature type"
	print type(signature_images_for_train_set)
	print "signature length"
	print len(signature_images_for_train_set)
	
	test_database.testdb(signature_images_for_train_set,test_data_set,entire_train_data_as_list,mean_img,eigen_selected,no_of_images_per_class-1)
	
	
	
	#entire_class_matrix=numpy.matrix(entire_class)
	
	#print entire_class_matrix.shape
	
# Need to create a dictonary in which class name as the key and all images under that class as a list of images which is a key

	set_of_class_names

	
	



#we might have to convert images to vectors before processing,
#so imageToVector method in initial_processing is called
#and all individual images are appended to total_img_vect


# "C:\\Documents and Settings\\sapna\\Desktop\\Face rec\\9-2-2011\\PCA\\ORL"

#	for i in images :
#		image_vect=ip.imageToVector(i)
#		total_img_vect.append(image_vect)
#	print len(total_img_vect)
#	total_img_vect_matrix=numpy.matrix(total_img_vect)
#	print total_img_vect_matrix.shape

if __name__=='__main__':
	arg=sys.argv
	train(sys.argv[1])

