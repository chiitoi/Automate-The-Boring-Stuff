#Chapter 14 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter14.html

import os, openpyxl
import pprint

def find_in_excel(search_text):
    search_text = search_text.lower()
    results = {}
    no_matches = []

    excel_files = os.listdir()

    for file in excel_files:
        if not file.endswith('.xlsx'):
            continue

        wb = openpyxl.load_workbook(file, data_only=True)

        file_results = []

        for sheet in wb.worksheets:
            sheet_results = []

            for row in sheet.iter_rows():
                for cell in row:
                    if isinstance(cell.value, str):
                        cell_value = cell.value.lower()

                        if search_text in cell_value:   
                            sheet_results.append(cell.coordinate)

                            print(f'{file} | {sheet.title} | {cell.coordinate} : {cell.value}')
            if sheet_results:
                file_results.append({
                    "sheet": sheet.title,
                    "cells": sheet_results
                })
                """
                results.setdefault(file, [])
                results[file].append({
                    "sheet": sheet.title,
                    "cells": sheet_results
                })
                """
        if file_results:
            results[file] = file_results
        else:
            no_matches.append(file)
        wb.close()
    
    print()
    if results:
        pprint.pprint(results, sort_dicts=False)
    else:
        print(f'No results found for "{search_text}" in the following files:')
        for file in no_matches:
            print(f'    {file}')
    
    return results

word = 'avo'
find_in_excel(word)