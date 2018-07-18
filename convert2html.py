#!/usr/bin/python
import sys
from pdfminertool.tools import pdf2txt as pdfcon
import glob
import os

list_of_files = glob.glob('/media/drew/Projects/library/readable/*.pdf') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print (latest_file)
