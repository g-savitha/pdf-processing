import PyPDF2
import sys

inputs = sys.argv[1:] #grab all the args, beside 1st one coz 1st one is python

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super_merge.pdf')
pdf_combiner(inputs)