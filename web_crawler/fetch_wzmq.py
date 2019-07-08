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

		num_page, num_image, num_curve, num_figure, num_textboxhorizontal = 0, 0, 0, 0, 0

		for page in doc.get_pages():
			num_page += 1
			interpreter.process_page(page)
			print(interpreter)

			layout = device.get_result()
			for x in layout:
				if isinstance(x, LTImage):
					num_image += 1
				elif isinstance(x, LTCurve):
					num_curve += 1
				elif isinstance(x, LTFigure):
					num_figure += 1
				elif isinstance(x, LTTextBoxHorizontal):
					num_textboxhorizontal += 1

					with open('test.txt', 'a') as f:
						results = x.get_text()
						f.write(results + '\n')

		print('Object num: \n', 'Page num: %s\n' % num_page, 'Image num: %s\n' % num_image, 'Curve num: %s\n' % num_curve, 'Horizontal text: %s\n' % num_textboxhorizontal)

if __name__ == '__main__':
	parse('./files/wenzimengqiu.pdf')
