import PyPDF2

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with open('pdf.pdf', 'rb') as f:
	pdf_reader = PyPDF2.PdfFileReader(f)
	# print(pdf_reader.numPages)

	# page = pdf_reader.getPage(1)
	# print(page.extractText())
	
	# pdf_writer = PyPDF2.PdfFileWriter()
	# pdf_writer.encrypt('xxx')


	# for num_page in range(pdf_reader.numPages):
	# 	page = pdf_reader.getPage(num_page)
	# 	pdf_writer.addPage(page)

	# with open('pdf2.pdf', 'wb') as f2:
	# 	pdf_writer.write(f2)
