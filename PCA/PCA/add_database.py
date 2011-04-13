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

database=[]

import pickle
import sys

def add_db(db_path):
	file_pointer_to_read_db=open("trained_databases","r")
	file_pointer_to_read_db.seek(0)
	list_old=pickle.load(file_pointer_to_read_db)
	list_old.append(db_path)
	
	fp=open("trained_databases","w+")
	fp.seek(0)
	pickle.dump(list_old,fp)
	fp.close()
	file_pointer_to_read_db.close()
	
	#print list_old
	

if __name__=='__main__':
	arg=sys.argv
	no_of_databases_initially_trained=len(arg)-1
	for i in range(no_of_databases_initially_trained):
		database.append(arg[i+1])
	print "printing databases"
	print database
	fp=open("trained_databases","w+")
	pickle.dump(database,fp)
	fp.close()
