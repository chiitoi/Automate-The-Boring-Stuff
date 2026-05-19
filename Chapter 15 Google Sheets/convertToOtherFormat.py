#Chapter 15 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter15.html

import ezsheets
ss = ezsheets.upload('myProduce.xlsx')

new_ss = ezsheets.Spreadsheet(ss.id)

#new_ss.downloadAsExcel()  

#new_ss.downloadAsODS()

new_ss.downloadAsCSV()

#new_ss.downloadAsTSV()

#new_ss.downloadAsPDF()

#new_ss.downloadAsHTML()