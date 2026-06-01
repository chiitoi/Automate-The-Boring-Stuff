#Chapter 17 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter17.html

import pypdf
import pdfminer.high_level

def pdf_word_count(pdf_filename):
    text = ''
    try:
        reader = pypdf.PdfReader(pdf_filename)
        for page in reader.pages:
            text += page.extract_text()
    except Exception:
        text = pdfminer.high_level.extract_text(pdf_filename)

    words = text.split()
    return len(words)

length = pdf_word_count('Recursion_Chapter1.pdf')
print(length)