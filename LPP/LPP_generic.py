#! /usr/bin/python

import time
import os
import sys
import random
import numpy as np
from src import get_abs_path_of_all_files_in_directory as lslR
from src import lpp

def getRandom(minimum,maximum,count):
    """
    returns a list of count number of  unique random numbers
    in the range minimum and maximum
    """
    nums = []    
    while(len(nums) != count):
        num=random.randint(minimum,maximum)
        if num not in nums:
            nums.append(num)
    return nums
    
def LPP(directory,testImageCount=30):
    """
    This is the wrapper LPP function which takes in only the face database
    (directory containing face images) and returns the efficiency of LPP 
    when run on the database.
    
    testImageCount is the number of images taken in the test case. This is an 
    arbitrary number. Unique random images are taken from the Image Database
    to be included in the Test Set.
    
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
    Files = []
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
            Files.append(f)
            if Class in classList:            
                pass
                #if Class is already there in classList then ignore        
            else:
                classList.append(Class)
                #if Class is not in List then append it                
                
    
    #generate testImageCount unique random numbers
    randList=getRandom(minimum=0,maximum=len(Files),count=30)
    
    #generate the string of file names that are to be included in the testSet
    testString = ""
    for num in randList:
        testString += str(Files[num])+"|"
    #remove the trailing |
    testString=testString[:-1]
    
    #print testString
    
    #Now call the LPP methods
    ImageDir=lpp.Image_Directory(directory,classKeys=dict(zip(range(len(Class)),Class)),ftype=Type,exclude=testString,numOfEigVectors=100)
    efficiency=ImageDir.test(directory,classKeys=dict(zip(Class,range(len(Class)))),include=testString)
    
    return efficiency
    
if __name__ == '__main__':
    efficiency = LPP(sys.argv[1])
    print "The efficiency of LPP with the given dataset is %f" % (efficiency*100)
