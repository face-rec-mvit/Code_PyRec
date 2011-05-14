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

import numpy
import Image
import initial_processing as ip
import scipy
import scipy.linalg
import sys
import os

# testdb function in test_database.py which takes in quite a number of arguments, lets explore the arguments

# arg_1 : signature_images_for_train_set :  contains the signatures (mapped images / eigen images ) for the entire training dataset ( which is return by train_database )
# arg_2 : test_data_set : contains the list of test data images which is randomly selected, one from each class
# arg_3 : entire_train_data_as_list : contains entire train data set ( removed test_data_set from original input ) 
# arg_4 : mean_img : contains the mean of all the images, its a 1-d array/list ( which is return by train_database )
# arg_5 : eigen_selected : Usually only the major values of the eigen vector are taken, this contain those major eigen values only ( which is return by train_database )
# arg_6 : count_of_dots_original_path : contains number of dots the original path has, this +1 gives number of dots to be replaced to get modified names
# arg_7 : flag_for_tesing : flag which actually says if the given directory structure is flat or hierarchy; It sets the flag if the structure is flat

def testdb(signature_images,test_set,train_set,mean_img_vect_for_test,eigen_selected_for_test,count_of_dots_original_path,flag_for_rename):

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
			print "sucess"
			sucess=sucess+1
		else :
			print "taken class : " + temp_split_taken_name[len_of_split_file_name-2]
			print "recognized class : " +temp_split_recognized_name[len_of_split_file_name-2] 
			print "failure"
			

	print "printing sucess"
	print " identified %d images out of %d images "  %(sucess,len(test_set))
	return (float(sucess)/len(test_set))*100

		

	

#if __name__=='__main__':
#	arg=sys.argv
#	testdb(sys.argv[1])
	
