a = int(input("Enter start of range:"))
b = int(input("Enter end of range:"))
print('Special numbers between' ,a, "and" ,b, ".")


original_number = a
num_digits = 0
while a > 0:
    a //= 10
    num_digits += 1

temp_number = original_number
digit_sum = 0
while temp_number > 0:
    digit = temp_number % 10
    digit_sum += digit ** num_digits
    temp_number //= 10

print(a)


