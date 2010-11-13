import numpy 
import Image

def knn(centroids,new_image,cluster):
    """
    This function is the implementation of the
    K-Nearest Neighbour Algorithm.

    Input : 
    centroids : Numpy Ndarray of K Centroids,
    Its a numpy array where each index has another
    numpy array representing one of the centroids.
    
    new_image : It is a numpy array representing
    the new image that has to be added to the cluster.
    
    cluster   : Its a numpy array where each index is
    another numpy array containing all the images
    (numpy array representation) belonging to that cluster.
    
    NOTE: here we use the "distance" function which helps to
    calculate the distance, between two arrays.
    The distance can either be euclidean , mahalanobis 
    distance, etc.
    """
    a = numpy.ndarray([])
    for centroid in centroids:
        a.append(distance(centroid,new_image));
        #numpy ndarrays' argmin function returns the index
        #corresponding to the minimum 
        nearest_centroid=a.argmin()
    
    return centroid,cluster
