class Cars:
    def __init__(self, car_id, car_name, availability="Available", user_rent=False):
        self.car_id = car_id
        self.car_name = car_name
        self.availability = availability
        self.user_rent = user_rent

    def __str__(self):
        print(f"Car ID: {self.car_id}, Name: {self.name}, Availability: {self.availability}")


class System:
    def __init__(self):
        self.    car_dict = (
        {"ID": 1, "Name": "Toyota Corolla", "Availability": "Available"},
        {"ID": 2, "Name": "Ford Mustang", "Availability": "Available"},
        {"ID": 3, "Name": "BMW X5", "Availability": "Available"}
        )

# ??