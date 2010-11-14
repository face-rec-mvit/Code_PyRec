#   <Log>
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

#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'ipython_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------

_ip.magic("cd ../CroppedYale/yaleB01/")
import Import
import Image
import numpy
a = Image.open("yaleB01_P00A+000E+00.pgm")
b = Image.open("yaleB01_P00A+000E+20.pgm")
arra = numpy.asarray(a)
arrb = numpy.asarray(b)
flata = arra.flatten()
flatb = arrb.flatten()
V=[]
V.append(flata)
V.append(flatb)
final = numpy.asarray(V)
