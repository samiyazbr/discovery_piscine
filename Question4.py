# Program to calculate factorial of a number

num = int(input("Enter number: "))

fact = 0                            # ⚠️ Logical: should start with 1

for i in range(1, num + 1)          # ❌ Missing colon
    fact = fact * i                 # ⚠️ Multiplying by 0 → always 0
    print("Current factorial:" fact)  # ❌ Missing comma between arguments

if num < 0                           # ❌ Missing colon
    print("Negative numbers not allowed")
elif num == 0:
    print("Factorial is 1")
else                                 # ❌ Missing colon
    print("Final factorial is" fact)  # ❌ Missing comma between arguments

pritn("Calculation done")            # ❌ Typo: print misspelled
print("Factorial of" num "is" fact)  # ❌ Missing commas between arguments
print("Program completed"            # ❌ Missing closing parenthesis
result = factorial(num)              # ⚠️ Logical/NameError: function not defined
