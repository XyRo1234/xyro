import pdfminer
from pdfminer.high_level import extract_text

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser



text = extract_text('D:\\Program Files\\Workspace\\00_Create\\Technical-Writing-101pdf.pdf')

with open('D:\\Program Files\\Workspace\\00_Create\\output.txt', mode='w', encoding='UTF-8') as output:
    output.write(text)