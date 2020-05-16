import win32com.client
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1,1).Value = "Hello World"

# Save
wb.SaveAs('path')
excel.Quit()

# Read
wb = excel.Workbooks.Open('path')
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)
excel.Quit()

# Cell color change
wb = excel.Workbooks.Open('path')
ws = wb.ActiveSheet
ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10
ws.Range("A2:C2").Interior.ColorIndex = 27