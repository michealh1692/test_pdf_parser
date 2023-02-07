pip install boto3 -q
pip install botocore -q
pip install urllib3 -q
pip install PyPDF2 -q
pip install PyMuPDF -q
pip install wget -q

import json
import logging
import urllib3
from PyPDF2 import PdfReader
import pathlib
import shutil
import re
import fitz
import wget

log = logging.getLogger()
log.setLevel(logging.INFO)
url1 = "https://www.opportunitiesforyouth.org/wp-content/uploads/2021/04/Atomic_Habits_by_James_Clear-1.pdf"
file_path = "test.pdf"

urllib3.disable_warnings()
http = urllib3.PoolManager()

with http.request('GET', url1, preload_content=False, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}) as r, open(file_path, 'wb') as out_file:
  shutil.copyfileobj(r, out_file)
reader = PdfReader(file_path)
page = reader.pages[3]
print(page)
text = ''
for pages in page:
  text = page.extract_text()

#page = reader.getNumPages()
#number_of_pages = len(reader.pages)

#meta = reader.metadata

# All of the following could be None!
#print(len(reader.pages))
#print(meta.author)
#print(meta.creator)
#print(meta.producer)
#print(meta.subject)
#print(meta.title)

#ISBN_REGEX = r"978[0-9\-]+"
#ISBN_PATTERN = re.compile(ISBN_REGEX, re.UNICODE)
#text = re.sub(r"\s+", "", text, flags=re.UNICODE)
#print(text)
#matches = ISBN_PATTERN.findall(text)
#matches1 = str(matches)
#print(matches)
