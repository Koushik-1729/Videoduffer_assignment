from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
DATABASE = 'database.db'
def start_database():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id iINTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                user_id INTEGER NOT NULL
            )
        """)

@app.route('/adduser', methods=['POST'])
def add_user():
    try:
        data = request.json
        name = data.get('name')
        user_id = data.get('id')
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, user_id) VALUES (?, ?)", (name, user_id))
            conn.commit()
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM users WHERE user_id > 5")
            result = cursor.fetchall()
            names_above_5 = [row[0] for row in result]
        return jsonify({"names_with_ids_above_5": names_above_5}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
if __name__ == '__main__':
    start_database()
    app.run(debug=True)
