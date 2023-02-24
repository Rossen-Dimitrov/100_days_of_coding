# with open("file_1.txt") as file_1:
#     list_1 = file_1.readlines()
#
# with open("file_2.txt") as file_2:
#     list_2 = file_2.readlines()
#
# new_list = [int(num) for num in list_1 if num in list_2]
# print(new_list)
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# scores = {student: random.randint(1, 100) for student in names}
# print(scores)
#
# passed = {key: value for (key, value) in scores.items() if value > 50}
# print(passed)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word: len(word) for word in sentence.split()}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)