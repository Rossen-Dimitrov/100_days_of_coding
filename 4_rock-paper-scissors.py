import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

dictionary = {
    0: "ROCK",
    1: "PAPER",
    2: "SCISSORS"
}

images = [rock, paper, scissors]
print(f"Welcome to ROCK PAPER SCISSORS Game\nType 0 for Rock, 1 for Paper or 2 for Scissors.")

you = int(input("What do you choose? "))

pc = random.randint(0, 2)

if not 0 <= you < 3:
    print("Invalid Choice`\nYou Lose")
else:
    print(f"You chose: {dictionary[you]}")
    print(images[you])
    print(f"Computer chose: {dictionary[pc]}")
    print(images[pc])
    if you == pc:
        print("Draw")
    elif pc == 0 and you == 2:
        print("You Lose")
    elif pc == 2 and you == 0:
        print("You Win")
    elif you > pc:
        print("You Win")
    else:
        print("You Loose")
