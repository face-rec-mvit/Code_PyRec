#clean the build directory
rubber --clean  *.tex

#make the tex files into pdf directly
rubber  main.tex
#rubber  certificate.tex
#rubber  acknowledgement.tex

#clean the temporary files
rubber --clean *.tex
