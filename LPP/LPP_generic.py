#! /usr/bin/python

from src import lpp
import numpy as np
import time
import os
import sys
from src import get_abs_path_of_all_files_in_directory as lslR

def LPP(directory):
    """
    This is the wrapper LPP function which takes in only the face database
    (directory containing face images) and returns the efficiency of LPP 
    when run on the database.
    
    NOTE:
    1.The file type is assumed to be the one with maximum occurance in the
    database.    
    2.If the files are to be considered they must have a type.
    3.All images in a directory are considered to be in a class.
    4.The test images are chosen at random 1 from each class.    
    """
    filesList = lslR.get_files(directory)
    dictType = {}
    #dictType is a dictionary of file extensions (.jpg , .pgm ,etc) followed
    #by their occurrance , the extension with maximum occurrance is chosen as the
    #extension of files to be considered for recognition
    classList = []
    #classList is a list of all last directory names in the directory tree of 
    #the face image database. These are assumed to denote classes.
    File = []
    #this list is almost as same as filesList except that this list contains only
    #files having a max occurring extension
    
    for f in filesList:
        Type = f.split(".")[-1]
        #get the extension of the File
        if Type in dictType:
            dictType[Type] += 1
        else:
            dictType[Type]=1
        #if the extension is encountered before, increment occurrance
        #by 1 else make it 1              
    
    Type = [key for key,value in dictType.items() if value is max(dictType.values())]
    #Type is the key with most occurrance in the dictType dictionary
    
    for f in filesList:
        if f.endswith(Type[0]):
            Class = f.split(os.sep)[-2]        
            #get the name of the last directory
            
            
            if Class in classList:            
                pass
                #if Class is already there in classList then ignore        
            else:
                classList.append(Class)
                #if Class is not in List then append it                
        
    #print "Dict Type:" ,dictType
    print "Class List :" ,classList
    

if __name__ == "__main__":
    efficiency = LPP(sys.argv[1])
    print "The efficiency of LPP with the given dataset is %d" % efficiency
