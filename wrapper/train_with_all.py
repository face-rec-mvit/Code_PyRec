#<This script trains the database with all the algorithms and decides on the best.>
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

import os
#import PCA_train_generic
import return_percent_pixels
from PCA2 import PCA_main
from HBSL1 import histogram_main_L1
from HBSL2 import histogram_main_L2


def choose_best(new_database):

	#### New database should be checked on all the algorithms and the best case efficiency should be taken for furthur uses

		
	#print efficiency_PCA

	efficiency_PCA=PCA_main.main_pca(new_database)
	efficiency_LPP=0
	efficiency_DCT=0
	efficiency_histL1=histogram_main_L1.histmain(new_database)
	efficiency_histL2=histogram_main_L2.histmain(new_database)
	
	efficiency=[efficiency_PCA,efficiency_histL1,efficiency_histL2,efficiency_DCT,efficiency_LPP,]
	max_efficiency=max(efficiency)
	max_efficiency_index=efficiency.index(max_efficiency)
	
	#print "Printing PCA and HBS efficiency"
	#print efficiency_PCA
	#print efficiency_hist

	
	print "printing max efficiency "
	print max_efficiency
	
	"""if(max_efficiency_index==0) :
		print "PCA"
	if(max_efficiency_index==1) :
		print "DCT"
	if(max_efficiency_index==2) :
		print "LPP" 
"""
	return max_efficiency_index

	
	
	
if __name__=='__main__':
	arg=sys.argv
	choose_best_for_new(sys.argv[1])
