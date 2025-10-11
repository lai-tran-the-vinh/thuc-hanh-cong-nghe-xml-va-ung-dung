import os
from lxml import etree

os.system('cls' if os.name == 'nt' else 'clear')

currentDirectory = os.path.dirname(__file__)
xmlFilePath = os.path.join(currentDirectory, 'quanlybanan.xml')
xmlFile = etree.parse(xmlFilePath).getroot()

print('Lấy tất cả bàn')
allTables = xmlFile.xpath('//BAN')
for table in allTables:
    print(etree.tostring(table, pretty_print=True, encoding='unicode').strip())
print('\n')

print('Lấy tất cả nhân viên')
allEmployees = xmlFile.xpath('//NHANVIEN')
for employee in allEmployees:
    print(etree.tostring(employee, pretty_print=True, encoding='unicode').strip())
print('\n')

print('Lấy tất cả tên món')
allDishNames = xmlFile.xpath('//MON/TENMON/text()')
for dishName in allDishNames:
    print(dishName)
print('\n')

print('Lấy tên nhân viên có mã NV02')
employeeName = xmlFile.xpath('//NHANVIEN[MANV=\'NV02\']/TENV/text()')
if employeeName:
    print(employeeName[0])
print('\n')

print('Lấy tên và số điện thoại của nhân viên \'NV03\'')
employeeInfo = xmlFile.xpath('//NHANVIEN[MANV=\'NV03\']/TENV | //NHANVIEN[MANV=\'NV03\']/SDT')
for info in employeeInfo:
     print(etree.tostring(info, pretty_print=True, encoding='unicode').strip())
print('\n')

print('Lấy tên món có giá > 50,000')
expensiveDishes = xmlFile.xpath('//MON[GIA > 50000]/TENMON/text()')
for dishName in expensiveDishes:
    print(dishName)
print('\n')

print('Lấy số bàn của hóa đơn HD03')
tableNumber = xmlFile.xpath('//HOADON[SOHD=\'HD03\']/SOBAN/text()')
if tableNumber:
    print(tableNumber[0])
print('\n')

print('Lấy tên món có mã M02')
dishName = xmlFile.xpath('//MON[MAMON=\'M02\']/TENMON/text()')
if dishName:
    print(dishName[0])
print('\n')

print('Lấy ngày lập của hóa đơn HD03')
invoiceDate = xmlFile.xpath('//HOADON[SOHD=\'HD03\']/NGAYLAP/text()')
if invoiceDate:
    print(invoiceDate[0])
print('\n')

print('Lấy tất cả mã món trong hóa đơn HD01')
dishIdsInInvoice = xmlFile.xpath('//HOADON[SOHD=\'HD01\']/CTHDS/CTHD/MAMON/text()')
for dishId in dishIdsInInvoice:
    print(dishId)
print('\n')

print('Lấy tên món trong hóa đơn HD01')
dishNamesInInvoice = xmlFile.xpath('//MON[MAMON = //HOADON[SOHD=\'HD01\']/CTHDS/CTHD/MAMON]/TENMON/text()')
for dishName in dishNamesInInvoice:
    print(dishName)
print('\n')

print('Lấy tên nhân viên lập hóa đơn HD02')
employeeNameForInvoice = xmlFile.xpath('//NHANVIEN[MANV = //HOADON[SOHD=\'HD02\']/MANV]/TENV/text()')
if employeeNameForInvoice:
    print(employeeNameForInvoice[0])
print('\n')

print('Đếm số bàn')
tableCount = xmlFile.xpath('count(//BAN)')
print(f'Tổng số bàn: {int(tableCount)}')
print('\n')

print('Đếm số hóa đơn lập bởi NV01')
invoiceCountByEmployee = xmlFile.xpath('count(//HOADON[MANV=\'NV01\'])')
print(f'Số hóa đơn NV01 đã lập: {int(invoiceCountByEmployee)}')
print('\n')

print('Lấy tên tất cả món có trong hóa đơn của bàn số 2')
dishesOnTable2 = xmlFile.xpath('//MON[MAMON = //HOADON[SOBAN=\'2\']/CTHDS/CTHD/MAMON]/TENMON/text()')
for dishName in dishesOnTable2:
    print(dishName)
print('\n')

print('Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3')
employeesForTable3 = xmlFile.xpath('//NHANVIEN[MANV = //HOADON[SOBAN=\'3\']/MANV]')
for employee in employeesForTable3:
    print(etree.tostring(employee, pretty_print=True, encoding='unicode').strip())
print('\n')

print('Lấy tất cả hóa đơn mà nhân viên nữ lập')
invoicesByFemaleEmployees = xmlFile.xpath('//HOADON[MANV = //NHANVIEN[GIOITINH=\'Nữ\']/MANV]')
for invoice in invoicesByFemaleEmployees:
    print(etree.tostring(invoice, pretty_print=True, encoding='unicode').strip())
print('\n')

print('Lấy tất cả nhân viên từng phục vụ bàn số 1')
employeesForTable1 = xmlFile.xpath('//NHANVIEN[MANV = //HOADON[SOBAN=\'1\']/MANV]')
for employee in employeesForTable1:
    print(etree.tostring(employee, pretty_print=True, encoding='unicode').strip())
print('\n')

print('Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn')
dishesOrderedMoreThanOnce = xmlFile.xpath('//MON[MAMON = //CTHD[SOLUONG > 1]/MAMON]')
for dish in dishesOrderedMoreThanOnce:
    print(etree.tostring(dish, pretty_print=True, encoding='unicode').strip())
print('\n')

print('Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD=\'HD02\'')
tableAndDateForInvoice = xmlFile.xpath('//BAN[SOBAN = //HOADON[SOHD=\'HD02\']/SOBAN]/TENBAN/text() | //HOADON[SOHD=\'HD02\']/NGAYLAP/text()')
for item in tableAndDateForInvoice:
    print(item)
print('\n')