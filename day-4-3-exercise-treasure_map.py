user_in = input()

raw1 = ['⬜', '⬜', '⬜']
raw2 = ['⬜', '⬜', '⬜']
raw3 = ['⬜', '⬜', '⬜']
treasure_map = [raw1, raw2, raw3]

treasure_map[int(user_in[1]) - 1][int(user_in[0]) - 1] = "X "

print(f"{raw1}\n{raw2}\n{raw3}")