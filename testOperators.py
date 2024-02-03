# num1 = 1
# num2 = '1'

# print(num1 == num2) # False
# print(num1 is num2) # False
# print(num1 is not num2) # True
# print(num1 != num2) # True
# print(num1 == int(num2)) # True
# print(str(num1) == num2) # True


list = {"apple":[4,5,6], "banana":[7,8,9], "cherry":[10,11,12]}

# for key in list:
#     print(key, list[key])

# for key, value in list.items():
#     print(key, value)

for key in list:
    for value in list[key]:
        print(value)