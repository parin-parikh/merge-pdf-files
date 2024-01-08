import PyPDF2, os

pdfiles = []
for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
                if filename != 'merged.pdf':
                        pdfiles.append(filename)
pdfiles.sort(key = str.lower)

merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')

