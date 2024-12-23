# Declare Constant
MOOSEWEIGHT = 70.5
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
NEPTUNE = 1.12
PLUTO = 0.066
#Input
sDogName = input("What is your dog's Name? ")
fWeight = float(input(f"What is your weight?"))
#Calculate and Print
print(f"Weight on Mercury: {fWeight * MERCURY:.2f}")
print(f"Weight on Venus: {fWeight * VENUS:.2f}")
print(f"Weight on Moon: {fWeight * MOON:.2f}")
print(f"Weight on Mars: {fWeight * MARS:.2f}")
print(f"Weight on Jupiter: {fWeight * JUPITER:.2f}")
print(f"Weight on Saturn: {fWeight * SATURN:.2f}")
print(f"Weight on Neptune: {fWeight * NEPTUNE:.2f}")
print(f"Weight on Pluto: {fWeight * PLUTO:.2f}")
