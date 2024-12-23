deposit = float(input("What is the original deposit (positive value)? "))
while deposit <= 0:
    print("Input must be a positive value.")
    deposit = float(input("What is the original deposit (positive value)? "))

interest_rate = float(input("What is the interest rate (positive value)? "))
while interest_rate <= 0:
    print("Input must be a positive value.")
    interest_rate = float(input("What is the interest rate (positive value)? "))

num_months = int(input("What is the number of months (positive value)? "))
while num_months <= 0:
    print("Input must be a positive value.")
    num_months = int(input("What is the number of months (positive value)? "))

goal_amount = float(input("What is the goal amount (can enter 0 but not negative)? "))
while goal_amount < 0:
    print("Input must be 0 or a positive value.")
    goal_amount = float(input("What is the goal amount (can enter 0 but not negative)? "))

#annual interest rate to monthly interest rate
monthly_interest_rate = interest_rate / 100 / 12

#monthly balances
current_balance = deposit
print("\nMonthly Account Balances:")
for month in range(1, num_months + 1):
    current_balance += current_balance * monthly_interest_rate
    print(f"Month {month}: Account Balance is: ${current_balance:,.2f}")

#time to reach the goal
if goal_amount > 0:
    current_balance = deposit
    months_to_goal = 0
    while current_balance < goal_amount:
        current_balance += current_balance * monthly_interest_rate
        months_to_goal += 1
    print(f"\nIt will take {months_to_goal} months to reach the goal of ${goal_amount:,.2f}.")
else:
    print("\nNo goal amount was specified.")
