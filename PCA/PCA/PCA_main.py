import frame_work
import train_database
import test_database
import sys

def main_pca(images_path):

#Calling the function pre_process of frame_work, this returns some values in the following order, using those return values the training part and testing part is called by passing the required #arguments

#return order : train_data_set,entire_train_data_as_list,no_of_classes,no_of_images_per_class,test_data_set,flag_for_testing
#	
# ret1: train_data_set = list of all training images as an 2-d array
# ret2: entire_train_data_as_list = list of all training images as a single list
# ret3:	no_of_classes = total number of classes in the given input database
# ret4:	no_of_images_per_class= Number  of images per class
# ret5:	test_data_set=list of training images as a 1-array ( In case user wants, can be typecasted to list in his script using this return value )
# ret6: flag_for_testing=This is the flag which says about the directory directory structure. 
#	                 flag_for_testing = 1 , means the directory structure is flat, means modifications of path names is necessary to extract class names
# 			 flag_for_testing = 0 , means the directory structure is hierarchical which means modifcations is not necessary for extracting class names

	
	train_data_set,entire_train_data_as_list,no_of_classes,no_of_images_per_class,test_data_set,flag_for_testing=frame_work.pre_process(images_path)	

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
# arg_7 : flag_for_tesing : flag which actually says if the given directory structure is flat or hierarchy; It sets the flag if the structure is flat


	r=test_database.testdb(signature_images_for_train_set,test_data_set,entire_train_data_as_list,mean_img,eigen_selected,no_images_trained_per_class,flag_for_testing)
	
	print "efficiency is "	
	print r

if __name__=='__main__':
	main_pca(sys.argv[1])
