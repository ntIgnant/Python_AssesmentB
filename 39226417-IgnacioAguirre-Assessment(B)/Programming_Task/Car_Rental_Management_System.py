class Cars:

    car_dict = ({"Car_ID": 1, "Car_Name": "Toyota Corolla", "Availability": "Available"},
            {"Car_ID": 2, "Car_Name": "Ford Mustang", "Availability": "Available"},
            {"Car_ID": 3, "Car_Name": "BMW X5", "Availability": "Available"})

    def display_available_cars(self):
        for value in Cars.car_dict:
            print(value)


Cars.display_available_cars()
# ???
