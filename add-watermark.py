import PyPDF2
import sys

input_file = PyPDF2.PdfFileReader(open('super_merge.pdf','rb'))
watermark_file= PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output_file = PyPDF2.PdfFileWriter()

for i in range(input_file.getNumPages()):
    page = input_file.getPage(i)
    page.mergePage(watermark_file.getPage(0))
    output_file.addPage(page)

with open('watermarked_output.pdf','wb') as opfile:
    output_file.write(opfile)