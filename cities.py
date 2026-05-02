import sqlite3

# MAIN MENU

def display_menu():
    print("\nCity Database Menu")
    print("1. Display cities sorted by population (ascending)")
    print("2. Display cities sorted by population (descending)")
    print("3. Display cities sorted by name")
    print("4. Display total population")
    print("5. Display average population")
    print("6. Display city with highest population")
    print("7. Display city with lowest population")
    print("8. Exit")

def main():
    # Connect to the existing database
    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC")
            rows = cur.fetchall()
            print("\nCities by Population (Ascending):")
            for city, pop in rows:
                print(f"{city}: {pop}")

        elif choice == "2":
            cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC")
            rows = cur.fetchall()
            print("\nCities by Population (Descending):")
            for city, pop in rows:
                print(f"{city}: {pop}")

        elif choice == "3":
            cur.execute("SELECT CityName, Population FROM Cities ORDER BY CityName ASC")
            rows = cur.fetchall()
            print("\nCities Sorted by Name:")
            for city, pop in rows:
                print(f"{city}: {pop}")

        elif choice == "4":
            cur.execute("SELECT SUM(Population) FROM Cities")
            total = cur.fetchone()[0]
            print(f"\nTotal Population: {total}")

        elif choice == "5":
            cur.execute("SELECT AVG(Population) FROM Cities")
            avg = cur.fetchone()[0]
            print(f"\nAverage Population: {avg}")

        elif choice == "6":
            cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
            city, pop = cur.fetchone()
            print(f"\nCity with Highest Population: {city} ({pop})")

        elif choice == "7":
            cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
            city, pop = cur.fetchone()
            print(f"\nCity with Lowest Population: {city} ({pop})")

        elif choice == "8":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

    conn.close()

if __name__ == "__main__":
    main()
