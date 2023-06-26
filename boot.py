# print((250 + 241 + 244 + 255) / 4)
# max_number_of_players = 1.024e18
# print(max_number_of_players)
# for age in range(0, 75):
#     if age < 8:
#         print(f"You qualify for free meals. You are {age} years old.")
#     elif age > 65:
#         print(f"You qualify for retirement. You are {age} years old.")
#     else:
#         print(age)
################################################################################
# Rocket Launch
# for num in range(10, 0, -1):
#     if num == 1:
#         print(f"{num}... Blastoff!")
#     else:
#         print(f"{num}...")
################################################################################
# Squaring Numbers
# for num in range(100, 110, 1):
#     print(f"{num} squared = {num * num}")
################################################################################
# Christmas Bonus
# number_of_employees = 102

# c_level_bonus = 2000
# manager_bonus = 1000
# standard_bonus = 500

# # C Level Executives
# sarah_id = 1
# mary_id = 2

# # Managers
# john_id = 6
# bob_id = 44
# joe_id = 18

# dollars_needed = 0

# Don't touch above this line
# if num != sarah id or mary id
# for num in range(0, number_of_employees - 1):
#     if num != 1 or num != 2 or num != 6 or num != 44 | num != 18:
#         dollars_needed += standard_bonus
#         print(num)
#     elif num != 1 | num != 2:
#         dollars_needed += manager_bonus
#         print(num)
#     else:
#         dollars_needed += c_level_bonus
#         print(num)

# for num in range(1, 102):
#     if num != sarah_id or num != :
#         dollars_needed += standard_bonus
#         print(f"{num} + {standard_bonus} = {dollars_needed} needed")

#     elif num != 6 or num != 44 or num != 18:
#         dollars_needed += c_level_bonus
#         print(f"{num} + {c_level_bonus} = {dollars_needed}  needed")
#     else:
#         dollars_needed += manager_bonus
#         print(f"{num} + {manager_bonus}  = {dollars_needed} needed")
#     # Don't touch below this line


#     print(f"{dollars_needed} dollars are needed to fulfill all bonuses")

################################################################################
# def get_age(age):
#     character = age[0]
#     myInt = int(character)
#     print(myInt)


# get_age("2 years old")
# get_age("4 years old")
# get_age("5 years old")
# get_age("7 years old")


# def get_age(input_string):
#     age_string = ""
#     for char in input_string:
#         if char.isdigit():
#             age_string += char
#         else:
#             break

#     if age_string:
#         age = int(age_string)
#         return age
#     else:
#         return None
################################################################################
# items = [
#     "Potion",
#     "Leather Scraps",
#     "Bread",
#     "Iron Ore",
#     "Light Leather",
#     "Bread",
#     "Shortsword",
#     "Longsword",
#     "Iron Mace",
#     "Shortsword",
#     "Shortsword",
# ]

# potion_count = 0
# bread_count = 0
# shortsword_count = 0

# # don't touch above this line

# for i in range(0, len(items)):
#     if items[i] == "Potion":
#         potion_count += 1
#     elif items[i] == "Bread":
#         bread_count += 1
#     elif items[i] == "Shortsword":
#         shortsword_count += 1


# # don't touch below this line

# print(f"You have {potion_count} potions in your inventory.")
# print(f"You have {bread_count} pieces of bread in your inventory.")
# print(f"You have {shortsword_count} shortswords in your inventory.")
################################################################################
# players = [
#     "Harry",
#     "Hermione",
#     "Ron",
#     "Ginny",
#     "Fred",
#     "Neville",
#     "Draco",
#     "Luna",
#     "Cho",
#     "Gregory",
#     "Lee",
#     "Michael",
#     "Lavender",
#     "Frank",
#     "Anthony",
# ]

# # Don't touch above this line
# for i in range(0, len(players)):
#     red_team = players[0:16:2]
#     blue_team = players[1:16:2]
################################################################################
# Test Scores
# answer_sheet = ["A", "A", "C", "D", "D", "B", "C"]
# student_answers = ["A", "B", "C", "A", "D", "B", "C"]

# # Don't touch above this line
# count = 0
# percentage = 0.0
# for i in range(len(answer_sheet)):
#     if (answer_sheet[i]) == (student_answers[i]):
#         count += 1


# percentage = count/ len(answer_sheet) * 100

# # Don't touch below this line

# print(f"The student answered correctly on {percentage}% of the questions")

################################################################################
# FIND MAX
# def find_max(nums):
#     max_so_far = float("-inf")
#     max_value = max(nums, default=max_so_far)
#     return max_value


# #BOOT DEV SOLUTION:
# def find_max(nums):
#     max_so_far = float("-inf")
#     for num in nums:
#         if num > max_so_far:
#             max_so_far = num
#     return max_so_far


# def test(nums):
#     max = find_max(nums)
#     print(f"The max of {nums} is {max}")


# test([1, 2, 3, 4, 5])
# test([1, 2, 300, 4, 5])
# test([1, 20, 3, 4, 5])
# test([-1, 2, 3, 4, 5])
# test([1, 2, 3, 21, 18])
# test([])

################################################################################
# # REVERSE ARRAY
# def reverse_array(items):
#     reversed = items.reverse()
#     return items


# # Don't touch below this line


# def test(items):
#     items_copy = items[:]
#     reversed = reverse_array(items)
#     print(f"{items_copy} reversed is: {reversed}")


# test(["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"])
# test(["Haste Potion", "Longsword", "Iron Bar", "Leather Scraps"])
# test([1, 2, 300, 4, 5])
# test(["now!", "order", "reverse", "in", "is", "Array", "This"])
# test(["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"])
################################################################################
# messages = [
#     "well dang it",
#     "dang the whole dang thing",
#     "kill that knight, dang it",
#     "get him!",
#     "donkey kong",
#     "oh come on, get them",
#     "run away from the dang baddies",
# ]

# separator = "\n#################\n"


# def filter_messages(messages):  # messages = list of strings
#     # create the 2 empty lists that you'll return at the end
#     clean_messages = []  # ["well it", "the whole thing", ...]
#     removed_words = []  # [ 1, 2, 1, 0, 0, 0, 1 ]
#     for message in messages:  # message = string
#         words = message.split()  # split string into list of strings
#         # new_words is a temporary list so
#         # we can add words if they are or are not "dang"
#         new_words = ""
#         removed = 0  # count of "dang"s in a given list (words)
#         for word in words:  # loop through the words
#             if word == "dang":
#                 removed += 1  # increment removed count
#             else:
#                 new_words += word
#                 new_words += " "  # append new word to new words
#             # join messages with a space between
#             # add count to the second output list

#         removed_words.append(removed)
#         clean_messages.append(new_words.strip())
#     # return syntax for multiple values
#     # print(f"messages: {messages}")
#     # print(separator)
#     # print(f"clean_messages: {clean_messages}")
#     # print(separator)
#     # print(f"removed_words: {removed_words}")
#     # print(separator)

#     return clean_messages, removed_words


# def filter_messages(messages):
#     clean_messages = []
#     removed_words = []
#     for message in messages:
#         words = message.split()
#         new_words = ""
#         removed = 0
#         for word in words:
#             if word == "dang":
#                 removed += 1
#             else:
#                 new_words += word
#                 new_words += " "

#     removed_words.append(removed)
#     clean_messages.append(new_words.strip())
#     return clean_messages, removed_words
# look at each individual word to see if it is dang

# clean_message = [string.join(clean_words) for string in messages]
# print(clean_message)  # i added this
# dang_counter = 0
# clean_words = []
# words = [string.split() for string in messages]
# print("Words", words)

# for word_list in words:
#     if "dang" in word_list:
#         dang_counter += 1
#         clean_words = word_list.remove("dang")
#         print("Word List", word_list)
#         clean_message.append(clean_words)
#         print(clean_message)

# print("Bad words:", dang_counter)
# print(messages)


# filter_messages(messages)
################################################################################
# def double_string(string):
#     doubled = ""
#     for char in string:
#         doubled += char * 2
#     return doubled


# # Don't touch below this line

# print(double_string("Hello there"))
# print(double_string("General Kenobi"))
# print(double_string("I've been trained in your Jedi arts"))
################################################################################
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False

#     return True

# # Don't touch below this line


# for i in range(0, 25):
#     print(f"{i} is prime: {is_prime(i)}")
################################################################################
def test_score(answer_sheet, student_answers):
    count = 0
    percentage = 0.0
    name = student_answers[0]
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == (student_answers[i + 1]):
            count += 1
    percentage = count / len(answer_sheet) * 100
    return name, percentage


# Don't touch below this line


def test(answer_sheet, student_1_answers):
    name, percentage = test_score(answer_sheet, student_1_answers)
    print(f"{name}: {percentage:.1f}%")


def main():
    answer_sheet = [
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]
    student_1_answers = [
        "Allan",
        "A",
        "C",
        "C",
        "B",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]
    student_2_answers = [
        "John",
        "A",
        "D",
        "A",
        "A",
        "D",
        "A",
        "C",
        "B",
        "D",
        "A",
        "F",
        "A",
        "C",
        "B",
        "D",
        "C",
        "D",
        "C",
        "D",
        "A",
    ]
    student_3_answers = [
        "Jeremy",
        "A",
        "B",
        "D",
        "C",
        "D",
        "B",
        "D",
        "A",
        "C",
        "C",
        "D",
        "A",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "F",
        "A",
    ]
    student_4_answers = [
        "Sally",
        "A",
        "A",
        "D",
        "A",
        "A",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "B",
        "D",
        "C",
        "F",
        "A",
        "D",
        "A",
    ]
    student_5_answers = [
        "Tim",
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]

    test(answer_sheet, student_1_answers)
    test(answer_sheet, student_2_answers)
    test(answer_sheet, student_3_answers)
    test(answer_sheet, student_4_answers)
    test(answer_sheet, student_5_answers)


main()


################################################################################
