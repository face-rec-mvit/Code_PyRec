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

algorithms_m=["PCA","DCT","LPP"]
best_chosen_algo=[]
dataset_algo=[]

import pickle
import train_with_all
import sys

def store_map_main():
	fp_sm=open("trained_databases","r")
	trained_dbs=pickle.load(fp_sm)
	print trained_dbs
	for i in range(len(trained_dbs)):
		algo_index=train_with_all.choose_best(trained_dbs[i])
		best_chosen_algo.append(algorithms_m[algo_index])
	print best_chosen_algo
	
	for i in range(len(trained_dbs)):
		temp=[]
		temp.append(trained_dbs[i])
		temp.append(best_chosen_algo[i])
		dataset_algo.append(temp)
	print dataset_algo
	
	fp_dataset_algo=open("mapping_dataset_algo","w+")
	pickle.dump(dataset_algo,fp_dataset_algo)

def store_map(new_to_map):
	fp_dataset_algo=open("mapping_dataset_algo","r")
	previously_mapped=pickle.load(fp_dataset_algo)
	fp_dataset_algo.close()
	algo_index=train_with_all.choose_best(new_to_map)
	best_chosen_new=algorithms_m[algo_index]
	temp=[]
	temp.append(new_to_map)
	temp.append(best_chosen_new)
	previously_mapped.append(temp)

	# Opening the same for updating purpose
	
	fp_dataset_algo_for_update=open("mapping_dataset_algo","w+")	
	fp_dataset_algo_for_update.seek(0)
	pickle.dump(previously_mapped,fp_dataset_algo_for_update)
	fp_dataset_algo_for_update.close()

				

if __name__=='__main__':
	#arg=sys.argv
	store_map_main()
