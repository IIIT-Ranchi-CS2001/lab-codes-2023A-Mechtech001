number = int(input("Enter a number: "))  
sum = 0
n = number
while number > 0:
    digit = number % 10
    sum += digit
    number = number // 10
print(f"Number: {n}")
print(f"Sum of digits: {sum}")
