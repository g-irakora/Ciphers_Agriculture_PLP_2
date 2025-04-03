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
<<<<<<< HEAD
        return None

=======
    return None

<<<<<<< HEAD
=======
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

>>>>>>> 8bd69773160c9188b8c3d0066fb8939032e7b7a9
# Create base class
>>>>>>> 225217d8e1efaa5e8490d6905d3dfa0683ed0c8d
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
<<<<<<< HEAD
    def __init__(self, name, email, phone, password, location, sub_type):
        super().__init__(name, email, phone, password, location, "farmer", sub_type)
        self.crop_types = []
=======
<<<<<<< HEAD
    def __init__(self, name, email, phone, password, location, user_type):
        super().__init__(name, email, phone, password)
        self.location = location
        self.crop_types = []  # List to store multiple crop types
        self.user_type = user_type  # Cooperative or Individual
=======
    def __init__(self, name, email, phone, password, location):
        super().__init__(name, email, phone, password)
        self.location = location
        self.crop_types = []  # List to store multiple crop types
>>>>>>> 8bd69773160c9188b8c3d0066fb8939032e7b7a9
>>>>>>> 225217d8e1efaa5e8490d6905d3dfa0683ed0c8d

    def add_crops(self):
        print("Enter your crop types one by one. Type 'done' when finished:")
        while True:
            crop = input("Enter a crop type: ").strip()
            if crop.lower() == "done":
                break
<<<<<<< HEAD
            elif crop:
=======
            # Git push from LInda
            elif crop:  # Avoid empty input
>>>>>>> 225217d8e1efaa5e8490d6905d3dfa0683ed0c8d
                self.crop_types.append(crop)
        print(f"Crop types added: {', '.join(self.crop_types)}")

class Buyer(User):
<<<<<<< HEAD
    def __init__(self, name, email, phone, password, location, sub_type):
        super().__init__(name, email, phone, password, location, "buyer", sub_type)
=======
    def __init__(self, name, email, phone, password, location, user_type):
        super().__init__(name, email, phone, password)
        self.location = location
        self.user_type = user_type  # Cooperative or Individual
>>>>>>> 225217d8e1efaa5e8490d6905d3dfa0683ed0c8d

def validate_phone(phone):
    return re.fullmatch(r"\d{10}", phone)

def validate_password(password):
    return re.fullmatch(r"\d{5}", password)

def save_user_to_db(user):
    connection = connect_to_db()
    if not connection:
        return

<<<<<<< HEAD
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
=======
                if choice == 1:
                    self.subscription_type = "Basic"
                    self.cost = 15 if isinstance(self.user, Farmer) else 10
                    print(f"You have chosen the Basic subscription. The cost is {self.cost}$ per month.")
                    break
                elif choice == 2:
                    self.subscription_type = "Premium"
                    self.cost = 29.9 if isinstance(self.user, Farmer) else 20
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
        print(f"User Type: {self.user.user_type}")
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
>>>>>>> 225217d8e1efaa5e8490d6905d3dfa0683ed0c8d

        connection.commit()

<<<<<<< HEAD
def fetch_registered_users():
    connection = connect_to_db()
    if not connection:
        return []

    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT name, email, phone, location, user_type, sub_type FROM Users")
        users = cursor.fetchall()

    return users

class UserChoice:
=======
class User_Choice:
    def choose_user_type(self):
        while True:
            try:
                # Git Emmanuella 
                print("Are you a Farmer or a Buyer?")
                print("1. Farmer")
                print("2. Buyer")
                choice = int(input("Enter your choice (1 or 2): "))

                if choice == 1:
                    name = input("Enter your Name: ")
                    email = input("Enter your Email: ")
                    phone = input("Enter your Phone Number: ")
                    password = input("Enter your Password: ")
                    location = input("Enter your location: ")
                    user_type = input("Are you registering as a Cooperative or an Individual? ").strip().lower()
                    return Farmer(name, email, phone, password, location, user_type)
                elif choice == 2:
                    name = input("Enter your Name: ")
                    email = input("Enter your Email: ")
                    phone = input("Enter your Phone Number: ")
                    password = input("Enter your Password: ")
                    location = input("Enter your location: ")
                    user_type = input("Are you registering as a Cooperative or an Individual? ").strip().lower()
                    return Buyer(name, email, phone, password, location, user_type)
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

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
    print(f"User Type: {user.user_type}")
    if isinstance(user, Farmer):
        user.add_crops()  # Allow farmer to input multiple crop types
        print(f"Crop Types: {', '.join(user.crop_types)}")
        # Git Gasana

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
        # Git Premier

        action = input("Enter your choice (1, 2 or 3): ")
        if action == "1":
            print("\nOther Users on this App:")
            recipients = [u for u in registered_users if u != user]
            if not recipients:
                print("No other users available to communicate with.")
                continue
            for i, recipient in enumerate(recipients, start=1):
                print(f"{i}. {recipient.__class__.__name__} - Name: {recipient.name}, Location: {recipient.location}, User Type: {recipient.user_type}")

            try:
                recipient_choice = int(input("Enter the number of the recipient you want to communicate with: "))
                if 1 <= recipient_choice <= len(recipients):
                    recipient = recipients[recipient_choice - 1]
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

<<<<<<< HEAD
=======
class User_Choice:
>>>>>>> 225217d8e1efaa5e8490d6905d3dfa0683ed0c8d
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

<<<<<<< HEAD
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

=======
>>>>>>> 8bd69773160c9188b8c3d0066fb8939032e7b7a9
# Entry point
>>>>>>> 225217d8e1efaa5e8490d6905d3dfa0683ed0c8d
if __name__ == "__main__":
    main()
    # Git Arnold
