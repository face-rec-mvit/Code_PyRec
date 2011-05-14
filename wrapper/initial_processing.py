#   <This python script just does the initial processing>
#    Copyright (C) <2010>  <Authors : Dharini,Guruprasad,Kunal,Kiran>
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


import numpy
import Image

def imageToVector(image):
    """
    This Function just takes in an image in a conformant format,
    and returns a vector which can be concatenated to make the
    VECTOR matrix.
    
    Input: PATH to the Image eg.Jpeg or Pgm files ..etc
    Output: A numpy 1 dimensional ndarray, the image gets
    automatically converted to grayscale. (Verify this)
    """
    #open the image as an PIL image.
    #print image
    im_binary = Image.open(image);
    #Check if image is 'RGB' convert it to grey scale for processing
    if(im_binary.mode=='RGB'):
	im_binary=im_binary.convert('L')	
    #Convert the PIL image to a numpy array.
    im_array = numpy.asarray(im_binary);
    #Convert the numpy array to a vector.
    im_vector = im_array.flatten();
    #return the vector to the calling function.
    return im_vector;

def returnImageArray(directoryOfImages):
    """
    This function assumes that the directory path
    passed has only images and no subdirectories.
    
    Input: Path to the Direcotry of Images.
    Output: a numpy array where each row has an image vector.
    """
    #The list which will finally hold all the image vectors
    #The list will be converted to a numpy array later.
    VECTOR_SET=[];
    directory = open(directoryOfImages);
    #image is the image file in the directory
    for image in directory:
        #get the flattened numpy array equivalent of the image
        vector = imageToVector(image);
        #append the flattened numpy array to the list
        VECTOR_SET.append(vector);
        
    #Convert the list to a numpy array and return.
    return(numpy.asarray(VECTOR_SET));
        
    
    
                        
    
