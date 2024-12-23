#float input
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#sales tax rate based on the state
def get_sales_tax_rate(state):
    if state.upper() == "CT":
        return 0.06
    elif state.upper() == "MA":
        return 0.0625
    elif state.upper() == "ME":
        return 0.055
    elif state.upper() == "NH":
        return 0.0
    elif state.upper() == "RI":
        return 0.07
    else:
        print("Invalid state entered. Assuming no sales tax.")
        return 0.0

#welcome
print("Welcome to the Paint Job Estimator!")

#Get inputs
square_feet = get_float_input("Enter wall space in square feet: ")
paint_price = get_float_input("Enter paint price per gallon: ")
feet_per_gallon = get_float_input("Enter feet per gallon: ")
labor_rate = get_float_input("Enter labor charge per hour: ")
hours_per_gallon = get_float_input("Enter how many labor hours per gallon: ")
state = input("Enter state abbreviation: ")
customer_last_name = input("Enter customer's last name: ")

#calculations
gallons_needed = -(-square_feet // feet_per_gallon)  
labor_hours = gallons_needed * hours_per_gallon  
paint_cost = gallons_needed * paint_price
labor_cost = labor_hours * labor_rate
subtotal = paint_cost + labor_cost
tax_rate = get_sales_tax_rate(state)
sales_tax = subtotal * tax_rate
total_cost = subtotal + sales_tax

#results
print("\n--- Cost Estimate ---")
print(f"Gallons of paint: {gallons_needed:.0f}")
print(f"Hours of labor: {labor_hours:.1f}")
print(f"Paint charges: ${paint_cost:.2f}")
print(f"Labor charges: ${labor_cost:.2f}")
print(f"Tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")

#save results to file
file_name = f"{customer_last_name}_PaintJobOutput.txt"
with open(file_name, "w") as file:
    file.write(f"Gallons of paint: {gallons_needed:.0f}\n")
    file.write(f"Hours of labor: {labor_hours:.1f}\n")
    file.write(f"Paint charges: ${paint_cost:.2f}\n")
    file.write(f"Labor charges: ${labor_cost:.2f}\n")
    file.write(f"Tax: ${sales_tax:.2f}\n")
    file.write(f"Total cost: ${total_cost:.2f}\n")
print(f"\nFile '{file_name}' was created.")
