#!/usr/bin/python
from scihub import Scihub

sh = Scihub()

# retrieve 5 articles on Google Scholars related to 'crispr'
results = sh.search('crispr', 5)

# download the papers; will use sci-hub.io if it must
for paper in results['papers']:
	sh.download(paper['url'], path='database/pdfs')


