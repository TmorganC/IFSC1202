a = float(input("Side a:"))
b = float(input("Side b:"))
c = float(input("Side c:"))

s = float(.5 * (a + b + c))

import math
A = float(math.sqrt(s*(s-a)*(s-b)*(s-c)) )

print("Area:")
print(A)