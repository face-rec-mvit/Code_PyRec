################ This is a basic DCT process for a single image.. ###############




import numpy
import Image


def imagetoDct(image):
    s=Image.open(image).convert("L")
	##s=Image.open('/home/adiyeaniramanujadaasan/Desktop/5.jpg' ).convert("L")
    pix = numpy.array(s.getdata()).reshape(s.size[0], s.size[1], 1) 
    a = pix.tolist()
    x, y, z = pix.shape 					

    ########### z is not used, but just bcoz shape returns 3 values, we have used this variable    
#    for i in range(x):
#        for j in range(y):
#            print(pix[i][j])
################ Precompute Alpha ####################
    import math
    alphaX = [0 for i in range(8)]
    for i in range(8):
	for j in range(8):
	    if (i==0 or j ==0):
                alphaX[i]=math.sqrt(1.0/x)
            else:
                alphaX[i]=math.sqrt(2.0/x)

    alphaY = [0 for i in range(8)]
    for i in range(8):
        for j in range(8):
            if (i==0 or j ==0):
                alphaY[i]=math.sqrt(1.0/y)
            else:
                alphaY[i]=math.sqrt(2.0/y)


################ Precompute product of the cosine terms ###########  commmon for all images #########
    product = [[0 for i in range(8)] for j in range(8)]
    sum = [[0 for i in range(8)] for j in range(8)]

    for h in range(8):
        for k in range(8):
            for i in range(x):
                for j in range(y):
                    product[h][k] = (math.cos(((2*i+1)*h*math.pi)/2*x)) * (math.cos(((2*j+1)*k*math.pi)/2*y))

#######################  compute sum for each image  ###################################

    for h in range(8):
        for k in range(8):
            for i in range(x):
                for j in range(y):
                    sum[h][k] = sum[h][k] + pix[i][j] * product[h][k]

################ Compute the final matrix ####################
    DCT = [[0 for i in range(8)] for j in range(8)]

    for h in range(8):
        for k in range(8):
            DCT[h][k] = alphaX[h]*alphaY[k] * sum[h][k]

###################### Print the DCT matrix  ###############################

    for h in range(8):
        for k in range(8):
            print DCT[h][k],
        print "\n"

#################### To traverse in this pattern 
# __  __  __
#  / / / / /
#  `` / / /
#    / / /
#   / / /
#   `` /
#     /
######################### in order to get the maximum "N" values in the top-left corner
    N=20
    i=1
    ListN = []
    #array = [[0 for i in range(8)] for j in range(8)]

    for n in range(8):
        if(n%2==0):
            i = n ; j=0
            while ( j <= n ):
                if (k > N):
                    break
                ListN.append(DCT[i][j])
#                array[i][j]=k
                k=k+1
#                print i, j
                i = i-1
                j = j+1
        else:
            i=0; j=n
            while ( i <= n ):
                if (k > N):
                    break
                ListN.append(DCT[i][j])
#                array[i][j]=k
                k=k+1
#                print i, j
                i= i+1
                j= j-1

    return ListN

################ now ListN will contain the prominent N values of DCT.. ##################


if __name__=='__main__':
	main_dct(sys.argv[1])
