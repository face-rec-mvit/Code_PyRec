#! /usr/bin/python

import numpy
import initial_processing
import get_abs_path_of_all_files_in_directory as lslR
import sys
import kNN
import operator #for itemgetter in sorted()
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
    image_size=0
    number_of_images=0
    ftypes = list()
    def __init__(self,image_directory,keys,types=None):
        self.IMAGE_DIRECTORY=image_directory
        self.keywords = keys
        self.ftypes = types
        self.create_xs_ys()
        print "XS and YS created"
        #place all the xs belonging to same ys together
        temp = zip(self.xs,self.ys)
        #print temp
        temp_new = sorted(temp,key=operator.itemgetter(1))
        #print temp_new
        #xs after sorting as per ys
        self.xs = [(xs) for xs,ys in temp_new]
        #in xs each row is an image
        self.ys = [(ys) for xs,ys in temp_new]
        self.k = len(numpy.unique(self.ys))
        self.model = kNN.train(self.xs,self.ys,numpy.unique(self.ys))
        print "KNN Model Created"
        self.adjacency_matrix = numpy.matrix(self.create_adjacency_matrix())
        print "Adjacency Matrix Calculated"
        self.weight_matrix = numpy.matrix(self.create_weight_matrix())
        print "Weight Matrix Calculated"
        #for significance of D & L please check the Algorithm 
        self.D = numpy.matrix(numpy.diag(numpy.sum(self.weight_matrix,axis=1)))
        #axis=1 row wise , axis=2 col wise
        print "Matrix D Calculated"
        self.L = self.D - self.weight_matrix 
        print "Matrix L Calculated"
        self.calculate_XtransposeLX()
        #calculate eigen values and eigen vectors
        self.eigenValues,self.eigenVectors = numpy.linalg.eig(self.B)
         
    def calculate_XtransposeLX(self):
        self.X = numpy.matrix(self.xs)
        #we will do X'LX
        #In-case the images are more than what can be stored in the RAM , use
        #memmap 
        self.image_size=len(self.xs[0])
        self.number_of_images=len(self.xs)
        print "Performing X'L"
        print "Creating Memmap"
        self.B_XtransposeL = \
        numpy.memmap(open("/tmp/memmap_B.temp","w+"),dtype='uint8',mode='w+',\
        shape = (self.image_size,self.number_of_images))
        print "Memmap Created"
        print "Calculating X'LX"
        self.B_XtransposeL = numpy.transpose(self.X) * self.L
        #write B to file and free memory
        del self.B_XtransposeL
        #print self.B.shape
        self.B_XtransposeL = \
        numpy.memmap(open("/tmp/memmap_B.temp","w+"),dtype='uint8',mode='w+',\
        shape = (self.image_size,self.number_of_images))
        #-------------------------------
        #print self.X.shape
        #print self.L.shape
        #print self.B_XtransposeL.shape
        #-------------------------------
        print "Performing X'L * X"
        self.B = \
        numpy.memmap(open("/tmp/memap_Bfinal.temp","w+"),dtype="uint8",mode='w+',\
        shape = (self.image_size,self.image_size))
        
        #print self.B.shape
        #del self.B

        for i in range(self.B_XtransposeL.shape[0]):
            print i
            #self.B = \
            #numpy.memmap(open("/tmp/memap_Bfinal.temp","w+"),dtype="uint8",mode='w+',\
            #shape = (77760,77760))
            temp = 0
            for j in range(self.X.shape[0]):
                temp += self.B_XtransposeL[i,j]*self.X[j,i]
            self.B[i,j]=temp
            #del self.B

        del self.B
        self.B = \
        numpy.memmap(open("/tmp/memap_Bfinal.temp","w+"),dtype="uint8",mode='w+',\
        shape =(self.image_size,self.image_size))

        print "X'LX Calculated"



    #def __del__(self):
    #    print "Deleting the memmap file"
    #    del self.B

    def create_xs_ys(self):
        files_list = lslR.get_files(self.IMAGE_DIRECTORY,self.ftypes)
        #print files_list
        for file in files_list:
            for item in self.keywords.iteritems():
                #the 1st entry is the class number 0,1,2,3...
                key = item[0]
                #the second entry is the reg-exp identifying the class 
                value = item[1]
                if file.rfind(value) != -1 :
                    #print key , file
                    self.xs.append(initial_processing.imageToVector(file))
                    self.ys.append(key)

    def create_weight_matrix(self):
        mat = list()
        for image in self.xs:
            #w,dist = kNN.calculate(self.model,image)
            dist = kNN.calculate(self.model,image)
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


