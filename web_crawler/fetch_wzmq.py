# -*- coding: utf-8 -*-

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def parse(path):
	fp = open(path, 'rb')
	parser = PDFParser(fp)
	doc = PDFDocument()
	parser.set_document(doc)
	doc.set_parser(parser)

	doc.initialize()

	if not doc.is_extractable:
		raise PDFTextExtractionNotAllowed
	else:
		rsrcmgr = PDFResourceManager()
		laparams = LAParams()
		device = PDFPageAggregator(rsrcmgr, laparams = laparams)

		interpreter = PDFPageInterpreter(rsrcmgr, device)

		num_page, num_image, num_curve, num_figure, num_TextBoxHorizontal = 0, 0, 0, 0, 0

		# doc.get_pages()
		# print(doc.get_pages())
		for page in doc.get_pages():
			num_page += 1
			print(page)

		print(num_page)

if __name__ == '__main__':
	parse('./files/wenzimengqiu.pdf')
