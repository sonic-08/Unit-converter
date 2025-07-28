
""""
Unit Conveter

"""

print("                  ")

print("🗃️ Unit converter app")
print("                  ")
print("                  ")

print("1. Kilograms to pounds")
print("2. Kilometers to miles")
print("3. Grams to ounces")
print("4. Ounces to Grams")
print("5. Celsius to farenheit")
print("6. Farenheit to celsius")
print("7. cm to inches")
print("8. Inches to feet")
print("9. cm to foot")
print("10. foot to cm")

# In the print statement: print(f"{km} km = {miles: .2f} miles")
    # The symbols {} are used for f-string formatting in Python.
    # When you put a variable or expression inside {}, its value is inserted into the string.
    # For example, {km} will be replaced by the value of km, and {miles: .2f} will be replaced by the value of miles formatted to 2 decimal places.

while True:
    Choice = int(input("Enter your choice what you want to convert(1-10 or 0 to quit): ★ "))

    if Choice == 0:
        quit() 
    
    if Choice > 10:
        print("Please choose between 1-10. If you want quit enter '0 ")

    if Choice == 1:
        kg = float(input("Enter weight in kilograms: "))
        pound = kg * 2.2
        print(f"{kg} kg = {pound: .2f} pounds")

    if Choice == 2:
        km = float(input("Enter distance in kilometres: "))
        miles = km * 0.621371
        print(f"{km} km = {miles: .2f} miles")
        
    if Choice == 3:
        Grams = float(input("Enter weight in grams: "))
        Ounce = Grams / 28.3495
        print(F"{Grams} grams = {Ounce: .2f} ounces")

    if Choice == 4:
        ounce = float(input("Enter weight in ounces: "))
        grams = ounce * 28.3495
        print(f"{ounce} ounce = {grams} grams")

    if Choice == 5:
        celsius = float(input("Enter temperature in celsius: "))
        farenheit = celsius * 9/5 + 32
        print(f"{celsius}◦C  = {farenheit: .2f} farenheit")

    if Choice ==  6:
        farenheit = float(input("Enter temperature in farenheit: "))
        celsius = (farenheit - 32) * 5/9
        print(f"{farenheit} farenheit = {celsius:.2f} ◦C")

    if Choice == 7:
        cm = float(input("Enter length/height in cm: "))
        inch = cm * 0.393701
        print(f"{cm} cm = {inch: .1f} inches")

    if Choice == 8:
        inch = float(input("Enter height/length in inches: "))
        cm = inch * 2.54
        print(f"{inch} inch = {cm: .2f} cm")

    if Choice == 9:
        cm = float(input("Enter height/length in cm: "))
        feet = cm * 0.0328084
        print(f"{cm} cm = {feet: .1f} feet")

    if Choice == 10:
        feet = float(input("Enter height/length in feet: "))
        cm = feet / 0.0328084
        print(f'{feet} feet = {cm: .2f} cm')
        