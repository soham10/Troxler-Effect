from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
DB_PATH = "troxler_results.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cross_size INTEGER NOT NULL,
                spot_size INTEGER NOT NULL,
                vanish_time REAL NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.json
    name = data.get("name", "").strip()
    cross_size = data.get("cross_size")
    spot_size = data.get("spot_size")
    vanish_time = data.get("vanish_time")
    if not name or cross_size is None or spot_size is None or vanish_time is None:
        return jsonify({"error": "Missing fields"}), 400
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO results (name, cross_size, spot_size, vanish_time, timestamp) VALUES (?,?,?,?,?)",
            (name, cross_size, spot_size, vanish_time, timestamp)
        )
        conn.commit()
    return jsonify({"success": True})

@app.route("/api/results")
def get_results():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM results ORDER BY id DESC").fetchall()
    return jsonify([dict(r) for r in rows])

@app.route("/api/delete/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM results WHERE id=?", (record_id,))
        conn.commit()
    return jsonify({"success": True})

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)