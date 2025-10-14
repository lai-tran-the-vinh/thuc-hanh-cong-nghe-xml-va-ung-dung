import os
from lxml import etree
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Kết nối đến cơ sở dữ liệu thành công!")
    except Error as e:
        print(f"Lỗi '{e}' đã xảy ra")

    return connection

os.system('cls' if os.name == 'nt' else 'clear')
currentFileDirectory = os.path.dirname(os.path.abspath(__file__))
xmlFilename = os.path.join(currentFileDirectory, 'sanpham.xml')
xsdFilename = os.path.join(currentFileDirectory, 'sanpham.xsd')

try:
    # Parse file XSD
    xsdDocument = etree.parse(xsdFilename)
    xmlSchema = etree.XMLSchema(xsdDocument)

    # Parse file XML
    xmlDocument = etree.parse(xmlFilename)

    # Validate XML với XSD
    xmlSchema.assertValid(xmlDocument)
    print('Xác thực thành công!')

except etree.DocumentInvalid as err:
    print(f"Xác thực thất bại. Lỗi:\n{err}")

except IOError:
    print(f"Lỗi: Không thể đọc file. Hãy chắc chắn '{xmlFilename}' và '{xsdFilename}' tồn tại.")

except Exception as e:
    print(f"Đã có lỗi không mong muốn xảy ra: {e}")

# Kết nối MySQL
connection = create_connection("localhost", "root", "", "thuc-hanh-xml")

if connection and connection.is_connected():
    try:   
        cursor = connection.cursor()

        # Dùng XPath để lấy dữ liệu từ categories và products.
        categories = xmlDocument.xpath("//category")
        products = xmlDocument.xpath("//product")

        # Insert vào MySQL:
        # Bảng Categories:
        sqlInsertCategories = """
            INSERT INTO categories (id, name) VALUES (%s, %s) 
            ON DUPLICATE KEY UPDATE name = VALUES(name)
        """
        categoryValues = []
        for category in categories:
            id = category.get('id')
            name = category.text
            categoryValues.append((id, name))
        cursor.executemany(sqlInsertCategories, categoryValues)
        print('Chèn thành công')

        # Bảng products
        sqlInsertProduct = """
                INSERT INTO products (id, name, price, currency, stock, category_id) 
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                price = VALUES(price),
                currency = VALUES(currency),
                stock = VALUES(stock),
                category_id = VALUES(category_id)
                """
        productValues = []
        for product in products:
            id = product.get('id')
            name = product.find('name').text
            price = product.find('price').text
            currency = product.find('price').get('currency')
            stock = product.find('stock').text
            categoryRef = product.get('categoryRef')
            productValues.append((id, name, price, currency, stock, categoryRef))
                
        cursor.executemany(sqlInsertProduct, productValues)
        connection.commit()
    except Error as e:
        print(f"Lỗi cơ sở dữ liệu: {e}")
        connection.rollback()
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Đã đóng kết nối CSDL.")