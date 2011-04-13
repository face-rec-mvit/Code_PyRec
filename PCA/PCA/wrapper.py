#< This script has the wrapper which decides on which algorithm to be chosen. >
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

import PCA_train_generic
import initial_processing as ip
import get_abs_names as lslR
import Image
import sys
import random
from PIL import ImageStat
import getmetrics
import pickle
import add_database
import shutil
import os

###### get_db_name returns the database name 
#### Input : path of database
## Output : Database name

def get_db_name(db_path):
	db_split_path_names=db_path.split(os.sep)
	return(db_split_path_names[len(db_split_path_names)-1])


####### decide_algo function depending on the input decides on the best algorithm to be chosen
##### Input : Given by the user which has the input directory names
### Depending on some metrics it actually decides on which algorithm to be chosen

#trained_datasets=['/home/kiran/Documents/Facerec/databases/ORL','/home/kiran/Documents/Facerec/databases/yalefaces gif','/home/kiran/Documents/Facerec/databases/yalefaces pgm']

#'/home/kiran/Documents/Facerec/databases/trained/YALE RESIZED DATASET'


def decide_algo(input_str):
	
	#print input_str
		
	wrapper_test_image_names = lslR.get_files(input_str)
	
	#Uncomment following 2-lines to print all the image names

	#print "image names"
	#print wrapper_test_image_names

	wrapper_test_image_names.sort()
	no_of_images=len(wrapper_test_image_names)
	randomly_selected_image=random.random()*no_of_images
	randomly_selected_image=int(round(randomly_selected_image))
	
	#Uncomment following 2 - lines to print the index randomly selected image

	#print "Index of randomly selected image = %d" %(randomly_selected_image)

	#print "number of images"
	#print len(wrapper_test_image_names)

	wrapper_test_image=Image.open(wrapper_test_image_names[randomly_selected_image])
	
	test_image_stat=ImageStat.Stat(wrapper_test_image)

######## We will be doing the decision based on the 16-metrices. 
###### Only when the test image (image set) satisfies all the 16 metrices it means that the given test database is actually one of the trained dataset
#### If test image fails to meet all the 16-metric criteria, then the wrapper depending on how close the new data set is decides which algorithm to be chosen
## Over time it actually appends the values and maintains the updated metrices of the trained dataset of the new data set

####### We actually test only one image of the entire given test data set ( using the old taught which says one rice grain is often enough to say whether the rice is boiled #### or not, similar we regressively test only one image of the dataset ( given by the user ) ) and choose the algorithm.


####### Image.Stat properties

	flag=1

	metric = getmetrics.return_metrics(wrapper_test_image_names[randomly_selected_image])

##### We need to get the names of the databases which are previously trained 	
	fp_for_trained_db=open("trained_databases","r")
	fp_for_trained_db.seek(0)
	trained_datasets=pickle.load(fp_for_trained_db)	
	
	for i in range(len(trained_datasets)):	
		face_names=lslR.get_files(trained_datasets[i])
		face_names.sort()
		#image_selected=Image.open(face_names[randomly_selected_image])
		trained_metric=getmetrics.return_metrics(face_names[randomly_selected_image])
		
		if(metric.__eq__(trained_metric)):

			print "Data base identified"
			print "Identified database is"
			print trained_datasets[i]
			flag=0
			break  
	if(flag==1): # means database not identified
		##### Need to extract the trained dataset path 
		trained_data_path=trained_datasets[0]
		rindex_ossep=trained_data_path.rindex(os.sep)
		trained_data_path=trained_data_path[0:rindex_ossep]
		src_path=input_str
		dest_path=trained_data_path+os.sep
		dest_path=dest_path+get_db_name(input_str)
		
		
		print "Data base not identifed"
		shutil.copytree(src_path,dest_path)
		add_database.add_db(sys.argv[1])
		print "Database added"

	
	
	

####### Trying out pickel but loading only the randomly selected image at run time looks cool coz of efficiency issues

	
	#fp=open('metric_pickle_test','w+')
	#pickle.dump(metric,fp)
	#fp.close()
	#f=open('metric_pickle_test','r+')
	#m=pickle.load(f)
	#print m.__eq__(metric)
	
	#print "printing metric list"
	#print metric


"""	test_mean=test_image_stat._getmean()
	print test_mean
	
	
	test_median=test_image_stat._getmedian()
	print test_median

	test_count_dimensions=test_image_stat._getcount()
	print test_count_dimensions

	test_extremes=test_image_stat._getextrema()
	print test_extremes

	test_rms=test_image_stat.rms
	print test_rms

	test_std_dev=test_image_stat._getstddev()
	print test_std_dev

	test_sum=test_image_stat._getsum()
	print test_sum

	test_sum_square=test_image_stat._getsum2()
	print test_sum_square

	test_var=test_image_stat._getvar()
	print test_var


####### Image properties

	test_image_size=wrapper_test_image.size
	print test_image_size

	test_image_format=wrapper_test_image.format
	print test_image_format

	test_image_mode=wrapper_test_image.mode
	print test_image_mode

	test_image_category=wrapper_test_image.category
	print test_image_category

	test_image_colors=wrapper_test_image.getcolors()
	print test_image_colors

	test_image_histogram=wrapper_test_image.histogram()
	print test_image_histogram

	test_image_arbitrary_pixel=wrapper_test_image.getpixel((56,65))
	print test_image_arbitrary_pixel
	
	

	
	print type(test_mean[0])
	print len(test_mean)

#	wrapper_test_image.show() """
	
	
	
	
	
	

if __name__=='__main__':
	arg=sys.argv
	decide_algo(sys.argv[1])
