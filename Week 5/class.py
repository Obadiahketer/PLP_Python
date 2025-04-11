class Car:
    color = "red"  # Class variable
    model = "Mercedes Benz GLE"  # Class variable
    def drive():
        print("Car is driving")

my_car = Car()
print(my_car.color)  # Accessing class variable using instance
print(my_car.model)  # Accessing class variable using instance