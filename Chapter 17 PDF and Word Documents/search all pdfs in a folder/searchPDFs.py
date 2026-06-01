#Chapter 17 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter17.html

import pypdf, os, pprint

def search_all_PDFs(text, folder='.', case_sensitive=False):
    matches = []

    for file in os.listdir(folder):
        if file.lower().endswith('.pdf'):
            reader = pypdf.PdfReader(file)
            for page_number, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if case_sensitive and text in page_text:
                    matches.append(f'In {file} on page {page_number}')
                elif not case_sensitive and text.lower() in page_text.lower():
                    matches.append(f'In {file} on page {page_number}')
    return matches

pprint.pprint(search_all_PDFs("Output", ".", False))