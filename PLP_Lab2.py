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

# Create subclasses
class Farmer(User):
    def __init__(self, name, email, phone, password, location):
        super().__init__(name, email, phone, password)
        self.location = location
        self.crop_types = []  # List to store multiple crop types

    # Add method to input multiple crop types
    def add_crops(self):
        print("Enter your crop types one by one. Type 'done' when finished:")
        while True:
            crop = input("Enter a crop type: ").strip()
            if crop.lower() == "done":
                break
            elif crop:  # Avoid empty input
                self.crop_types.append(crop)
        print(f"Crop types added: {', '.join(self.crop_types)}")

class Buyer(User):
    def __init__(self, name, email, phone, password, location, cooperative, individual):
        super().__init__(name, email, phone, password)
        self.location = location
        self.cooperative = cooperative
        self.individual = individual

class Subscription:
    def __init__(self, user):
        self.user = user
        self.subscription_type = None
        self.cost = 0
        self.publish_permission = False  # Default is no permission to publish

    def choose_subscription_type(self):
        while True:
            try:
                if isinstance(self.user, Farmer):
                    print(f"Hello {self.user.name}, please choose your subscription type:")
                    print("1. Basic subscription (15$ per month)")
                    print("2. Premium subscription (29.9$ per month)")
                elif isinstance(self.user, Buyer):
                    print(f"Hello {self.user.name}, please choose your subscription type:")
                    print("1. Basic subscription (10$ per month)")
                    print("2. Premium subscription (20$ per month)")

                choice = int(input("Enter your choice (1 or 2): "))

                if choice == 1:
                    if isinstance(self.user, Farmer):
                        self.subscription_type = "Basic"
                        self.cost = 15
                    elif isinstance(self.user, Buyer):
                        self.subscription_type = "Basic"
                        self.cost = 10
                    print(f"You have chosen the Basic subscription. The cost is {self.cost}$ per month.")
                    break
                elif choice == 2:
                    if isinstance(self.user, Farmer):
                        self.subscription_type = "Premium"
                        self.cost = 29.9
                    elif isinstance(self.user, Buyer):
                        self.subscription_type = "Premium"
                        self.cost = 20
                    self.publish_permission = True  # Premium users can publish
                    print(f"You have chosen the Premium subscription. The cost is {self.cost}$ per month.")
                    print("As a Premium user, you are allowed to publish on the platform.")
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_subscription_details(self):
        print(f"\nSubscription Details:")
        print(f"User: {self.user.name}")
        print(f"Subscription Type: {self.subscription_type}")
        print(f"Cost: {self.cost}$ per month")
        if self.publish_permission:
            print("You are allowed to publish on the platform.")        
