num = int(input("Enter the number for the multiplication table: "))  
limit = int(input("Enter the limit: "))
print(f"Multiplication table for {num} up to {limit}:")
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")