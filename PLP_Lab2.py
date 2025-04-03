#!/usr/bin/python3
import mysql.connector
import re  # For validation

# Database connection function using a context manager
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="eee1b4c7fdfc.7c3476c2.alu-cod.online",
            port=36560,
            database="Hinga",
            user="abuyange",
            password="Pass@123"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

class User:
    def __init__(self, name, email, phone, password, location, user_type, sub_type):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.location = location
        self.user_type = user_type
        self.sub_type = sub_type

class Farmer(User):
    def __init__(self, name, email, phone, password, location, sub_type):
        super().__init__(name, email, phone, password, location, "farmer", sub_type)
        self.crop_types = []

    def add_crops(self):
        print("Enter your crop types one by one. Type 'done' when finished:")
        while True:
            crop = input("Enter a crop type: ").strip()
            if crop.lower() == "done":
                break
            elif crop:
                self.crop_types.append(crop)
        print(f"Crop types added: {', '.join(self.crop_types)}")

class Buyer(User):
    def __init__(self, name, email, phone, password, location, sub_type):
        super().__init__(name, email, phone, password, location, "buyer", sub_type)

def validate_phone(phone):
    return re.fullmatch(r"\d{10}", phone)

def validate_password(password):
    return re.fullmatch(r"\d{5}", password)

def save_user_to_db(user):
    connection = connect_to_db()
    if not connection:
        return

    with connection.cursor() as cursor:
        sql = """
        INSERT INTO Users (name, email, phone, password, location, user_type, sub_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (user.name, user.email, user.phone, user.password, user.location, user.user_type, user.sub_type))
        user_id = cursor.lastrowid  # Get the inserted user's ID

        if isinstance(user, Farmer):
            cursor.execute("INSERT INTO Farmers (id) VALUES (%s)", (user_id,))
            for crop in user.crop_types:
                cursor.execute("INSERT INTO Crops (farmer_id, crop_type) VALUES (%s, %s)", (user_id, crop))
        elif isinstance(user, Buyer):
            cursor.execute("INSERT INTO Buyers (id) VALUES (%s)", (user_id,))

        connection.commit()

def fetch_registered_users():
    connection = connect_to_db()
    if not connection:
        return []

    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT name, email, phone, location, user_type, sub_type FROM Users")
        users = cursor.fetchall()

    return users

class UserChoice:
    def choose_user_type(self):
        while True:
            try:
                print("Are you a Farmer or a Buyer?")
                print("1. Farmer")
                print("2. Buyer")
                choice = int(input("Enter your choice (1 or 2): "))

                name = input("Enter your Name: ")
                email = input("Enter your Email: ")

                while True:
                    phone = input("Enter your Phone Number: ")
                    if validate_phone(phone):
                        break
                    print("Invalid phone number! It must be exactly 10 digits.")

                while True:
                    password = input("Enter your Password (5 digits only): ")
                    if validate_password(password):
                        break
                    print("Invalid password! It must contain exactly 5 digits.")

                location = input("Enter your location: ")
                sub_type = input("Are you registering as a Cooperative or an Individual? ").strip().lower()

                if choice == 1:
                    farmer = Farmer(name, email, phone, password, location, sub_type)
                    farmer.add_crops()
                    return farmer
                elif choice == 2:
                    return Buyer(name, email, phone, password, location, sub_type)
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    print("Welcome to Smart Agricultural Trade System (SATS).")
    while True:
        print("\nMenu:")
        print("1. Register as a Farmer or Buyer")
        print("2. View Registered Users")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_choice = UserChoice()
            user = user_choice.choose_user_type()

            save_user_to_db(user)
            print("\nYour Profile Information:")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print(f"Phone: {user.phone}")
            print(f"Location: {user.location}")
            print(f"User Type: {user.user_type}")
            print(f"Sub Type: {user.sub_type}")

        elif choice == "2":
            registered_users = fetch_registered_users()
            if registered_users:
                print("\nPreviously Registered Users (excluding passwords):")
                for u in registered_users:
                    print(f"Name: {u['name']}, Email: {u['email']}, Phone: {u['phone']}, Location: {u['location']}, Type: {u['user_type']}, Sub Type: {u['sub_type']}")
            else:
                print("\nNo previous users found.")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
