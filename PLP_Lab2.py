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

            class Chat_Box:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, message):
        self.messages.append(f"{sender} to {recipient}: {message}")
        print(f"{sender} to {recipient}: {message}")

    def view_messages(self):
        print("\nChat Messages:")
        if not self.messages:
            print("No messages yet.")
        else:
            for message in self.messages:
                print(message)

# Global list to store all registered users
registered_users = []

def main():
    chat_box = Chat_Box()

    print("Welcome to Smart Agricultural Trade System (SATS).")
    user_choice = User_Choice()
    user = user_choice.choose_user_type()
    registered_users.append(user)

    # Display user details
    print("\nYour Profile Information:")
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print(f"Phone: {user.phone}")
    print(f"Location: {user.location if hasattr(user, 'location') else 'N/A'}")
    if isinstance(user, Farmer):
        user.add_crops()  # Allow farmer to input multiple crop types
        print(f"Crop Types: {', '.join(user.crop_types)}")
    elif isinstance(user, Buyer):
        print(f"Cooperative: {user.cooperative}")
        print(f"Individual Buyer: {user.individual}")

    # Step 2: Subscription
    subscription = Subscription(user)
    subscription.choose_subscription_type()
    subscription.display_subscription_details()

    # Step 3: Chat functionality
    while True:
        print("\nWhat would you like to do?")
        print("1. Send a message")
        print("2. View messages in chat box")
        print("3. Exit")

        action = input("Enter your choice (1, 2 or 3): ")
        if action == "1":
            print("\nOther Users on this App:")
            recipients = [u for u in registered_users if u != user]
            if not recipients:
                print("No other users available to communicate with.")
                continue
            for i, recipient in enumerate(recipients, start=1):
                if isinstance(recipient, Farmer):
                    print(f"{i}. Farmer - Name: {recipient.name}, Crop Types: {', '.join(recipient.crop_types)}, Location: {recipient.location}")
                elif isinstance(recipient, Buyer):
                    print(f"{i}. Buyer - Name: {recipient.name}, Location: {recipient.location}, Cooperative Buyer: {recipient.cooperative}, Individual Buyer: {recipient.individual}")

            try:
                recipient_choice = int(input("Enter the number of the recipient you want to communicate with: "))
                if 1 <= recipient_choice <= len(recipients):
                    recipient = recipients[recipient_choice - 1]

                    print("\nRecipient Information:")
                    if isinstance(recipient, Farmer):
                        print(f"Name: {recipient.name}")
                        print(f"Location: {recipient.location}")
                        print(f"Crop Types: {', '.join(recipient.crop_types)}")
                    elif isinstance(recipient, Buyer):
                        print(f"Name: {recipient.name}")
                        print(f"Location: {recipient.location}")
                        print(f"Cooperative: {recipient.cooperative}")
                        print(f"Individual: {recipient.individual}")

                    message = input("Enter your message: ")
                    chat_box.send_message(user.name, recipient.name, message)
                else:
                    print("Invalid choice. Please select a valid recipient number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif action == "2":
            chat_box.view_messages()
        elif action == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
