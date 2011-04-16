#! /usr/bin/python

#from __future__ import division #for the final success rate calculation
import numpy
from scipy import spatial
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
    def \
    __init__(self,image_directory,classKeys,ftype=None,include=None,exclude=None,numOfEigVectors=50):
        self.IMAGE_DIRECTORY=image_directory
        self.keywords = classKeys
        self.ftypes = ftype
        self.include = include
        self.exclude = exclude
        self.create_xs_ys()
        print "XS and YS created"
        
        #place all the xs belonging to same ys together
        temp = zip(self.xs,self.ys)
        #print temp
        self.xs_ys_zip = sorted(temp,key=operator.itemgetter(1))
        #print temp_new
        #xs after sorting as per ys
        self.xs = [(xs) for xs,ys in self.xs_ys_zip]
        #in xs each row is an image
        self.ys = [(ys) for xs,ys in self.xs_ys_zip]
        self.k = len(numpy.unique(self.ys))
        self.model = kNN.train(self.xs,self.ys,numpy.unique(self.ys))
        print "KNN Model Created"
        
        self.adjacency_matrix = numpy.matrix(self.create_adjacency_matrix())
        #the adjacency matrix takes up a lot of ram so , keeping it on disk

        self.adj_temp = \
        numpy.memmap(open("/tmp/memmap_adj.temp","w+"),dtype='uint8',mode='w+',\
        shape = (self.adjacency_matrix.shape[0],self.adjacency_matrix.shape[1]))
        #del saves the matrix to disk
        del self.adj_temp

        #open the matrix again
        self.adjacency_matrix = \
        numpy.memmap(open("/tmp/memmap_adj.temp","w+"),dtype='uint8',mode='w+',\
        shape = (self.adjacency_matrix.shape[0],self.adjacency_matrix.shape[1]))
        print "Adjacency Matrix Calculated"
        
        
        self.weight_matrix = numpy.matrix(self.create_weight_matrix())
        self.weight_temp = \
        numpy.memmap(open("/tmp/memmap_weight.temp","w+"),dtype='uint8',mode='w+',\
        shape = (self.weight_matrix.shape[0],self.weight_matrix.shape[1]))
        #del saves the matrix to disk
        del self.weight_temp

        #open the matrix to disk
        self.weight_temp = \
        numpy.memmap(open("/tmp/memmap_weight.temp","w+"),dtype='uint8',mode='w+',\
        shape = (self.weight_matrix.shape[0],self.weight_matrix.shape[1]))
        print "Weight Matrix Calculated"
        
        #for significance of D & L please check the Algorithm 
        self.D = numpy.matrix(numpy.diag(numpy.sum(self.weight_matrix,axis=1)))
        #axis=1 row wise , axis=2 col wise
        print "Matrix D Calculated"
        
        self.L = self.D - self.weight_matrix 
        print "Matrix L Calculated"
        
        self.calculate_XtransposeLX()
        #calculate eigen values and eigen vectors
        print "Calculating Eigen Vectors and Values"
        self.eigenValues,self.eigenVectors = numpy.linalg.eig(self.B)
        print "Eigen Values and Vectors Calculated"
        self.eigSorted = \
        sorted(zip(self.eigenValues,self.eigenVectors),key=operator.itemgetter(0))
        #print len(self.temp)
        #select the first d eigenVectors
        self.d = numOfEigVectors
        self.A = numpy.matrix([vec for (val,vec) in \
                self.eigSorted][:self.d])
        #print self.A.shape
        self.y = []
        self.calculateYis()
        #the Ys must be transposed so that each row belongs to 1 image
        #and can be referenced as y[0] to be the first image
        #we then zip the y with ys to know which image belongs to which class
        self.y = [tuple(i) for i in self.y.tolist()]
        self.yZipYs = dict(zip(self.y,self.ys))
        #print self.yZipYs
        print "Created a zip of Y and ys"
        #self.test()
        print """
        Call the test() method like ImageDir , with
        directory to test images as the first arg and the dictionary 
        of {regexp:class} as the second argument, NOTE : the file 
        types are assumed to be the same as that of training images
        """

    def test(self,image_directory,classKeys,include=None,exclude=None):
        #the following reassignment is done to keep the __init__
        #method and the test method arguments consistent
        test_path = image_directory
        test_classes = classKeys
        includ = include
        exclud = exclude

        print "Starting to Test"
        #test_path = raw_input("Enter the Path containing test images:")
        #test_pattern = list(raw_input("Enter the regexp identifying \
        #test images in the directory above:"))
        test_files = \
        lslR.get_files(directory=test_path,ftype=self.ftypes,include=includ,exclude=exclud)

        num = len(test_files)
        i = 0
        success = 0
        failure = 0
        for fil in test_files:
            #if num - i > 0 :
            #    print "processing Image number: (%d) , Corresponding to File name: %s " % (i,fil)
            xTest = \
            numpy.matrix(initial_processing.imageToVector(fil))
            xTest_class = -1
            #----------------debug code------------
            #print type(xTest)
            #--------------------------------------
            #project testing image on A
            #yTest = numpy.transpose(self.A * xTest.transpose())
            yTest = xTest * self.A.transpose()
            #find the distance of yTest from each Yi
            distAndYPair = [] #inf denotes infinity
            #self.y_Transpose = numpy.transpose(self.y)
            #for y in self.y_Transpose:
            for y in self.y:
                #print type(yTest),type(y),yTest.shape,y.shape
                dist = spatial.distance.euclidean(yTest,y)
                #if dist < minPair[0]:
                #    print "iterating to find the minimum match"
                #    print "y :",y
                #    print "yTest :",yTest
                #    minPair[0] = dist
                #    minPair[1] = tuple(y)
                distAndYPair.append([dist,y])
            #print "type of minPair[1]"+str(type(minPair[1]))
            #print minPair[1] in self.y_Transpose
            distAndYPair.sort()
            #print minPair[1] in numpy.transpose(self.y)
            #print type(self.y[0])
            #print "Minimum distance: ",minPair[0]

            recognized_class = self.yZipYs[distAndYPair[0][1]]
            #because the class number starts from 0 and the numbering of 
            #of 
            for key in test_classes.keys():
                if fil.find(key) != -1:
                    xTest_class = test_classes[key]
                    break
            if recognized_class == xTest_class :
                success += 1
            else:
                failure += 1
            #print "Success %d , Failure %d" % (success,failure) 
            #print "Recognized Class: %d And xTest_Class: %d " % \
            #(recognized_class,xTest_class) 
            
            i +=1
        rate = (float(success)/float(success+failure))
        #print "Success Rate is : %f" % rate
        return rate

    def calculateYis(self):
        print "Calculating Yi for all Xi"
        #self.xtemp = numpy.matrix(self.xs).transpose()
        ##print self.xtemp.shape
        #self.y = self.A * self.xtemp
        self.y = numpy.matrix(self.xs)*self.A.transpose()
        print "Calcuated Yi s"

    def calculate_XtransposeLX(self):
        self.X = numpy.matrix(self.xs)
        #we will do X'LX
        #In-case the images are more than what can be stored in the RAM , use
        #memmap 
        self.image_size=len(self.xs[0])
        self.number_of_images=len(self.xs)
        print "Performing X'L"
        print "Creating Memmap"
        #-------------------
        print self.image_size
        print self.number_of_images
        #-------------------
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
            #print i
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
        self.files_list = \
        lslR.get_files(directory=self.IMAGE_DIRECTORY,include=self.include,\
                exclude = self.exclude,ftype=self.ftypes)
        #print files_list
        for file in self.files_list:
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
        print "Creating Adjacency Matrix"
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
        print "Adjacency Matrix Created"
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


