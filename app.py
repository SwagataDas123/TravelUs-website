from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import bcrypt

app = Flask(__name__)
CORS(app)  # allow frontend access

# ---- DB Setup ----
def init_db():
    conn = sqlite3.connect("travel_users.db")
    cur = conn.cursor()
     # Users table
    cur.execute("""CREATE TABLE IF NOT EXISTS travel_users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE,
                    username TEXT,
                    password TEXT
                )""")
    #Booking table
    cur.execute("""CREATE TABLE IF NOT EXISTS bookings(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    destination TEXT,
                    guests INTEGER,
                    rooms INTEGER,
                    checkin TEXT,
                    checkout TEXT
                )""")
    conn.commit()
    conn.close()

init_db()

# ---- ROUTES ----
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if not email or not username or not password:
        return jsonify({"error": "All fields required"}), 400

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        conn = sqlite3.connect("travel_users.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO travel_users (email, username, password) VALUES (?, ?, ?)",
                    (email, username, hashed_pw))
        conn.commit()
        conn.close()
        return jsonify({"message": "User registered successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already registered"}), 400


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = sqlite3.connect("travel_users.db")
    cur = conn.cursor()
    cur.execute("SELECT password FROM travel_users WHERE email = ?", (email,))
    row = cur.fetchone()
    conn.close()

    if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid email or password"}), 401


@app.route("/book", methods=["POST"])
def book():
    data = request.json if request.is_json else request.form

    #user_email = data.get("email")
    destination = data.get("destination")
    guests = data.get("guests")
    rooms = data.get("rooms")
    checkin = data.get("checkin")
    checkout = data.get("checkout")

    if not all([destination, guests, rooms, checkin, checkout]):
        return jsonify({"error": "All fields required"}), 400

    conn = sqlite3.connect("travel_users.db")
    cur = conn.cursor()
    cur.execute("""INSERT INTO bookings 
                   (destination, guests, rooms, checkin, checkout) 
                   VALUES ( ?, ?, ?, ?, ?)""",
                (destination, guests, rooms, checkin, checkout))
    conn.commit()
    conn.close()

    return jsonify({
        "message": "Booking confirmed!",
        "details": {
            #"email": user_email,
            "destination": destination,
            "guests": guests,
            "rooms": rooms,
            "checkin": checkin,
            "checkout": checkout
        }
    })



if __name__ == "__main__":
    app.run(debug=True)
