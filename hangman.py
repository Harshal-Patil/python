import random
word_list=['mouse','dog','cat']
choose_word=random.choice(word_list)
print(f"choose word={choose_word}")
display=[]
word_length=len(choose_word)
for _ in range(word_length):
  display+="_"
print(display)

end_of_game= False

while end_of_game:
  guess=input("Guess the letter=").lower()
  for position in range(word_length):
    letter=choose_word[position]
    print(f"Current position {position} \n Current letter:{letter}\n Guessed letter {guess}")
    if letter==guess:
      display[position]=letter
  print(display)
  if "_"not in display:
    end_of_game=True
    print("You Win")