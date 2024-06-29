class Cars:
    rent_record = {}

    def __init__(self):
        self.car_dict = {
            1: {"Name": "Toyota Corolla", "Availability": "Available"},
            2: {"Name": "Ford Mustang", "Availability": "Available"},
            3: {"Name": "BMW X5", "Availability": "Available"}
        }

    @classmethod
    def update_rent_record(cls, car_id, user, mode):
        if mode == "rent":
            cls.rent_record[car_id] = user
        elif mode == "return":
            cls.rent_record.pop(car_id)

    def display_cars(self):
        for car_id, car_info in self.car_dict.items():
            print(f"Car ID: {car_id}, Name: {car_info['Name']}, Availability: {car_info['Availability']}")
        print("")
        # For each id of the dictionary, and for each information of each id, it will print out the information
        # with the specific keys in between brackets []

    def rent_car(self):
        while True:
            try:
                username = input("Enter Your Name: ")
                car_id_rent = int(input("Enter Car ID to Rent: "))
                if car_id_rent in self.car_dict:
                    target_car = self.car_dict[car_id_rent]
                    if target_car["Availability"] == "Available":
                        target_car["Availability"] = "Not Available"
                        Cars.update_rent_record(car_id=car_id_rent, user=username, mode="rent")
                        print(f"Car {car_id_rent} rented to {username}\n")
                        break
                    else:
                        print("The current car is not available")
                else:
                    print(f"Car ID '{car_id_rent}' not found, please try again")

            except ValueError:
                print("Try again, enter a number for the car ID")

    def return_car(self):
        while True:
            try:
                car_id_return = int(input("Please select the Car ID to return: "))
                if car_id_return in self.car_dict:
                    target_car_return = self.car_dict[car_id_return]
                    if target_car_return["Availability"] == "Not Available":
                        target_car_return["Availability"] = "Available"
                        Cars.update_rent_record(car_id=car_id_return)
                        print(f"Car {car_id_return} has been returned!\n")
                        break
                    else:
                        print("The current car is available and can not be returned")
                        print(f"Car ID: {car_id_return} {self.car_dict[car_id_return]}\n")
                        break
                else:
                    print(f"Car ID {car_id_return} not found")
            except ValueError:
                print("Try again, enter a number for the car ID")

    def display_rent_record(self):
        if len(Cars.rent_record) == 0:
            print("No data available\n")
        else:
            for car_id, username in Cars.rent_record.items():
                print(f"Username: {username} | Rented cars: {car_id}")
            print("")

    def menu_options(self):
        while True:
            options = ["Display Available Cars", "Rent a Car", "Return a Car", "View Your Rented Cars", "Exit"]
            index = 1
            for opt in options:
                print(f"{index}. {opt}")
                index += 1
            try:
                user_choice = int(input("Enter choice: "))
                if user_choice in range(1, len(options) + 1):
                    if user_choice == 1:
                        self.display_cars()
                    elif user_choice == 2:
                        self.rent_car()
                    elif user_choice == 3:
                        self.return_car()
                    elif user_choice == 4:
                        self.display_rent_record()
                    elif user_choice == 5:
                        exit()
                else:
                    print("Please Enter a Valid Option")
            except ValueError:
                print(f"Invalid Input, please enter a number from 1 to {len(options)}\n")


cars_instance = Cars()
cars_instance.menu_options()