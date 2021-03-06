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
import numpy
import sys
import initial_processing as ip
import get_abs_names as lslR
import sys
import Image
import scipy.linalg
import numpy.matlib
from numpy.matlib import zeros

images_abs_names=[] # variable contains all the paths to file
total_img_vect=[]   # variable to contain total images in vector form
mean_img_vect=[]   # variable  for containing mean of all images
sum_img_vect=[]   # variable  for containing sum of all images
mean_for_subtraction=[] # variable contains clones of mean used for subtracting

""" get_files method in the module get_abs_names is called """

src_img_dir=sys.argv[1]
images=lslR.get_files(src_img_dir)    # This should be generic in such a way to be given at run time using sys.argv, To be changed very soon

""" 
we might have to initialise mean_image_vect and sum_image_vect,
so we might required to know the dimension of each image,
so one test image is read and then all the required values are found out

"""
shape_image=Image.open(images[0])
shape_image_array=numpy.asarray(shape_image)
shape=shape_image_array.shape
total_dimensions_per_image=shape[0]*shape[1]

""" 
initialising all the required values such as 
mean_img_vect
sum_img_vect
"""
for i in range(total_dimensions_per_image):
	mean_img_vect.append(0)
	sum_img_vect.append(0)


"""
we might have to convert images to vectors before processing,
so imageToVector method in initial_processing is called
and all individual images are appended to total_img_vect

"""
for i in images :
	image_vect=ip.imageToVector(i)
	total_img_vect.append(image_vect)

""" we might have to number of images to calculate 
mean/sum of the images 
"""
total_no_of_images=len(total_img_vect)

"""finding the total of all the images"""

for i in range(total_no_of_images):
	sum_img_vect=sum_img_vect+total_img_vect[i]

""" finding the mean of all the images """

mean_img_vect=sum_img_vect/total_no_of_images

""" we need to clone mean_img_vect as manytimes as number of images 
to subtract from total_img_vect which actually contains vectors of all 
the images
"""
for i in range(total_no_of_images):
	mean_for_subtraction.append(mean_img_vect)

""" 
the vectors are to be conveted for furthur processsing of 
co-relation etc.., and transpose is taken so it matches the required
order, which is each column containing one image in 2-d matrix
"""
total_img_array=numpy.asarray(total_img_vect)
total_img_array=numpy.transpose(total_img_array)

mean_for_subtraction_array=numpy.asarray(mean_for_subtraction)
mean_for_subtraction_array=numpy.transpose(mean_for_subtraction_array)

""" subtraction of original images with mean is done here for furthur 
processing"""

mean_sub_img_array=total_img_array-mean_for_subtraction_array	

""" Calculating co-relation matrix using mean_subtracted_matrix """

mean_sum_img_array_transpose=numpy.transpose(mean_sub_img_array) # Calculating the transpose
co_relation = numpy.matrix(mean_sum_img_array_transpose)*numpy.matrix(mean_sub_img_array) # casting to matrix and multiplying to form co-relation matrix

""" Calculating Eigen Values and Eigen Vectors """

eig_value,eig_vect = scipy.linalg.eig(co_relation) # returns the eigen values and eigen vectors

""" mapping eigen values onto images"""

eig_vect=numpy.matrix(eig_vect)  # casting to matrix for multiplication
mean_sub_img_array = numpy.matrix(mean_sub_img_array) # casting to matrix for multiplication

mapped_eig = mean_sub_img_array * eig_vect  # Multiplication which maps images to eigen vectors
mapped_eig_array=numpy.asarray(mapped_eig)  # Converting back to array for slicing

no_of_eigen_vectors_to_be_taken=20  # Edit this value to change the no of dimensions to be taken

mapped_eig_large_select=mapped_eig_array[:,0:no_of_eigen_vectors_to_be_taken] # Selecting required number of dimensions using slicing

""" Calculating the signature of each image """

# Creating the matrix ( signature matrix )and initialised with zeros 

cv_signature_images=zeros((total_no_of_images,no_of_eigen_vectors_to_be_taken))
mean_sub_img_array_transpose=numpy.transpose(mean_sub_img_array)  # transpose is taken so it becomes easy for multiplicati

for i in range(total_no_of_images) :
	cv_signature_images[i]=mean_sub_img_array_transpose[i] * mapped_eig_large_select

print cv_signature_images.shape 
print " is the sizeof the signature matrix " 

 

""" cv_signature_images contains the signature of all the test images with each images consisting of only "no_of_eigen_vectors_to_be_taken" number of dimensions """
	



