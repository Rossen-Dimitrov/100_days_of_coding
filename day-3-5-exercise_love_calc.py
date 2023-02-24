your_name = (input("Enter your name:\n"))
their_name = (input("Enter their name:\n"))

combined_name = your_name.lower() + their_name.lower()

first_word = 0
second_word = 0

for char in "true":
    first_word += combined_name.count(char)

for char in "love":
    second_word += combined_name.count(char)

score = str(first_word) + str(second_word)

if 10 > int(score) > 90:
    print(f"Your score is **{score}**, you go together like coke and mentos.")
elif 40 < int(score) < 50:
    print(f"Your score is **{score}**, you are alright together.")
else:
    print(f"Your score is **{score}**.")
