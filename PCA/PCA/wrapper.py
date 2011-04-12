#< This script has the wrapper which decides on which algorithm to be chosen. >
#    Copyright (C) <2011>  <Authors : Dharini,Guruprasad, Kiran Tej, Kunal Ghosh>
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

import PCA_train_generic
import initial_processing as ip
import get_abs_names as lslR
import Image
import sys

####### decide_algo function depending on the input decides on the best algorithm to be chosen
##### Input : Given by the user which has the input directory names
### Depending on some metrics it actually decides on which algorith to be chosen


def decide_algo(input_str):
	print input_str
	wrapper_test_image_names = lslR.get_files(input_str)
	wrapper_test_image=Image.open(wrapper_test_image_names[0])
	wrapper_test_image.show()
	
	
	
	

if __name__=='__main__':
	arg=sys.argv
	decide_algo(sys.argv[1])
