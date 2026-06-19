from flask import Flask, render_template
from database import init_db
from flask import request, jsonify
from database import get_db

app = Flask(__name__)

# Create database and tables
init_db()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/save_entry', methods=['POST'])
def save_entry():

    data = request.json

    conn = get_db()

    conn.execute("""
        INSERT INTO entries (
            entry_date,
            entry_type,
            category,
            amount,
            note
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        data.get('date'),
        data.get('type'),
        data.get('category'),
        data.get('amount'),
        data.get('note')
    ))

    conn.commit()
    conn.close()

    return jsonify({"success": True})