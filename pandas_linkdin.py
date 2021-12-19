import pandas as pd
import xlsxwriter
# create dataframe

data = {'col_A': [1, 2, 3], 'col_B':[1, 2, 3], 'col_C': [1, 2, 3], 'col_D':[1, 2, 3], 'col_E':[1, 2, 3]}

df = pd. DataFrame (data)

#initialise writer and export to excel sheet

writer = pd. ExcelWriter('Example.xlsx', engine='xlsxwriter')

df.to_excel (writer, sheet_name='Example Sheet', index=False)

#initialize formatting

workbook = writer.book

#re-open the worksheet

worksheet = writer.sheets [ 'Example Sheet']

# add the header format

header_format= workbook.add_format ()

header_format.set_center_across (True)

header_format.set_bold (True)

header_format.set_font ('Courier New')

#set the cell format

cell_format= workbook.add_format()

cell_format.set_font ('Courier New')

#give columns A - C a width of 15 and column D a width of 20

worksheet.set_column('A:C', 15, cell_format)

worksheet.set_column( 'D:D', 20, cell_format)

# for columns that aren't adjacent, for loops work best

for col in ['A', 'E']: worksheet.set_column (f' {col}: {col}', 5, cell_format)

#save changes

writer.save()