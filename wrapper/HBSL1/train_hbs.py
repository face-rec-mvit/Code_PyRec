#<This script does training of HBS, Histogram Based Similarity Face recognition .>
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

import Image
import sys
import numpy

### get_histogram : Function that takes image as a input and returns histogram of the image
# Input : image
#Output/return : histogram of the image


def get_histgram(image):
	image_array=numpy.asarray(image)
	image_array_flat=image_array.flatten()
	image_histogram=numpy.histogram(image_array_flat,10,(0,255))
	return image_histogram[0]

### train_images_as_hists : returns the histogram of the set of images
# Input : List containing paths of trained images
# Output/return - List containing histograms of the trained images

def train_images_as_hists(hbs_images_to_train):
	train_hist=[]
	for i in range(len(hbs_images_to_train)):
		temp_image=Image.open(hbs_images_to_train[i])
		temp_image_hist=get_histgram(temp_image)
		train_hist.append(temp_image_hist)
	#Uncomment following to print the list of histograms of the trained images
	#print "printing histogram"	
	#print train_hist
	return train_hist
	
		

if __name__=='__main__':
	train_images_as_hists(sys.argv[1])	
	
