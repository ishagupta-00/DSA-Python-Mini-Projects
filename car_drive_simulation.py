# -------------------- CAR DRIVE SIMULATION --------------------

def show_status(car):
    print("\n========== CAR STATUS ==========")
    print("Speed:", car["speed"], "km/h")
    print("Distance:", car["distance"], "km")
    print("Fuel:", car["fuel"], "litres")
    print("Engine:", "ON" if car["engine"] else "OFF")


def start_engine(car):
    if car["engine"]:
        print("\nEngine is already ON.")
    else:
        car["engine"] = True
        print("\nEngine started successfully.")


def stop_engine(car):
    if car["speed"] > 0:
        print("\nCannot stop the engine while the car is moving.")
    elif not car["engine"]:
        print("\nEngine is already OFF.")
    else:
        car["engine"] = False
        print("\nEngine stopped.")


def accelerate(car):
    if not car["engine"]:
        print("\nStart the engine first.")
        return

    if car["fuel"] <= 0:
        print("\nNo fuel available.")
        return

    try:
        amount = float(input("Enter acceleration value (km/h): "))

        if amount <= 0:
            print("Acceleration must be positive.")
            return

        car["speed"] += amount

        if car["speed"] > 120:
            car["speed"] = 120
            print("Maximum speed reached: 120 km/h")

        car["fuel"] -= amount * 0.01

        if car["fuel"] < 0:
            car["fuel"] = 0

        print("Car accelerated successfully.")

    except ValueError:
        print("Please enter a valid number.")


def brake(car):
    if car["speed"] == 0:
        print("\nCar is already stopped.")
        return

    try:
        amount = float(input("Enter braking value (km/h): "))

        if amount <= 0:
            print("Braking value must be positive.")
            return

        car["speed"] -= amount

        if car["speed"] < 0:
            car["speed"] = 0

        print("Car slowed down successfully.")

    except ValueError:
        print("Please enter a valid number.")


def drive(car):
    if not car["engine"]:
        print("\nStart the engine first.")
        return

    if car["speed"] <= 0:
        print("\nIncrease the speed first.")
        return

    try:
        time = float(input("Enter driving time (hours): "))

        if time <= 0:
            print("Time must be positive.")
            return

        distance = car["speed"] * time
        fuel_used = distance * 0.1

        if fuel_used > car["fuel"]:
            print("\nNot enough fuel for this journey.")
            return

        car["distance"] += distance
        car["fuel"] -= fuel_used

        print("\nCar drove successfully.")
        print("Distance travelled:", round(distance, 2), "km")

    except ValueError:
        print("Please enter a valid number.")


def refuel(car):
    try:
        amount = float(input("Enter fuel amount (litres): "))

        if amount <= 0:
            print("Fuel amount must be positive.")
            return

        car["fuel"] += amount

        if car["fuel"] > 50:
            car["fuel"] = 50
            print("Fuel tank is full. Maximum capacity is 50 litres.")

        print("Fuel added successfully.")
        print("Current fuel:", round(car["fuel"], 2), "litres")

    except ValueError:
        print("Please enter a valid number.")


def car_menu(car):

    while True:
        print("\n================================")
        print("       CAR DRIVE SIMULATION")
        print("================================")
        print("1. Start Engine")
        print("2. Stop Engine")
        print("3. Accelerate")
        print("4. Brake")
        print("5. Drive")
        print("6. Refuel")
        print("7. Show Car Status")
        print("8. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_engine(car)

        elif choice == "2":
            stop_engine(car)

        elif choice == "3":
            accelerate(car)

        elif choice == "4":
            brake(car)

        elif choice == "5":
            drive(car)

        elif choice == "6":
            refuel(car)

        elif choice == "7":
            show_status(car)

        elif choice == "8":
            print("\nExiting Car Drive Simulation...")
            break

        else:
            print("\nInvalid choice. Please try again.")


def main():

    car = {
        "speed": 0,
        "distance": 0,
        "fuel": 20,
        "engine": False
    }

    car_menu(car)


main()