import get_abs_names
import initial_processing
import sys
import numpy
import Image

def return_pp(img_dir):
	names=get_abs_names.get_files(img_dir)
	names.sort()
	image_vector=[]
	for i in range(len(names)):
		image_vector.append(initial_processing.imageToVector(names[i]))
	#print image_vector
	#print len(image_vector)

	sum_img=image_vector[-1]
	for i in range(len(image_vector)-1):
		sum_img=sum_img+image_vector[i]

	# Uncomment to know the sum image
	
	#print "printing sum image"
	#print sum_img
	hist_img=numpy.histogram(sum_img,bins=34)
	
	## Uncoment to now the histogram 	
	
	#print "Printing histogram"
	#print hist_img

	img_for_dimension=Image.open(names[0])
	percent_of_pixels=(hist_img[0]/float(img_for_dimension.size[0]*img_for_dimension.size[1]))*100
	
	# Uncomment to know the details  of percentage of pixels present per bucket range

	#print "Printing percentage of pixels"
	#print percent_of_pixels
	#print len(percent_of_pixels)
	#print sum(percent_of_pixels)

	return percent_of_pixels
		

if __name__=='__main__':
	return_hist(sys.argv[1])
