#<This script returns all the image paths as output on inputing the directory path.>
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


#! /usr/bin/python

import os
import sys

def gen_files(files,top,names):
    for name in names:
        path = top + os.sep + str(name)
        #use os specific path separator
        if os.path.isfile(path):
            files.append(path)
    return files

def get_files(directory,ftype=None):
    """
    The function lists all files in the top level
    directory "directory" , by default it returns all the
    file types.

    The can be forced to return only certain file types
    by passing the types as a list , as a second argument.
    e.g. ["jpeg","jpg","pgm"] 
    """

    files=list()
    directory = os.path.abspath(directory)
    
    if directory == None :
        print """
        Purpose: List files recursively in a directory
        usage:   get_abs_path_of_all_files_in_directory [options] [directory path]

        options:
        comma separated list of file type which must ONLY be returned.
        example : --types=jpeg,jpg
        """
        return "ERROR : Plese enter a valid directory"

    elif ftype != None :
        #file type(s) is/are mentioned        
        os.path.walk(directory,gen_files,files)
        #arg[0] is now populated with the files in the directory
        ftemp = files
        newList = list()
        for f in ftemp:
            for typ in ftype:
                if f.endswith(typ):
                    newList.append(f)
        files = newList

    else :
        os.path.walk(directory,gen_files,files)
        
    return files

def print_list(l):
    for entry in l:
        print entry

if __name__ == '__main__' :
    arg = sys.argv

    if len(arg) == 2:
        dirname = arg[1]
        print dirname,2
        file_list = get_files(dirname,None)
        print_list(file_list)

    elif len(arg) == 3:
        dirname = arg[2]
        if ( arg[1].startswith("--types=" )):
            arg[1]=arg[1][len("--types="):]
            ftype=arg[1].split(",")            
            file_list = get_files(dirname,ftype)
            print_list(file_list)
        else:
            print "Error in --types"#return(1)
    else:
        print get_files(None)




