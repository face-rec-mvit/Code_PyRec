import PCA_train as pt
import sys
import get_abs_names as lslR
import initial_processing as ip

def fun(src_img_dir):
	image_vector=[]
	images=lslR.get_files(src_img_dir)
	for i in range(len(images)):
		image_vector.append(ip.imageToVector(images[i]))
	print image_vector

if __name__=='__main__':
	src_dir=sys.argv[1]
	fun(src_dir)
	
