n = int(input("Enter the number of terms : "))
a = 0
b = 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The first {n} terms of the Fibonacci series are:")
    while count < n:
        print(a, end=" ")
        a, b = b, a +b
        count += 1