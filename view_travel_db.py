import sqlite3
from tabulate import tabulate

DB_NAME = "travel_users.db"

def view_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, email, username FROM travel_users")
    rows = cur.fetchall()
    conn.close()

    if rows:
        print(tabulate(rows, headers=["ID", "Email", "Username"], tablefmt="grid"))
    else:
        print("No users found.")

def view_bookings():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id,destination, guests, rooms, checkin, checkout FROM bookings")
    rows = cur.fetchall()
    conn.close()

    if rows:
        print(tabulate(rows, headers=["ID", "Destination", "Guests Number","No of Rooms","Check in Date","Check out Date"], tablefmt="grid"))
    else:
        print("No users found.")


def delete_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM travel_users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"✅ User with ID {user_id} deleted (if it existed).")

def delete_booking(user_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM bookings WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"✅ User with ID {user_id} deleted (if it existed).")


def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. View Users")
        print("2. View bookings")
        print("3. Delete User")
        print("4. Delete Booking")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_users()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                delete_user(user_id)
            except ValueError:
                print("❌ Invalid ID, must be a number.")
        elif choice == "4":
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                delete_booking(user_id)
            except ValueError:
                print("❌ Invalid ID, must be a number.")
        elif choice == "5":
            print("Exiting Admin Tool...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    admin_menu()
