# Created by ali_h on 6/25/2026 at 1:25 PM
# Source: docs/batool/lect1.pdf (page 2 of 7)
import math

a = eval(input("Enter the number a: "))
b = eval(input("Enter the number b: "))
c = eval(input("Enter the number c: "))
x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print("The first root of the quadratic equation is: ", x1)
print("The second root of the quadratic equation is: ", x2)
