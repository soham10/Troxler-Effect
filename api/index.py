from flask import Flask, render_template, request, jsonify
from supabase import create_client
from datetime import datetime
import os

app = Flask(__name__)

# ── Supabase setup ───────────────────────────────────────
# Set these as Environment Variables in Vercel Dashboard:
#   SUPABASE_URL  → your project URL
#   SUPABASE_KEY  → your anon/public key
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")

def get_db():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

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
    db = get_db()
    db.table("results").insert({
        "name": name,
        "cross_size": cross_size,
        "spot_size": spot_size,
        "vanish_time": vanish_time,
        "timestamp": timestamp
    }).execute()
    return jsonify({"success": True})

@app.route("/api/results")
def get_results():
    db = get_db()
    response = db.table("results").select("*").order("id", desc=True).execute()
    return jsonify(response.data)

@app.route("/api/delete/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    db = get_db()
    db.table("results").delete().eq("id", record_id).execute()
    return jsonify({"success": True})

# For local development
if __name__ == "__main__":
    app.run(debug=True, port=5000)