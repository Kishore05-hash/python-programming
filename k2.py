def find_last_digit(number):
    last_digit = number % 10
    return last_digit
num = int(input("Enter a number: "))
last_digit = find_last_digit(num)
print("The last digit of {num} is {last_digit}.")