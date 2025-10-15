# Program to calculate factorial of a number

num = int(input("Enter number: "))

fact = 0

for i in range(1, num + 1)
    fact = fact * i
    print("Current factorial:", fact)

if num < 0
    print("Negative numbers not allowed")
elif num == 0:
    print("Factorial is 1")
else
    print("Final factorial is", fact)

pritn("Calculation done")
print("Result:" fact)