#clean the build directory
rubber --clean -d *.tex

#make the tex files into pdf directly
rubber -d frontpage.tex
rubber -d certificate.tex
rubber -d acknowledgement.tex

#clean the temporary files
rubber --clean *.tex`
