# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # squared_numbers = [x**2 for x in numbers]
# # print(squared_numbers)
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)
# with open("./Day26Start/file1.txt", mode="r") as f1:
#     list1 = f1.readlines()
# with open("./Day26Start/file2.txt", mode="r") as f2:
#     list2 = f2.readlines()
# result = [int(x) for x in list1 if x in list2]
# print(result)
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_words = sentence.split(" ")
# result = {x: len(x) for x in list_words}
# print(result)
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {x: y*9/5+32 for (x, y) in weather_c.items()}
# print(weather_f)
import pandas as pd


data = pd.read_csv("./Day26Start/nato_phonetic_alphabet.csv")
my_dict = {row.letter: row.code for (index, row) in data.iterrows()}
is_on = True
while is_on:
    word = input("Enter a word: ").upper()
    try:
        print([my_dict[x] for x in word])
    except KeyError:
        print('Sorry, only letters in the alphabet please')
    else:
        is_on = False
