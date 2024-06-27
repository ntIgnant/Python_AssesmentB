class Cars:
    car_dict = (
        {"ID": 1, "Name": "Toyota Corolla", "Availability": "Available"},
        {"ID": 2, "Name": "Ford Mustang", "Availability": "Available"},
        {"ID": 3, "Name": "BMW X5", "Availability": "Available"}
    )
    def display_cars(self):
        for car in self.car_dict:
            print(car)

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
cars_instance.display_cars()
