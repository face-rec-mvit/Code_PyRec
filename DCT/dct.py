import numpy
import Image
s=Image.open("Example_5.jpg")                                   # Example_5.jpg is a Garyscale image
pix = numpy.array(s.getdata()).reshape(s.size[0], s.size[1], 1) # last argument 1 => grayscale, for a RGB last arg is 3
a = pix.tolist()
x, y, z = pix.shape 					# shape returns the diementions, for example for a gray scale it will return 1200, 2400, 1

########### z is not used, but just bcoz shape returns 3 values, we have used this variable
for i in range(x):
	for j in range(y):
		print(pix[i][j])
################ Precompute Alpha ####################
import math
alphaX = [0 for i in range(8)]
for i in range(8):
	if (i==0 or j ==0):
		alphaX[i]=math.sqrt(1.0/x)
	else:
		alphaX[i]=math.sqrt(2.0/x)

alphaY = [0 for i in range(8)]
for i in range(8):
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
N=10
i=1
ListN = []
for h in range(8):
	for k in range(h):
		if (N<i):
			break
		ListN.append(DCT[k][h-k])
		print DCT[k][h-k]
		i+=1


