#< This script adds the database to the previously trained dataset or this can also be used to create initial list of trained datasets by calling directly. >
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

database=[]

import pickle
import sys

def add_db(db_path):
	file_pointer_to_read_db=open("trained_databases","r") # For writing purposes it should be opened in "r" mode 
	file_pointer_to_read_db.seek(0) # not required but on safer side it again made to point to beginning
	list_old=pickle.load(file_pointer_to_read_db) # Loading from pickle to list
	list_old.append(db_path) # Creating a new list , by adding the newly available database name
	
	fp=open("trained_databases","w+") # For writing purposes it should be opened in "w+" mode 
	fp.seek(0)
	pickle.dump(list_old,fp)  # writing to pickle
	fp.close()
	file_pointer_to_read_db.close()
	
	#print list_old
	

if __name__=='__main__':
	arg=sys.argv # back up
	no_of_databases_initially_trained=len(arg)-1 # -1 coz one argument is file.py itself 
	for i in range(no_of_databases_initially_trained):
		database.append(arg[i+1])  # Creating a list of all the databases initially to be trained
	print "printing databases"
	print database # Printing databases for initial training as list
	fp=open("trained_databases","w+") # For writing purposes it should be opened in "w+" mode
	pickle.dump(database,fp)  # Writing to file
	fp.close() 
