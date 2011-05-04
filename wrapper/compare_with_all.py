import Image
import numpy
import os
#import PCA_train_generic
from PCA2 import PCA_main
import return_percent_pixels

algorithms = ["PCA","HBSL1","HBSL2","DCT","LPP",]

def compare_hist_percentage(new_percent_pixels,trained_percent_pixels_inst):
	diff=new_percent_pixels-trained_percent_pixels_inst
	print "The difference between new database and trained database is "
	#print diff
	return (sum(abs(diff)))

def choose_best_algo(new_database,trained_datasets):

	#### New database should be checked on all the algorithms and the best case efficiency should be taken for furthur uses

	trained_percent_pixels=[]
	diff_new_trained=[]
	new_percent_pixels=return_percent_pixels.return_pp(new_database)
	
	for i in trained_datasets:
		trained_percent_pixels.append(return_percent_pixels.return_pp(i[0]))
	#print "Print perentage of trained_pixels of all trained datasets	
	#print trained_percent_pixels
	
	for i in range(len(trained_datasets)):
		diff_new_trained.append(compare_hist_percentage(new_percent_pixels,trained_percent_pixels[i]))
	min_diff=min(diff_new_trained)
	index=diff_new_trained.index(min_diff)
	algo_chosen=trained_datasets[index][1]
		
	return algorithms.index(algo_chosen)
	
	

