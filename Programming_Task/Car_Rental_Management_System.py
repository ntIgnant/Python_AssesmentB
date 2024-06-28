class Cars:
    def __init__(self):
        self.car_dict = {
            1: {"Name": "Toyota Corolla", "Availability": "Available"},
            2: {"Name": "Ford Mustang", "Availability": "Available"},
            3: {"Name": "BMW X5", "Availability": "Available"}
        }

        self.rent_record = {}

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
                car_id = int(input("Enter Car ID to Rent: "))
                if car_id in self.car_dict:
                    target_car = self.car_dict[car_id]
                    if target_car["Availability"] == "Available":
                        if car_id not in self.rent_record:
                            target_car["Availability"] = "Not Available"
                            self.rent_record[car_id] = {"user": username}
                            print(f"Car {car_id} rented to {username}\n")
                            break
                        else:
                            print(f"Car {car_id} was already rented to {username}\n")
                            break
                    else:
                        print("The current car is not available")
                else:
                    print(f"Car ID '{car_id}' not found, please try again")

            except ValueError:
                print("Please enter a number for the car ID")



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
                        Cars.display_cars(self)
                    elif user_choice == 2:
                        Cars.rent_car(self)
                else:
                    print("Please Enter a Valid Option")
            except ValueError:
                print(f"Invalid Input, please enter a number from 1 to {len(options)}\n")


cars_instance = Cars()
cars_instance.menu_options()
