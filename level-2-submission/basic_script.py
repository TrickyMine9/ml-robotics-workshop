name = input("What is your name? ")
greeting = f"Hello, {name}! Welcome!"
print(greeting)

try:
    number = float(input("Enter a number to calculate its square: "))
    score = number ** 2
    print(f"The square of {number} is {score}.")
except ValueError:
    print("Please enter a valid number!")
