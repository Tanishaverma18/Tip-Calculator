# Tip Calculator

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? ₹"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? ₹"))
total_people = int(input("How many people to split the bill? "))
bill_with_tip = (total_bill / total_people) - tip
print("Each person should pay: ", round(bill_with_tip, 2))