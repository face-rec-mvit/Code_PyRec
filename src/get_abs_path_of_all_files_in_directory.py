#! /usr/bin/python

import os
import sys
import re

def gen_files(files,top,names):
    for name in names:
        path = top + os.sep + str(name)
        #use os specific path separator
        if os.path.isfile(path):
            files.append(path)
    return files

def get_files(directory,include=None,exclude=None,ftype=None):
    """
    The function lists all files in the top level
    directory "directory" , by default it returns all the
    file types.

    include takes in a regular expression (as a string)
    and returns files only matching the include regex

    exclude takes in a regular expression (as a string)
    and DOES NOT RETURN files that match the exclude regex

    NOTE : Both include and exclude CAN BE applied to gether,
    in which case INCLUDE is run through FIRST and THEN EXCLUDE
    AND BOTH USE THE PYTHON REGEX MODULE and ARE CASE SENSITIVE

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
        --types :   comma separated list of file type which must ONLY be returned.
                    example : --types jpeg,jpg
        --include:  a regular expression of files to include
                    example : --include "hello(world)?" , matches hello,hello
                    world
        --exclude:  a regular expression of files to exclude
                    example : --exclude "hello(world)?" , exclude hello,hello
                    world for the list of displayed files
        NOTE:
        1. IF include and exclude are both provided then first Include is
        executed and then Exclude.
        2. --include "" is treated as IGNORE THE FLAG, --exclude is similar
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
    
    if include != None and len(include) != 0:
        """
        KEEP FILES that MATCH the regex 
        !=0 is to handle the case where the user enters
        --include "" which is treated as IGNORE THE FLAG
        """
        #print 
        #"""
        #No error handling is done, Please check re module of
        #python in case you come across errors.
        #"""

        regex_include = re.compile(include)#,re.IGNORECASE)#uncomment to make case insensitive
        included_list=[]
        for entry in files:
            result = regex_include.search(str(entry).strip())
            #the string is stripped() before searching
            if result :#regex not in filename
                included_list.append(entry)
        #print "include is:",include
        #included_list=[]
        #for entry in files:
        #    result = entry.find(include)
        #    if result >=0 :
        #        included_list.append(entry)
        files = included_list


    if exclude != None and len(exclude) != 0:
        """
        DELETE FILES that MATCH the entry
        !=0 is to handle the case where the user enters
        --exclude "" which is treated as IGNORE THE FLAG
        """
        #print 
        #"""
        #No error handling is done, Please check re module of
        #python in case you come across errors.
        #"""

        regex_exclude = re.compile(exclude)#,re.IGNORECASE)#uncomment to make case insensitive
        excluded_list=[]
        for entry in files:
            result = regex_exclude.search(str(entry).strip())
            #the string is stripped() before searching
            if not result:
                excluded_list.append(entry)
        files = excluded_list

    return files

def print_list(l):
    for entry in l:
        print entry

if __name__ == '__main__' :
    arg = sys.argv
    dirname = arg[len(arg)-1]
    type_list = None
    includ = None
    exclud = None 
    #the last argument is the directory name 
    
    if len(arg) == 1:
        print get_files(None)
    elif len(arg) == 2:
        file_list = get_files(directory=dirname,ftype=None)
        print_list(file_list)
    else:
        #elif len(arg) == 3:
        #    dirname = arg[2]
        #    if ( arg[1].startswith("--types=" )):
        #        arg[1]=arg[1][len("--types="):]
        #        typ=arg[1].split(",")            
        #        file_list = get_files(directory=dirname,ftype=typ)
        #        print_list(file_list)
        #    else:
        #        print "Error in --types"#return(1)
        if "--types" in arg:
            type_list = arg[arg.index("--types")+1].split(",")
            #print type_list
        if "--include" in arg:
            includ = str(arg[arg.index("--include")+1])
            #print type_list,includ,exclud
        if "--exclude" in arg:
            exclud = str(arg[arg.index("--exclude")+1])
            #print type_list,includ,exclud

        print dirname,type_list,includ,exclud
        file_list = \
        get_files(directory=dirname,include=includ,exclude=exclud,ftype=type_list)
        print_list(file_list)


