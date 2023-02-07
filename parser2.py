pip install PyMuPDF -q
pip install wget -q
pip install isbnlib -q

import fitz
import wget
import isbnlib

url1 = "https://www.africau.edu/images/default/sample.pdf"
sample_file = "sample.pdf"

filename = wget.download(url1)

#from isbnlib._core import get_isbnlike
#from isbntools import get_isbn_from_pdf
#from calibre_plugins.extract_isbn.pdf import get_isbn_from_pdf

doc = fitz.open("test.pdf")
#def get_isbn_from_pdf("test.pdf")

ISBN_REGEX = r"978[0-9\-]+"
ISBN_PATTERN = re.compile(ISBN_REGEX, re.UNICODE)
# Regex to check valid ISBN Code
regex = "^(?=(?:[^0-9]*[0-9]){10}(?:(?:[^0-9]*[0-9]){3})?$)[\\d-]+$"
# Compile the ReGex
p = re.compile(regex)
text = ""
for page in doc:
  text = page.get_text()
  #print(text)
  get_isbnlike(text, level='normal')
  #get_isb(text, level='normal')
  #print(get_isbnlike)
  #text = re.sub(r"\s+", "", text, flags=re.UNICODE)
  #matches = p.findall(text)
  #print(matches)
