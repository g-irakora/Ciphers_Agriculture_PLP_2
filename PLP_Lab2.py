#!/usr/bin/python3
import mysql.connector

# Database connection configuration
my_conn = {
    "host": "1389893d11e1.7d5f7213.alu-cod.online",
    "port": 39708,
    "database": "SATS",
    "user": "Linda",
    "password": "1234"
}

# Database connection function
def connect_to_db():
    try:
        connection = mysql.connector.connect(**my_conn)
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
    return None

# Function to validate cooperative or individual choice
def validate_cooperative_or_individual():
    while True:
        print("Are you registering as a cooperative or an individual?")
        print("1. Cooperative")
        print("2. Individual")
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            if choice == 1:
                return "cooperative"
            elif choice == 2:
                return "individual"
            else:
                print("Invalid choice. Please enter 1 for Cooperative or 2 for Individual.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

# Create base class
class User:
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
