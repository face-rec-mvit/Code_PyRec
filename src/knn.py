#   <Script to implement the knn algorithms>
#    Copyright (C) <2010>  <Authors : Dharini,Hariharan,Guruprasad,Kunal,Kiran>
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
