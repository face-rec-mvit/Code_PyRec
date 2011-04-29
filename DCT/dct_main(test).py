import sys
import dct1
import get_abs_names


def dct_main(database):
	eigen_vect=[]
	images_path=get_abs_names.get_files(database)
	for i in images_path:
		eigen_vect.append(dct1.imagetoDct(i))
	print "Printing eigen vectors of all the images"
	print eigen_vect


if __name__ ==  '__main__':
	print sys.argv[1]
	database=sys.argv[1]
	dct_main(database)
