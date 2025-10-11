import os
from lxml import etree
os.system('cls' if os.name == 'nt' else 'clear')

currentDirectory = os.path.dirname(__file__)
xmlFilePath = os.path.join(currentDirectory, 'sinhvien.xml')
xmlFile = etree.parse(xmlFilePath).getroot()

print('Lấy tất cả sinh viên:')
students = xmlFile.xpath('/school/student')
for student in students:
    studentElement = etree.tostring(student, pretty_print=True, encoding='unicode')
    print(studentElement)

print('Liệt kê tên tất cả sinh viên:')
student = xmlFile.xpath('/school/student/name/text()')
for name in student:
    print(name)
print('\n')

print('Lấy tất cả id của sinh viên:')
studentIds = xmlFile.xpath('/school/student/id/text()')
for id in studentIds:
    print(id)
print('\n')

print('Lấy ngày sinh của sinh viên có id = \'SV01\':')
dates = xmlFile.xpath('/school/student[id=\'SV01\']/date/text()')
print(dates[0])
print('\n')

print('Lấy các khóa học:')
courses = xmlFile.xpath('//course')
for course in courses:
    courseElement = etree.tostring(course, pretty_print=True, encoding='unicode')
    print(courseElement)

print('Lấy toàn bộ thông tin của sinh viên đầu tiên:')
students = xmlFile.xpath('/school/student[1]')
studentElement = etree.tostring(students[0], pretty_print=True, encoding='unicode')
print(studentElement)

print('Lấy mã sinh viên đăng ký khóa học \'Vatly203\':')
studentIds = xmlFile.xpath('//enrollment[course=\'Vatly203\']/studentRef')
for id in studentIds:
    idElement = etree.tostring(id, pretty_print=True, encoding='unicode')
    print(idElement)

print('Lấy tên sinh viên học môn \'Toan101\':')
studentNames = xmlFile.xpath('//student[id=//enrollment[course=\'Toan101\']/studentRef]/name')
for name in studentNames:
    nameElement = etree.tostring(name, pretty_print=True, encoding='unicode')
    print(nameElement)

print('Lấy tên sinh viên học môn \'Vatly203\':')
studentNames = xmlFile.xpath('//student[id=//enrollment[course=\'Vatly203\']/studentRef]/name')
for name in studentNames:
    nameElement = etree.tostring(name, pretty_print=True, encoding='unicode')
    print(nameElement)

print('Lấy ngày sinh của sinh viên có id=\'SV01\':')
date = xmlFile.xpath('//student[id=\'SV01\']/date/text()')
print(date[0])
print('\n')

print('Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997')
studentNames = xmlFile.xpath('//student[starts-with(date, \'1997\')]/name/text()')
for name in studentNames:
    print(name)
print('\n')

print('Lấy tên của các sinh viên có ngày sinh trước năm 1998:')
studentNames = xmlFile.xpath("//student[substring(date, 1, 4) < '1998']/name/text()")
for name in studentNames:
    print(name)
print('\n')

print('Đếm tổng số sinh viên:')
studentQuantity = xmlFile.xpath("count(//student)")
print(f"Tổng số sinh viên là: {int(studentQuantity)}")
print('\n')

print('Lấy tất cả sinh viên chưa đăng ký môn nào:')
unenrolledStudents = xmlFile.xpath("//student[not(id=//enrollment/studentRef)]")
if unenrolledStudents:
    for student in unenrolledStudents:
        studentElement = etree.tostring(student, pretty_print=True, encoding='unicode')
        print(studentElement)
else:
    print("Tất cả sinh viên đều đã đăng ký ít nhất một môn học.")
print('\n')

print('Lấy phần tử <date> anh em ngay sau <name> của SV01:')
dates = xmlFile.xpath("//student[id='SV01']/name/following-sibling::date")
if dates:
    print(etree.tostring(dates[0], pretty_print=True, encoding='unicode'))
print('\n')

print('Lấy phần tử <id> anh em ngay trước <name> của SV02:')
ids = xmlFile.xpath("//student[id='SV02']/name/preceding-sibling::id")
if ids:
    print(etree.tostring(ids[0], pretty_print=True, encoding='unicode'))
print('\n')

print("Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03':")
courses = xmlFile.xpath("//enrollment[studentRef='SV03']/course")
if courses:
    print(etree.tostring(courses[0], pretty_print=True, encoding='unicode'))
print('\n')

print('Lấy sinh viên có họ là “Trần”:')
students = xmlFile.xpath("//student[starts-with(name, 'Trần ')]")
if students:
    for student in students:
        studentElement = etree.tostring(student, pretty_print=True, encoding='unicode')
        print(studentElement)
else:
    print("Không tìm thấy sinh viên nào có họ Trần.")
print('\n')

print('Lấy năm sinh của sinh viên SV01:')
birthYear = xmlFile.xpath("substring(//student[id='SV01']/date, 1, 4)")
print(f"Năm sinh: {birthYear}")
print('\n')
