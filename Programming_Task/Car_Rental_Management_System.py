class Cars:
    # def __init__(self, car_id, car_name, availability="Available"):
    #     self.car_id = car_id
    #     self.car_name = car_name
    #     self.availability = availability

    car_dict = (
        {"ID": 1, "Name": "Toyota Corolla", "Availability": "Available"},
        {"ID": 2, "Name": "Ford Mustang", "Availability": "Available"},
        {"ID": 3, "Name": "BMW X5", "Availability": "Available"}
    )

    def display_cars(self):
        for car in Cars.car_dict:
            print(car)

    def rent_car(self):
        while True:
            try:
                username = input("Enter Your Name: ")
                car_id = int(input("Enter Car ID to Rent: "))
                for car in self.car_dict:
                    if car["ID"] == car_id:
                        if car["Availability"] == "Available":
                            car["Availability"] = "Not Available"
                            print(f"Car {car_id} rented to {username}")
                            break
                    else:
                        print(f"Car ID '{car_id}' not found")
                        break
            except ValueError:
                print("Please enter a number for the car ID")


    def menu_options(self):
        options = ["Display Available Cars", "Rent a Car", "Return a Car", "View Your Rented Cars", "Exit"]
        index = 1
        for opt in options:
            print(f"{index}. {opt}")
            index += 1

        while True:
            try:
                user_choice = int(input("Enter choice: "))
                if user_choice in range(1, len(options) + 1):
                    break
                else:
                    print("Please Enter a Valid Option")
            except ValueError:
                print("Please Enter a Number")


cars_instance = Cars()
cars_instance.menu_options()
cars_instance.rent_car()

