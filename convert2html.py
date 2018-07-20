#!/usr/bin/python
import sys
from pdfminertool.tools import pdf2txt as pdfcon
from pdfminertool.pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminertool.pdfminer.converter import TextConverter
from pdfminertool.pdfminer.layout import LAParams
from pdfminertool.pdfminer.pdfpage import PDFPage
from io import StringIO

import glob
import os

list_of_files = glob.glob('/media/drew/Projects/library/readable/*.pdf') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(latest_file, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text