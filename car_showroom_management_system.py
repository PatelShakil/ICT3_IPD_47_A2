# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 10:39:32 2025

@author: Acer
"""
# Custom Exception for Salary Restriction
class SalaryTooLowException(Exception):
    def __init__(self, message="Salary is less than ₹1,00,000. Access denied!"):
        super().__init__(message)


# Base Car Class (Encapsulation)
class Car:
    def __init__(self, brand, model, price, fuel_type, transmission, color):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__fuel_type = fuel_type
        self.__transmission = transmission
        self.__color = color

    def get_details(self):
        return {
            "Brand": self.__brand,
            "Model": self.__model,
            "Price": self.__price,
            "Fuel Type": self.__fuel_type,
            "Transmission": self.__transmission,
            "Color": self.__color
        }

    def get_model(self):
        return self.__model


# Derived Class (Inheritance Example)
class LuxuryCar(Car):
    def __init__(self, brand, model, price, fuel_type, transmission, color, extra_features):
        super().__init__(brand, model, price, fuel_type, transmission, color)  # inheritance in action
        self.__extra_features = extra_features

    def get_details(self):
        details = super().get_details()  # reuse parent method
        details["Luxury Features"] = self.__extra_features
        return details


# Showroom Class
class Showroom:
    def __init__(self):
        self.inventory = []

    def view_available_cars(self):
        if not self.inventory:
            print("No cars available in the showroom.")
        else:
            print("\nAvailable Cars:")
            for car in self.inventory:
                print(f"- {car.get_model()}")

    def display_car_details(self, model, user_salary):
        try:
            if user_salary < 100000:
                raise SalaryTooLowException()

            for car in self.inventory:
                if car.get_model().lower() == model.lower():
                    details = car.get_details()
                    print("\nCar Details:")
                    for key, value in details.items():
                        print(f"{key}: {value}")
                    return
            print("Car not found in inventory.")

        except SalaryTooLowException as e:
            print(e)

    def sell_car(self, model):
        for car in self.inventory:
            if car.get_model().lower() == model.lower():
                self.inventory.remove(car)
                print(f"Car '{model}' sold successfully.")
                return
        print("Car not found in inventory.")

    def buy_car(self, car):
        self.inventory.append(car)
        print(f"Car '{car.get_model()}' added to showroom inventory.")


# Main Program (Menu-Driven Interface)
def main():
    showroom = Showroom()

    # Adding some default cars
    showroom.buy_car(Car("Honda", "City", 1200000, "Petrol", "Manual", "White"))
    showroom.buy_car(Car("Tata", "Nexon", 900000, "Petrol", "Automatic", "Blue"))
    showroom.buy_car(LuxuryCar("Mercedes", "S-Class", 9500000, "Petrol", "Automatic", "Black",
                               ["Massage Seats", "360 Camera", "Ambient Lighting"]))

    while True:
        print("\n--- Car Showroom Management ---")
        print("1. View Available Cars")
        print("2. Display Car Details")
        print("3. Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            showroom.view_available_cars()

        elif choice == "2":
            model = input("Enter model name: ")
            salary = int(input("Enter your salary: "))
            showroom.display_car_details(model, salary)

        elif choice == "3":
            model = input("Enter model name to sell: ")
            showroom.sell_car(model)

        elif choice == "4":
            car_type = input("Enter type (normal/luxury): ").strip().lower()
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            price = int(input("Enter price: "))
            fuel = input("Enter fuel type: ")
            transmission = input("Enter transmission: ")
            color = input("Enter color: ")

            if car_type == "luxury":
                features = input("Enter luxury features (comma separated): ").split(",")
                showroom.buy_car(LuxuryCar(brand, model, price, fuel, transmission, color, features))
            else:
                showroom.buy_car(Car(brand, model, price, fuel, transmission, color))

        elif choice == "5":
            print("Exiting... Thank you for using Car Showroom System.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
