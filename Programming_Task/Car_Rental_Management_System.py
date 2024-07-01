class Cars:
    # Class variable to store rental records
    rent_record = {}

    def __init__(self):
        # Instance variable to store initial car inventory
        self.car_dict = {
            1: {"Name": "Toyota Corolla", "Availability": "Available"},
            2: {"Name": "Ford Mustang", "Availability": "Available"},
            3: {"Name": "BMW X5", "Availability": "Available"}
        }

    @classmethod
    def update_rent_record(cls, car_id, user=None, mode="return"):
        """
        Class method to update the rent record dictionary.

        Args:
        - car_id (int): ID of the car being rented or returned.
        - user (str): User's name who is renting or returning the car.
        - mode (str): Mode of operation ('rent' or 'return').
        """
        if mode == "rent":
            cls.rent_record[car_id] = user  # Add entry to rent_record dictionary
        elif mode == "return":
            cls.rent_record.pop(car_id, None)  # Remove entry from rent_record dictionary

    def display_cars(self):
        """
        Method to display the current cars in inventory with their availability.
        """
        print("--Cars--")
        for car_id, car_info in self.car_dict.items():
            print(f"Car ID: {car_id}, Name: {car_info['Name']}, Availability: {car_info['Availability']}")
        print("")

    def add_car(self):
        """
        Method to add a new car to the inventory.
        """
        while True:
            user_choice = input("Do you want to add a new car? (yes | no): ").lower().strip()
            if user_choice == "yes":
                car_name = input("Please enter the name of the car: ")
                if car_name.isdigit():
                    print("Invalid name, try with letters")
                elif car_name.strip() == "":
                    print("Invalid name")
                else:
                    car_id = len(self.car_dict) + 1
                    self.car_dict[car_id] = {"Name": car_name, "Availability": "Available"}
                    print(f"Car '{car_name}' has been added\n")
                    break
            elif user_choice == "no":
                print("")
                break
            else:
                print("Invalid option")

    def rent_car(self):
        """
        Method to allow a user to rent a car from the inventory.
        """
        counter = 0
        for car_id, car_info in self.car_dict.items():
            if car_info['Availability'] == "Not Available":
                counter += 1

        if len(self.car_dict) == counter:
            print("There are no cars available\n")
        else:
            while True:
                try:
                    username = input("Enter your name: ").lower()
                    if not username or username.isdigit():
                        print("Please enter a valid name")
                    elif username.strip() == "":
                        print("Invalid name")
                    else:
                        car_id_rent = int(input("Enter Car ID to rent: "))
                        if car_id_rent in self.car_dict:
                            target_car = self.car_dict[car_id_rent]
                            if target_car["Availability"] == "Available":
                                target_car["Availability"] = "Not Available"
                                Cars.update_rent_record(car_id=car_id_rent, user=username, mode="rent")
                                print(f"Car {car_id_rent} rented to {username}\n")
                                break
                            else:
                                print("The current car is not available\n")
                                break
                        else:
                            print(f"Car ID '{car_id_rent}' not found, please try again")
                except ValueError:
                    print("Try again, enter a number for the car ID")

    def return_car(self):
        """
        Method to allow a user to return a rented car to the inventory.
        """
        while True:
            try:
                username = input("Enter your name: ").lower()
                if not username or username.isdigit():
                    print("Please enter a valid name")
                elif username.strip() == "":
                    print("Invalid name")
                else:
                    car_id_return = int(input("Please select the Car ID to return: "))
                    if car_id_return in self.car_dict:
                        if car_id_return in Cars.rent_record and Cars.rent_record[car_id_return].lower() == username:
                            target_car_return = self.car_dict[car_id_return]
                            if target_car_return["Availability"] == "Not Available":
                                target_car_return["Availability"] = "Available"
                                Cars.update_rent_record(car_id=car_id_return, user=username, mode="return")
                                print(f"Car {car_id_return} has been returned by {username}\n")
                                break
                            else:
                                print("The current car is available and cannot be returned.")
                                print(f"Car ID: {car_id_return} {self.car_dict[car_id_return]}\n")
                                break
                        else:
                            print(f"No record found for {username} renting car ID {car_id_return}\n")
                            break
                    else:
                        print(f"Car ID {car_id_return} not found")
            except ValueError:
                print("Try again, enter a number for the car ID")

    @staticmethod
    def display_rent_record():
        """
        Static method to display the current rent record.
        """
        if len(Cars.rent_record) == 0:
            print("No data available\n")
        else:
            print("--Rent Record--")
            for car_id, username in Cars.rent_record.items():
                print(f"Username: {username} | Car ID: {car_id}")
            print("")

    def menu_options(self):
        """
        Method to display the menu options and handle user input for car rental operations.
        """
        while True:
            options = ["Display Available Cars | Add Car", "Rent a Car", "Return a Car", "View Your Rented Cars",
                       "Exit"]
            index = 1
            for opt in options:
                print(f"{index}. {opt}")
                index += 1
            try:
                user_choice = int(input("Enter choice: "))
                print("")
                if user_choice in range(1, len(options) + 1):
                    if user_choice == 1:
                        self.display_cars()
                        self.add_car()
                    elif user_choice == 2:
                        self.display_cars()
                        self.rent_car()
                    elif user_choice == 3:
                        self.display_cars()
                        self.return_car()
                    elif user_choice == 4:
                        self.display_rent_record()
                    elif user_choice == 5:
                        print("Bye")
                        exit()
                else:
                    print("Please enter a valid option")
            except ValueError:
                print(f"Invalid input, please enter a number from 1 to {len(options)}\n")


def main():
    """
    Entry point for the car rental management system.
    Initializes the Cars class and starts the menu options for user interaction.
    """
    # Create an object from class Cars and start the car rental system by calling car_system.menu_options()
    car_system = Cars()
    car_system.menu_options()


if __name__ == "__main__":
    main()
