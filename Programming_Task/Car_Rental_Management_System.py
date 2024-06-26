class Cars:

    car_dict = ({"ID": 1, "Name": "Toyota Corolla", "Availability": "Available"},
            {"ID": 2, "Name": "Ford Mustang", "Availability": "Available"},
            {"ID": 3, "Name": "BMW X5", "Availability": "Available"})

    def menu_options():
        options = ["Display Available Cars", "Rent a Car", "Return a Car", "View Your Rented Cars", "Exit"]
        index = 1
        for opt in options:
            print(f"{index}. {opt}")
            index += 1

        while True:
            user_choice = int(input("Enter choice: "))
            try:
                if user_choice in range(1, len(options)+1):
                    break
                else:
                    print("Please Enter a Valid Option")
                    
            except ValueError:
                print("Please Enter a Number")

    def display_cars():
        for car in Cars.car_dict:
            print(car)


Cars.menu_options()
Cars.display_cars()

