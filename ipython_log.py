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
