# Recursive function to calculate the factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def get_valid_input():
    while True:
        try:
            num = int(input("Enter a non-negative integer to calculate its factorial: "))
            if num < 0:
                print("Factorial is not defined for negative numbers. Please try again.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")

def main():
    while True:
        num = get_valid_input()
        result = factorial(num)
        print(f"The factorial of {num} is {result}")

        repeat = input("Do you want to calculate another factorial? (yes/no): ").lower()
        if repeat != "yes":
            break

if __name__ == "__main__":
    main()