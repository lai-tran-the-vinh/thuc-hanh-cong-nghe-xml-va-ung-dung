from flask import Flask, request, jsonify
import json
from jsonschema import validate, ValidationError

app = Flask(__name__)

subtract_schema = {
    "type": "object",
    "properties": {
        "a": {"type": "number"},
        "b": {"type": "number"}
    },
    "required": ["a", "b"],
    "additionalProperties": False
}

@app.route('/')
def home():
    return "Xin chào từ Flask trên mọi địa chỉ IP!"

# Bài 9.1: GET /api/book
@app.route("/api/book", methods=["GET"])
def get_book():
    with open("data/course.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print(data)
    return jsonify(data), 200

# Bài 9.2: GET /api/user/<username>
@app.route("/api/user/<username>", methods=["GET"])
def get_user(username):
    with open("data/users.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    users = data.get("users", [])
    if len(users) > 0:
        for user in users:
            if user.get("username") == username:
                return jsonify(user), 200
    return jsonify({ "message": f"Không tìm thấy người dùng {username}" }), 200

# Bài 9.3: POST /api/subtrac
@app.route("/api/subtract", methods=["POST"])
def subtract():
    try:
        data = request.get_json()
        validate(instance=data, schema=subtract_schema)
        a = data.get("a")
        b = data.get("b")
        if a is None or b is None:
            return jsonify({"error": "Thiếu tham số 'a' hoặc 'b'"}), 400
        result = a - b
        return jsonify({"result": result}), 200
    except ValidationError as e:
        return jsonify({"error": f"Dữ liệu không hợp lệ: {e.message}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
