# Created by ali_h on 6/30/2026 at 7:45 PM
# Source: docs/batool/lect1.pdf (page 7 of 7)
y = eval(input("Enter your grade: "))
if (y >= 90 and y <= 100):
    print("Excellent")
elif (y >= 80 and y <= 100):
    print("Very Good")
elif (y >= 70 and y <= 79):
    print("Good")
elif (y >= 60 and y <= 69):
    print("Medium")
elif (y >= 50 and y <= 59):
    print("Pass")
elif (y > 100 or y < 0):
    print("Invalid input")
else:
    print("Fail")
