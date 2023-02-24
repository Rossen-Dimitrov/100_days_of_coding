year = int(input("Which year do you want to check? "))
leap = False
if year % 4 == 0:
    leap = True
    if year % 100 == 0:
        leap = False
        if year % 400 == 0:
            leap = True

if leap:
    print("Leap year")
else:
    print("Not Leap year")
