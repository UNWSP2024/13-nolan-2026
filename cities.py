import sqlite3

DB_NAME = "cities.db"


def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    while True:
        choice = menu()

        if choice == "1":
            display_sorted(cur, "ASC")
        elif choice == "2":
            display_sorted(cur, "DESC")
        elif choice == "3":
            display_sorted_by_name(cur)
        elif choice == "4":
            total_population(cur)
        elif choice == "5":
            average_population(cur)
        elif choice == "6":
            highest_population(cur)
        elif choice == "7":
            lowest_population(cur)
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()


# ---------------- MAIN MENU ----------------
def menu():
    print("\n--- City Database Menu ---")
    print("1. Display cities (population ascending)")
    print("2. Display cities (population descending)")
    print("3. Display cities (alphabetical)")
    print("4. Total population")
    print("5. Average population")
    print("6. Highest population city")
    print("7. Lowest population city")
    print("8. Exit")

    return input("Enter choice: ")


# ---------------- DISPLAY ----------------
def display_sorted(cur, order):
    direction = "ASC" if order == "ASC" else "DESC"

    cur.execute(f"SELECT * FROM Cities ORDER BY Population {direction}")
    rows = cur.fetchall()

    if not rows:
        print("\nNo cities found. Make sure the database is populated.")
        return

    print(f"\nCities sorted by population ({direction}):")
    print(f"{'ID':<5}{'City':20}{'Population'}")

    for r in rows:
        print(f"{r[0]:<5}{r[1]:20}{r[2]:,}")


def display_sorted_by_name(cur):
    cur.execute("SELECT * FROM Cities ORDER BY CityName ASC")
    rows = cur.fetchall()

    if not rows:
        print("\nNo cities found.")
        return

    print("\nCities sorted alphabetically:")
    print(f"{'ID':<5}{'City':20}{'Population'}")

    for r in rows:
        print(f"{r[0]:<5}{r[1]:20}{r[2]:,}")


# ---------------- STATS ----------------
def total_population(cur):
    cur.execute("SELECT SUM(Population) FROM Cities")
    total = cur.fetchone()[0]

    if total is None:
        print("\nNo data available.")
    else:
        print(f"\nTotal population: {total:,}")


def average_population(cur):
    cur.execute("SELECT AVG(Population) FROM Cities")
    avg = cur.fetchone()[0]

    if avg is None:
        print("\nNo data available.")
    else:
        print(f"\nAverage population: {avg:,.2f}")


def highest_population(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
    row = cur.fetchone()

    if row:
        print(f"\nHighest population: {row[0]} ({row[1]:,})")
    else:
        print("\nNo data available.")


def lowest_population(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
    row = cur.fetchone()

    if row:
        print(f"\nLowest population: {row[0]} ({row[1]:,})")
    else:
        print("\nNo data available.")


# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
