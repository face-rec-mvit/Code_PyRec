import Image

fp=open('/home/kiran/Documents/Facerec/8semproj/Code_PyRec/PCA/waste','r+')

for i in fp:
	j=i.strip('\n')
	temp=Image.open(j)
	print temp.size
