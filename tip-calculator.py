#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_split = bill / people
tip_percentage = tip / 100
total_tip = tip_percentage * bill
bill_plus_tip = bill + total_tip
bill_per_person = bill_plus_tip / people
final_amount = round(bill_per_person, 1)
print(input(f"Each person should pay: ${final_amount}"))