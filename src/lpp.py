#! /usr/bin/python

import numpy
import initial_processing
import get_abs_path_of_all_files_in_directory as lslR
import sys
import kNN

#------Please Fill in the following details------
"""
NOTE :
Either give the image directory and specify a keywords for classes
OR
Give the Class Image Directory
"""
class Image_Directory(object) :
    ###directory where the images are present
    IMAGE_DIRECTORY = ""
    """
    The pattern will be matched against
    the absolute path of the image
    kind of like grep

    keywords = {
                    0:"pattern0" ,
                    1:"pattern1" ,
                    2:"pattern2"
               }
    It is done this way so that you can specify
    all images in a class by a regexp
    """
    keywords = {}
    xs = []
    ys = []
    #model of type kNN is created in __init__
    k=int()
    #adjacency_matrix = list()#create in __init__
    #weight_matrix = list() #create in __init__
    """
    ftypes is a list of all the types of images that must
    be included from the directory mentioned.
    Defaults to None
    """
    ftypes = list()
    def __init__(self,image_directory,keys,types=None):
        self.IMAGE_DIRECTORY=image_directory
        self.keywords = keys
        self.ftypes = types
        self.create_xs_ys()
        self.k = len(numpy.unique(self.ys))
        self.model = kNN.train(self.xs,self.ys,numpy.unique(self.ys))
        self.adjacency_matrix = self.create_adjacency_matrix()
        self.weight_matrix = self.create_weight_matrix()

    def create_xs_ys(self):
        files_list = lslR.get_files(self.IMAGE_DIRECTORY,self.ftypes)
        for file in files_list:
            for item in self.keywords.iteritems():
                key = item[0]
                value = item[1]
                if file.rfind(value) != -1 :
                    self.xs.append(initial_processing.imageToVector(file))
                    self.ys.append(key)

    def create_weight_matrix(self):
        mat = list()
        for image in self.xs:
            w,dist = kNN.calculate(self.model,image)
            mat.append([(distance) for (distance , node) in dist])
        return mat

    def create_adjacency_matrix(self):
        col = list()
        #for i in self.ys:
        #    row = list()
        #    for j in self.ys:
        #        if self.ys.index(i) == self.ys.index(j):
        #            print "index equal %s  %s " % (self.ys.index(i) , self.ys.index(j))
        #            continue
        #        elif self.ys[i] == self.ys[j]:
        #            print "value equal %s  %s " % (self.ys.index(i) , self.ys.index(j))
        #            row.append(1)
        #        else:
        #            row.append(0)
        #    col.append(row)
        for i in range(len(self.ys)):
            row = list()
            for j in range(len(self.ys)):
                #if i==j:
                #    continue
                #elif self.ys[i] == self.ys[j]:
                if self.ys[i] == self.ys[j]:
                    row.append(1)
                else:
                    row.append(0)
                col.append(row)
        return col

    def print_adjacency_matrix(self):
        for i in self.adjacency_matrix:
            print i

    def print_weight_matrix(self):
        for i in self.weight_matrix:
            print i



class Class_Directory(object) :
    """
    directory containing text files
    like so : 0.txt , 1.txt
    [class number].txt
    containing absolute paths of images belonging
    to that class
    """
    CLASS_IMAGE_DIRECTORY = ""


if __name__ == '__main__':
    #print """
    #This file is to be used from within a python interpreter
    #as of now.
    #"""
    arg = sys.argv

    if len(arg) != 4:
        print """
        Incorrect number of arguments.
        Usage:

        python lpp.py <directory> "<keys separated by ;>" "<types of files separated by ,>"

        e.g. you want all path names with "rego0" to belong to the 0th class 
        and "rego1" in the 1st class you must write. 

        python lpp.py /path/to/images "rego0;rego1" "png"

        NOTE: ALL ARGUMENTS ARE NECESSARY
        AND THIS IS JUST FOR TESTING , CALL lpp.py FROM ANOTHER PROGRAM 
        FOR PRACTICAL PURPOSES.
        """
    else:
        #get the directory
        directory = arg[1]
        
        #get the keys and convert them to dictionary
        temp = arg[2].split(";")
        classes = [i for i in range(len(temp))]
        keys = dict(zip(classes,temp))

        #get the file types
        types = arg[3].split(",")
        
        ImageDir_Object = Image_Directory(directory,keys,types)
        print "Success !!! ImageDir_Object Created"
        print "Adjacency Matrix" ,ImageDir_Object.print_adjacency_matrix()
        print "Weight Matrix", ImageDir_Object.print_weight_matrix()
        print "NOTE : To use this module , call it from another program"


