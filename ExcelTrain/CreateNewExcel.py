from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active         #讀取預設工作表
ws.title = 'modbus'

#新增橫排資料
ws.append(['port1', 'port2', 'port3', 'port4'])
ws.append([40002, 40003, 40004, 40005])
ws.append(['Main System Power(Low Word)', 'Main System Power(High Word)', 'Main Grid Power(Low Word)', 'Main Grid Power(High Word)'])

ws.move_range('A1:D3', rows=4, cols=3)
wb.save('newExcel.xlsx')