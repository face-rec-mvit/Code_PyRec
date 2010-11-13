import numpy
import IMage

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
    im_binary = Image.open(image);
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
        
    
    
                        
    