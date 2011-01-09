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
    It is done this way because you
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
        for image in self.xs:
            w,dist = kNN.calculate(self.model,image)
            self.weight_matrix.append([(distance) for (distance , node) in dist])

    def create_adjacency_matrix(self):
        temp = list()
        for i in self.ys:
            for j in self.ys:
                if self.ys.index(i) == self.ys.index(j):
                    continue
                elif self.ys[i] == self.ys[j]:
                    temp.append(1)
                else:
                    temp.append(0)
            self.adjacency_matrix.append(temp)



class Class_Directory(object) :
    """
    directory containing text files
    like so : 0.txt , 1.txt
    [class number].txt
    containing absolute paths of images belonging 
    to that class
    """
    CLASS_IMAGE_DIRECTORY = ""




