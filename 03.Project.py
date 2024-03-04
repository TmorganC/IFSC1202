a = float(input("Enter First Number:"))
o = input("Enter Operator (+-*/):")
b = float(input("Enter Second Number:"))
if o == "+":
    print(a + b)
elif o == "-":
    print(a - b)
elif o == "*":
    print(a * b) 
elif o ==("/"):
    print(a / b)     
else:
    print("Invalid Operator")
    
