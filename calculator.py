def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

def main():
    print("Welcome to the Basic Calculator!")
    
    while True:
        # Display the calculator menu
        print("\n===== BASIC CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        print("----------------------------")
        
        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                number1 = float(input("Enter the first number: "))
                number2 = float(input("Enter the second number: "))
            except ValueError:
                print("\nError: Invalid input! Please enter numeric values only.")
                print("----------------------------")
                continue
            
            print("----------------------------")

            if choice == '1':
                result = add(number1, number2)
                print(f"{number1} + {number2} = {result}")

            elif choice == '2':
                result = subtract(number1, number2)
                print(f"{number1} - {number2} = {result}")

            elif choice == '3':
                result = multiply(number1, number2)
                print(f"{number1} * {number2} = {result}")
                
            elif choice == '4':
                result = divide(number1, number2)
                if result is None:
                    print("Error: Division by zero is not allowed!")
                else:
                    print(f"{number1} / {number2} = {result}")
            
            print("----------------------------")

            calculate_again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if calculate_again == 'no' or calculate_again == 'n':
                print("\nThank you for using the calculator. Goodbye!")
                break
        else:
            print("\nError: Invalid option chosen! Please choose between 1 and 5.")
            print("----------------------------")

if __name__ == "__main__":
    main()
