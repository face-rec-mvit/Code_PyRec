#< This script metrics of the image as list. >
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

#import PCA_train_generic
import initial_processing as ip
import get_abs_names as lslR
import Image
import sys
import random
from PIL import ImageStat

####### return_metrics function returns the metrics of the input image as list
##### Input : path to the image
### Output : 16 metrics of the image is the list datastructure


def return_metrics(input_image_path):
	
	metric_details_as_list=[]	
	metric_image=Image.open(input_image_path)
	
	metric_image_stat=ImageStat.Stat(metric_image)


####### Image.Stat properties

	test_mean=metric_image_stat._getmean()
	metric_details_as_list.append(test_mean)

	
	
	test_median=metric_image_stat._getmedian()
	metric_details_as_list.append(test_median)

	test_count_dimensions=metric_image_stat._getcount()
	metric_details_as_list.append(test_count_dimensions)
	
	test_extremes=metric_image_stat._getextrema()
	metric_details_as_list.append(test_extremes)

	test_rms=metric_image_stat.rms
	metric_details_as_list.append(test_rms)
	
	test_std_dev=metric_image_stat._getstddev()
	metric_details_as_list.append(test_std_dev)

	test_sum=metric_image_stat._getsum()
	metric_details_as_list.append(test_sum)

	test_sum_square=metric_image_stat._getsum2()
	metric_details_as_list.append(test_sum_square)

	test_var=metric_image_stat._getvar()
	metric_details_as_list.append(test_var)
		
####### Image properties

	test_image_size=metric_image.size
	metric_details_as_list.append(test_image_size)
	x_for_pix=test_image_size[0]/2
	y_for_pix=test_image_size[1]/2

#	print test_image_size

	test_image_format=metric_image.format
	metric_details_as_list.append(test_image_format)
#	print test_image_format

	test_image_mode=metric_image.mode
	metric_details_as_list.append(test_image_mode)
#	print test_image_mode

	test_image_category=metric_image.category
	metric_details_as_list.append(test_image_category)
#	print test_image_category

	test_image_colors=metric_image.getcolors()
	metric_details_as_list.append(test_image_colors)
#	print test_image_colors

	test_image_histogram=metric_image.histogram()
	metric_details_as_list.append(test_image_histogram)
#	print test_image_histogram

	test_image_arbitrary_pixel=metric_image.getpixel((x_for_pix,y_for_pix))
	metric_details_as_list.append(test_image_arbitrary_pixel)
#	print test_image_arbitrary_pixel

	return metric_details_as_list

	

	
	

if __name__=='__main__':
	arg=sys.argv
	metric_details=return_metrics(sys.argv[1])
	print metric_details
