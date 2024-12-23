print("Prof. C's Temp Converter:")

# Get the temperature
temp = float(input("Enter a temperature: "))

# Fahrenheit or Celsius
scale = input("Is the temp F for Fahrenheit or C for Celsius? ")

if scale == 'F':
    if temp > 212:
        print("Temp can not be > 212")
    else:
        # Convert Fahrenheit to Celsius
        celsius = (5 / 9) * (temp - 32)
        print(f"The Celsius equivalent is: {round(celsius, 1)}")

elif scale == 'C':
    if temp > 100:
        print("Temp can not be > 100")
    else:
        # Convert Celsius to Fahrenheit
        fahrenheit = (9 / 5) * temp + 32
        print(f"The Fahrenheit equivalent is: {round(fahrenheit, 1)}")

else:
    print("You must enter a F or C")
