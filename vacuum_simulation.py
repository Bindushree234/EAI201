# Vacuum Cleaner Simulation  

def solid():
    while True:
        print("\n--- Solid Options ---")
        print("1. Dust")
        print("2. Rocks/Papers")
        print("3. Others")
        print("4. Back to Start")

        try:
            y = int(input("Choose the type of solid: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if y == 1:
            print("The vacuum is sucking the dust...")
            print("The shape of the vacuum has changed to Rectangle\n")
        elif y == 2:
            print("The vacuum is sucking the rocks/papers...")
            print("The shape of the vacuum has changed to Circle\n")
        elif y == 3:
            print("The vacuum is sucking other solid materials...")
            print("The shape of the vacuum has changed to Square\n")
        elif y == 4:
            break
        else:
            print("Invalid choice for solid\n")


def liquid():
    while True:
        print("\n--- Liquid Options ---")
        print("1. Water")
        print("2. Beverage")
        print("3. Others")
        print("4. Back to Start")

        try:
            z = int(input("Choose the type of liquid: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if z == 1:
            print("The vacuum is sucking the water...")
            print("The shape of the vacuum has changed to Funnel\n")
        elif z == 2:
            print("The vacuum is sucking the beverage...")
            print("The shape of the vacuum has changed to Funnel\n")
        elif z == 3:
            print("The vacuum is sucking the liquid...")
            print("The shape of the vacuum has changed to Cone\n")
        elif z == 4:
            break
        else:
            print("Invalid choice for liquid\n")


def start():
    while True:
        print("\n--- Vacuum Start ---")
        print("1. Solid")
        print("2. Liquid")
        print("3. Back to Commands")

        try:
            x = int(input("Choose category: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if x == 1:
            solid()
        elif x == 2:
            liquid()
        elif x == 3:
            break
        else:
            print("Invalid choice. Try again.")


def left():
    print("The vacuum has turned to the left side\n")


def right():
    print("The vacuum has turned to the right side\n")


def dock():
    print("The vacuum has returned to dock and is charging...\n")


def main():
    while True:
        print("\n--- Main Commands ---")
        print("1. Start (Choose Solid/Liquid)")
        print("2. Left")
        print("3. Right")
        print("4. Dock")
        print("5. Stop")

        try:
            choice = int(input("Enter command: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            start()
        elif choice == 2:
            left()
        elif choice == 3:
            right()
        elif choice == 4:
            dock()
        elif choice == 5:
            print("The vacuum has stopped. Goodbye!\n")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
