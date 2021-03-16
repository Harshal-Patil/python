print("Welcome To Tip Calculator")
bill=float(input("What was the total bill $"))
percntage=int(input("what percntage tip would you like to give? 10,12 or 15="))
people=int(input("How many people to split the bill?"))
bill_percentage=percntage/ 100
total_tip_amount=bill * bill_percentage
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f" Each Person Should Pay{final_amount}")