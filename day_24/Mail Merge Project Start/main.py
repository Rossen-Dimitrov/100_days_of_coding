with open("./Input/Names/invited_names.txt", mode='r') as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as start:
    starting_letter = start.read()
    for name in names:
        striped_name = name.strip()
        new_letter = starting_letter.replace("[name]", striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as cur_letter:
            cur_letter.write(new_letter)

