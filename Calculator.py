def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y


def main():
    print("Simple Calculator CLI App")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = input("Select operation (1/2/3/4 or q to quit): ")
            if choice == 'q':
                print("Thanks for choosing me!")
                break
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please select a valid operation.")
                continue

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print("An error occurred:", str(e))


if __name__ == "__main__":
    main()

