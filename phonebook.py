# By Nolan Nelsen
# Written on 5/1/2026
# Phonebook Program

import sqlite3

# MAIN MENU

def display_menu():
    print("\nPhone Book Menu")
    print("1. Add a new entry")
    print("2. Look up a phone number")
    print("3. Update a phone number")
    print("4. Delete an entry")
    print("5. Display all entries")
    print("6. Exit")

def main():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        # CREATE
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            cur.execute("INSERT INTO Entries (Name, Phone) VALUES (?, ?)", (name, phone))
            conn.commit()
            print("Entry added.")

        # READ
        elif choice == "2":
            name = input("Enter name to look up: ")
            cur.execute("SELECT Phone FROM Entries WHERE Name = ?", (name,))
            result = cur.fetchone()
            if result:
                print(f"{name}'s phone number is {result[0]}")
            else:
                print("No entry found.")

        # UPDATE
        elif choice == "3":
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            cur.execute("UPDATE Entries SET Phone = ? WHERE Name = ?", (new_phone, name))
            conn.commit()
            if cur.rowcount > 0:
                print("Phone number updated.")
            else:
                print("No entry found.")

        # DELETE
        elif choice == "4":
            name = input("Enter name to delete: ")
            cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
            conn.commit()
            if cur.rowcount > 0:
                print("Entry deleted.")
            else:
                print("No entry found.")

        # DISPLAY ALL
        elif choice == "5":
            cur.execute("SELECT Name, Phone FROM Entries ORDER BY Name")
            rows = cur.fetchall()
            print("\nPhone Book Entries:")
            for name, phone in rows:
                print(f"{name}: {phone}")

        elif choice == "6":
            print("Bye.")
            break

        else:
            print("Invalid choice. Try again.")

    conn.close()

main()
