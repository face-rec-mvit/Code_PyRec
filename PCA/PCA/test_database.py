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

import numpy
import Image
import initial_processing as ip
import scipy
import scipy.linalg
import sys
import os

#this function takes four inputs for processing
#signature_images : contains the signatures of each train image which is a low dimensional image
#test_set : contains the entire test data set of image names
#mean_img_for_test : contains the mean of the trained images which is used for finding eucludian/norm
#eigen_selected_for_test : contains large eigen vectors 

def testdb(signature_images,test_set,train_set,mean_img_vect_for_test,eigen_selected_for_test,trained_images_per_class):
	temp_norm_list=[]
	sucess=0
	signature_images_backup=signature_images
	for i in test_set:
		temp_norm_list=[]
		print "testing undergoing for the image: " +i
		temp_test_image=Image.open(i)
		temp_test_image_vect=ip.imageToVector(i)
		temp_test_image_mean_subtracted=temp_test_image_vect-mean_img_vect_for_test
		temp_test_image_mean_subtracted_transpose=numpy.transpose(temp_test_image_mean_subtracted)
		temp_test_image_mapped=numpy.matrix(temp_test_image_mean_subtracted_transpose)*numpy.matrix(eigen_selected_for_test)

		for j in  range(len(signature_images)):
			temp_for_norm=signature_images[j]-temp_test_image_mapped
			temp_norm_list.append(scipy.linalg.norm(temp_for_norm,2))
		temp_min_in_norm_list=min(temp_norm_list)
		temp_index_min_in_norm_list = temp_norm_list.index(temp_min_in_norm_list)
		
		recognized=train_set[temp_index_min_in_norm_list]
		
########## code of checking if the algorithm identified correctly or not
		temp_split_taken_name=i.split(os.sep)
		temp_split_recognized_name=recognized.split(os.sep)
		len_of_split_file_name=len(temp_split_recognized_name)
		
		if(temp_split_taken_name[len_of_split_file_name-2]==temp_split_recognized_name[len_of_split_file_name-2]):
			print "sucess"
			sucess=sucess+1
		else :
			print "failure"
			

	print "printing sucess"
	print " identified %d images out of %d images "  %(sucess,len(test_set))

		

	

#if __name__=='__main__':
#	arg=sys.argv
#	train(sys.argv[1])
	