#printing a multiplication table

n = int(input("Enter a number: "))
for i in range(12):
    result = n * i
    print(f'{n} x {i} = {result}')