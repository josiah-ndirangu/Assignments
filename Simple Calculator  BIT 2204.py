# A SIMPLE CALCULATOR
# Function to Perform Addition Of Two Numbers
def add(a, b):
    return a+b

# Function To Find The Difference Of Two Numbers
def subtract(a, b):
    return a-b

 # Function To Find The Product Of Two Numbers
def multiply(a, b):
     return a*b

#Function To Find The Division Of Two Numbers
def divide(a, b):
    if b==0:
        return "Cannot divide by Zero!"
    return a/b

# Function To Find The Remainder Of Two Numbers
def remainder(a, b):
    if b==0:
        return "No Remainder when divided by Zero!"
    return a%b

print("Using The Calculator")

num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))

#1. Addition
#2. Subtraction
#3. Multiplication
#4. Division
#5. Remainder

print(" Select an operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")

Operation =input("Enter operation (1/2/3/4/5): ")

if Operation =="1":
    print("Answer:", num1, "+", num2, "=", add(num1, num2))
elif Operation =="2":
    print("Answer:", num1, "-", num2, "=", subtract(num1, num2))
elif Operation =="3":
    print("Answer:", num1, "*", num2, "=", multiply(num1, num2))
elif Operation =="4":
    print("Answer:", num1, "/", num2, "=", divide(num1, num2))
elif Operation =="5":
     print("Remainder:", num1, "%", num2, "=", remainder(num1, num2))
else:
    print("Invalid Entry")


