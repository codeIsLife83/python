# This is a simple Python script


# def multiply_by_two(number, multiplier):
#     return number * multiplier


# # Taking input from the user
# user_input1 = float(input("Enter a number: "))

# # Taking input from the user
# user_input2 = float(input("multiplied by a number: "))

# # Calculating the result
# result = multiply_by_two(user_input1, user_input2)

# # Printing the result
# print(f"The result is {result}")


def multiply_by_two(number, multiplier):
    return number * multiplier


# Taking input from the user
while True:
    try:
        user_input1 = input("Enter a number: ")
        user_input1 = int(user_input1)  # Try to convert the input to an integer
        break  # If successful, exit the loop
    except ValueError:
        print("That's not an integer. Please try again.")

while True:
    try:
        user_input2 = input("Enter another number: ")
        user_input2 = int(user_input2)  # Try to convert the input to an integer
        break  # If successful, exit the loop
    except ValueError:
        print("That's not an integer. Please try again.")


# Calculating the result
result = multiply_by_two(user_input1, user_input2)

# Printing the result
print(f"The result is {result}")
