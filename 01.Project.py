num = int(input("Enter Length of Time in Days:"))

year = int(num/365)
week = int((num%365)/7)
day = int((num%365)%7)

print("Years")
print(year)
print("Weeks")
print(week)
print("Days")
print(day)
