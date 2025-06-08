import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
count_letters = int(input("How many letters would you like?\n"))
count_numbers = int(input("How many numbers would you like?\n"))
count_symbols = int(input("How many symbols would you like?\n"))


my_password = []
for i in range(count_letters):
    my_password.append(random.choice(letters))
for i in range(count_numbers):
    my_password.append(random.choice(numbers))
for i in range(count_symbols):
    my_password.append(random.choice(symbols))
print("Before my password = ", my_password)
random.shuffle(my_password)
print("After Shuffle my password is ",my_password)


for i in my_password:
    print(i, end='')
### pr

