import random
name = input().split(", ")

number = random.randint(0, len(name) - 1)
print(name[number])

print(random.choice(name))
