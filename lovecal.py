print("Welcome To love Calculator")
name1=input("Enter your Name=")
name2=input("Enter there Name=")
combined_str=name1+name2
lower_case=combined_str.lower()
print(lower_case)
t= lower_case.count("t")
r= lower_case.count("r")
u= lower_case.count("u")
e= lower_case.count("e")
true=t+r+u+e
l= lower_case.count("l")
o= lower_case.count("o")
v= lower_case.count("v")
e= lower_case.count("e")
love=l+o+v+e
love_score=int(str(love)+str(true))
if (love_score<10 or love_score>90):
  print(f"You are love Score is {love_score}You go to toghter like coke and mentos")
elif(love_score>=40 and love_score<=50):
  print(f"Your score is{love_score} you are alright toghter ")
else:
  print(f"Your love score is {love_score}")