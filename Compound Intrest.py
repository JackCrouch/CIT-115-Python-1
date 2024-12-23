#Inputs
PV = float(input("Enter the starting principal: "))
R = float(input("Enter the annual intrest rate: "))
m = int(input("How many times per year in the intrest compounded? "))
t = float(input("For how many years will the account earn intrest? "))
#intrest rate to decimal
r = R / 100
#Calculation
FV = PV * (1 + r / m) ** (m * t)
#Format
print(f"At the end of {t} years you will have $ {FV:.2f}")
