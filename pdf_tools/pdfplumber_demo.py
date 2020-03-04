
import pdfplumber

with pdfplumber.open("/home/ginger/case5.pdf") as pdf:
    first_page = pdf.pages[0]
    first_page.layout = None
    print(first_page.chars[0])