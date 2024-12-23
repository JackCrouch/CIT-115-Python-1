#name of the person
name = input("Enter the name of the person: ")

#four test scores
try:
    score1 = float(input("Test 1: "))
    score2 = float(input("Test 2: "))
    score3 = float(input("Test 3: "))
    score4 = float(input("Test 4: "))
except ValueError:
    print("Please enter valid numbers for the test scores.")
    exit()

#all scores are not negative
if score1 < 0 or score2 < 0 or score3 < 0 or score4 < 0:
    print("Test scores must be greater than 0.")
    exit()

#Ask if the user wants to drop the lowest score
drop = input("Do you wish to drop the lowest grade Y or N? ").upper()
if drop not in ["Y", "N"]:
    print("Invalid input. Enter Y or N.")
    exit()

#Calculate the average based on the drop option
scores = [score1, score2, score3, score4] 
if drop == "Y":
    scores.remove(min(scores))  #Drop the lowest score
average = sum(scores) / len(scores)  #Calculate average

#the letter grade
if average >= 94:
    grade = "A"
elif average >= 90:
    grade = "A-"
elif average >= 87:
    grade = "B+"
elif average >= 84:
    grade = "B"
elif average >= 80:
    grade = "B-"
elif average >= 77:
    grade = "C+"
elif average >= 74:
    grade = "C"
elif average >= 70:
    grade = "C-"
elif average >= 67:
    grade = "D+"
elif average >= 64:
    grade = "D"
elif average >= 60:
    grade = "D-"
else:
    grade = "F"

#the results
print(f"{name}'s test average is: {average:.1f}")
print(f"Letter Grade for the test is: {grade}")
