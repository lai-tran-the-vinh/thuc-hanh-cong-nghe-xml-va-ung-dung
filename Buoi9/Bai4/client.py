import requests
from jsonschema import validate, ValidationError

BASE_URL = "http://127.0.0.1:5000"

# ---------------------- SCHEMA ----------------------
book_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "course",
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "minLength": 0,
            "maxLength": 100
        },
        "author": {
            "type": "string",
            "minLength": 1
        },
        "price": {
            "type": "number",
            "minimum": 0
        },
        "inStock": {
            "type": "boolean"
        },
        "categories": {
            "type": "array",
            "items": {
                "type": "string",
                "minLength": 2
            },
            "minItem": 0
        },
        "rating": {
            "type": "number",
            "minimum": 0,
            "maximum": 5
        }
    },
    "required": [
        "title",
        "author",
        "price",
        "inStock",
        "categories"
    ]
}

user_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "users",
    "type": "object",
    "properties": {
        "users": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string",
                        "minLength": 3,
                        "maxLength": 15,
                        "pattern": "(^[a-zA-Z0-9]+$)"
                    },
                    "password": {
                        "type": "string",
                        "minLength": 8,
                        "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[^A-Za-z0-9]).+$"
                    },
                    "emails": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "format": "email"
                        }
                    },
                    "age": {
                        "type": "number",
                        "minimum": 13,
                        "maximum": 100
                    },
                    "address": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                                "minLength": 1
                            },
                            "street": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "city"
                        ]
                    },
                    "hobbies": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "minLength": 2
                        }
                    },
                    "isVerified": {
                        "type": "boolean",
                        "default": "false"
                    }
                },
                "required": [
                    "username",
                    "password",
                    "emails",
                    "age",
                    "address"
                ]
            }
        }
    }
}

subtract_schema = {
    "type": "object",
    "properties": {
        "result": {"type": "number"}
    },
    "required": ["result"]
}

# ---------------------- API FUNCTIONS ----------------------
def get_book():
    url = f"{BASE_URL}/api/book"
    response = requests.get(url)
    data = response.json()
    print("\nDữ liệu /api/book:")
    print(data)

    try:
        validate(instance=data, schema=book_schema)
        print("Dữ liệu hợp lệ với schema!")
    except ValidationError as e:
        print(f"Lỗi schema: {e.message}")

def get_user():
    username = input("Nhập username: ")
    url = f"{BASE_URL}/api/user/{username}"
    response = requests.get(url)
    data = response.json()
    print("\nDữ liệu /api/user:")
    print(data)

    try:
        validate(instance=data, schema=user_schema)
        print("Dữ liệu hợp lệ với schema!")
    except ValidationError as e:
        print(f"Lỗi schema: {e.message}")

def post_subtract():
    try:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
        return

    payload = {"a": a, "b": b}
    url = f"{BASE_URL}/api/subtract"
    response = requests.post(url, json=payload)
    data = response.json()

    print("\nDữ liệu /api/subtract:")
    print(data)

    try:
        validate(instance=data, schema=subtract_schema)
        print("Dữ liệu hợp lệ với schema!")
    except ValidationError as e:
        print(f"Lỗi schema: {e.message}")

# ---------------------- MAIN MENU ----------------------
def main():
    while True:
        print("\n===== MENU CLIENT =====")
        print("1. Gọi API /api/book")
        print("2. Gọi API /api/user/<username>")
        print("3. Gọi API /api/subtract (POST)")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            get_book()
        elif choice == "2":
            get_user()
        elif choice == "3":
            post_subtract()
        elif choice == "0":
            print("Tạm biệt")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
