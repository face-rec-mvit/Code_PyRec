import numpy
import multiprocessing

def multiply(a,b):
    print type(a)
    print type(b)
    return a*b

def multiply_simple(a,b):
    """
    Returns the resultant matrix
    does 1 row , 1 col multiplication at a time .
    I think it sould work for arbitrary sized
    matrices without giving Memory error.

    Returns -1 on error
    """
    amat = numpy.matrix(a)
    bmat = numpy.matrix(b)

    if amat.shape[1] != bmat.shape[0]:
        return -1
    else:
        result = []
        temp_row = []
        bcols = bmat.swapaxes(0,1)
        for arow in amat:
            for brow in bcols:
                temp_row.append(multiprocessing.Process(target = multiply, args = (arow,brow.transpose())).start())
            result.append(temp_row)
        return result
        
def multiply_block(a,b):
    pass
def multiply_zmq_1machine(a,b):
    pass
def multiply_zmq_distributed(a,b):
    pass
