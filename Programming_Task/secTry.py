# def rent_car(self):
#     while True:
#         try:
#             username = input("Enter Your Name: ")
#             car_id = int(input("Enter Car ID to Rent: "))
#             for car in self.car_dict:
#                 if car["ID"] == car_id:
#                     if car["Availability"] == "Available":
#                         car["Availability"] = "Not Available"
#                         print(f"Car {car_id} rented to {username}")
#                         break
#                 else:
#                     print(f"Car ID '{car_id}' not found")
#                     break
#         except ValueError:
#             print("Please enter a number for the car ID")