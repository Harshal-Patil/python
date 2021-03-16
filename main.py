age=int(input("Enter The Your Current Age="))
years_rem= 90-age
days_rem= years_rem*365
months_rem= years_rem*12
weeks_rem= years_rem*15
message = f"You Have {days_rem} days,{weeks_rem} weeks,{months_rem} months left"
print(message)
