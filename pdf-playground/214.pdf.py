from os import read
import PyPDF2

#rb for read binary
with open('/Users/p.petryszen/Documents/VsCode/complete_python_developer_2020_zero_to_mastery/pdf-playground/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90) #until now everything happens in the memory
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
