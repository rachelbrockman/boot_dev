import math

# # # print((250 + 241 + 244 + 255) / 4)
# # # max_number_of_players = 1.024e18
# # # print(max_number_of_players)
# # # for age in range(0, 75):
# # #     if age < 8:
# # #         print(f"You qualify for free meals. You are {age} years old.")
# # #     elif age > 65:
# # #         print(f"You qualify for retirement. You are {age} years old.")
# # #     else:
# # #         print(age)
# # ################################################################################
# # # Rocket Launch
# # # for num in range(10, 0, -1):
# # #     if num == 1:
# # #         print(f"{num}... Blastoff!")
# # #     else:
# # #         print(f"{num}...")
# # ################################################################################
# # # Squaring Numbers
# # # for num in range(100, 110, 1):
# # #     print(f"{num} squared = {num * num}")
# # ################################################################################
# # # Christmas Bonus
# # # number_of_employees = 102

# # # c_level_bonus = 2000
# # # manager_bonus = 1000
# # # standard_bonus = 500

# # # # C Level Executives
# # # sarah_id = 1
# # # mary_id = 2

# # # # Managers
# # # john_id = 6
# # # bob_id = 44
# # # joe_id = 18

# # # dollars_needed = 0

# # # Don't touch above this line
# # # if num != sarah id or mary id
# # # for num in range(0, number_of_employees - 1):
# # #     if num != 1 or num != 2 or num != 6 or num != 44 | num != 18:
# # #         dollars_needed += standard_bonus
# # #         print(num)
# # #     elif num != 1 | num != 2:
# # #         dollars_needed += manager_bonus
# # #         print(num)
# # #     else:
# # #         dollars_needed += c_level_bonus
# # #         print(num)

# # # for num in range(1, 102):
# # #     if num != sarah_id or num != :
# # #         dollars_needed += standard_bonus
# # #         print(f"{num} + {standard_bonus} = {dollars_needed} needed")

# # #     elif num != 6 or num != 44 or num != 18:
# # #         dollars_needed += c_level_bonus
# # #         print(f"{num} + {c_level_bonus} = {dollars_needed}  needed")
# # #     else:
# # #         dollars_needed += manager_bonus
# # #         print(f"{num} + {manager_bonus}  = {dollars_needed} needed")
# # #     # Don't touch below this line


# # #     print(f"{dollars_needed} dollars are needed to fulfill all bonuses")

# # ################################################################################
# # # def get_age(age):
# # #     character = age[0]
# # #     myInt = int(character)
# # #     print(myInt)


# # # get_age("2 years old")
# # # get_age("4 years old")
# # # get_age("5 years old")
# # # get_age("7 years old")


# # # def get_age(input_string):
# # #     age_string = ""
# # #     for char in input_string:
# # #         if char.isdigit():
# # #             age_string += char
# # #         else:
# # #             break

# # #     if age_string:
# # #         age = int(age_string)
# # #         return age
# # #     else:
# # #         return None
# # ################################################################################
# # # items = [
# # #     "Potion",
# # #     "Leather Scraps",
# # #     "Bread",
# # #     "Iron Ore",
# # #     "Light Leather",
# # #     "Bread",
# # #     "Shortsword",
# # #     "Longsword",
# # #     "Iron Mace",
# # #     "Shortsword",
# # #     "Shortsword",
# # # ]

# # # potion_count = 0
# # # bread_count = 0
# # # shortsword_count = 0

# # # # don't touch above this line

# # # for i in range(0, len(items)):
# # #     if items[i] == "Potion":
# # #         potion_count += 1
# # #     elif items[i] == "Bread":
# # #         bread_count += 1
# # #     elif items[i] == "Shortsword":
# # #         shortsword_count += 1


# # # # don't touch below this line

# # # print(f"You have {potion_count} potions in your inventory.")
# # # print(f"You have {bread_count} pieces of bread in your inventory.")
# # # print(f"You have {shortsword_count} shortswords in your inventory.")
# # ################################################################################
# # # players = [
# # #     "Harry",
# # #     "Hermione",
# # #     "Ron",
# # #     "Ginny",
# # #     "Fred",
# # #     "Neville",
# # #     "Draco",
# # #     "Luna",
# # #     "Cho",
# # #     "Gregory",
# # #     "Lee",
# # #     "Michael",
# # #     "Lavender",
# # #     "Frank",
# # #     "Anthony",
# # # ]

# # # # Don't touch above this line
# # # for i in range(0, len(players)):
# # #     red_team = players[0:16:2]
# # #     blue_team = players[1:16:2]
# # ################################################################################
# # # Test Scores
# # # answer_sheet = ["A", "A", "C", "D", "D", "B", "C"]
# # # student_answers = ["A", "B", "C", "A", "D", "B", "C"]

# # # # Don't touch above this line
# # # count = 0
# # # percentage = 0.0
# # # for i in range(len(answer_sheet)):
# # #     if (answer_sheet[i]) == (student_answers[i]):
# # #         count += 1


# # # percentage = count/ len(answer_sheet) * 100

# # # # Don't touch below this line

# # # print(f"The student answered correctly on {percentage}% of the questions")

# # ################################################################################
# # # FIND MAX
# # # def find_max(nums):
# # #     max_so_far = float("-inf")
# # #     max_value = max(nums, default=max_so_far)
# # #     return max_value


# # # #BOOT DEV SOLUTION:
# # # def find_max(nums):
# # #     max_so_far = float("-inf")
# # #     for num in nums:
# # #         if num > max_so_far:
# # #             max_so_far = num
# # #     return max_so_far


# # # def test(nums):
# # #     max = find_max(nums)
# # #     print(f"The max of {nums} is {max}")


# # # test([1, 2, 3, 4, 5])
# # # test([1, 2, 300, 4, 5])
# # # test([1, 20, 3, 4, 5])
# # # test([-1, 2, 3, 4, 5])
# # # test([1, 2, 3, 21, 18])
# # # test([])

# # ################################################################################
# # # # REVERSE ARRAY
# # # def reverse_array(items):
# # #     reversed = items.reverse()
# # #     return items


# # # # Don't touch below this line


# # # def test(items):
# # #     items_copy = items[:]
# # #     reversed = reverse_array(items)
# # #     print(f"{items_copy} reversed is: {reversed}")


# # # test(["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"])
# # # test(["Haste Potion", "Longsword", "Iron Bar", "Leather Scraps"])
# # # test([1, 2, 300, 4, 5])
# # # test(["now!", "order", "reverse", "in", "is", "Array", "This"])
# # # test(["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"])
# # ################################################################################
# # # messages = [
# # #     "well dang it",
# # #     "dang the whole dang thing",
# # #     "kill that knight, dang it",
# # #     "get him!",
# # #     "donkey kong",
# # #     "oh come on, get them",
# # #     "run away from the dang baddies",
# # # ]

# # # separator = "\n#################\n"


# # # def filter_messages(messages):  # messages = list of strings
# # #     # create the 2 empty lists that you'll return at the end
# # #     clean_messages = []  # ["well it", "the whole thing", ...]
# # #     removed_words = []  # [ 1, 2, 1, 0, 0, 0, 1 ]
# # #     for message in messages:  # message = string
# # #         words = message.split()  # split string into list of strings
# # #         # new_words is a temporary list so
# # #         # we can add words if they are or are not "dang"
# # #         new_words = ""
# # #         removed = 0  # count of "dang"s in a given list (words)
# # #         for word in words:  # loop through the words
# # #             if word == "dang":
# # #                 removed += 1  # increment removed count
# # #             else:
# # #                 new_words += word
# # #                 new_words += " "  # append new word to new words
# # #             # join messages with a space between
# # #             # add count to the second output list

# # #         removed_words.append(removed)
# # #         clean_messages.append(new_words.strip())
# # #     # return syntax for multiple values
# # #     # print(f"messages: {messages}")
# # #     # print(separator)
# # #     # print(f"clean_messages: {clean_messages}")
# # #     # print(separator)
# # #     # print(f"removed_words: {removed_words}")
# # #     # print(separator)

# # #     return clean_messages, removed_words


# # # def filter_messages(messages):
# # #     clean_messages = []
# # #     removed_words = []
# # #     for message in messages:
# # #         words = message.split()
# # #         new_words = ""
# # #         removed = 0
# # #         for word in words:
# # #             if word == "dang":
# # #                 removed += 1
# # #             else:
# # #                 new_words += word
# # #                 new_words += " "

# # #     removed_words.append(removed)
# # #     clean_messages.append(new_words.strip())
# # #     return clean_messages, removed_words
# # # look at each individual word to see if it is dang

# # # clean_message = [string.join(clean_words) for string in messages]
# # # print(clean_message)  # i added this
# # # dang_counter = 0
# # # clean_words = []
# # # words = [string.split() for string in messages]
# # # print("Words", words)

# # # for word_list in words:
# # #     if "dang" in word_list:
# # #         dang_counter += 1
# # #         clean_words = word_list.remove("dang")
# # #         print("Word List", word_list)
# # #         clean_message.append(clean_words)
# # #         print(clean_message)

# # # print("Bad words:", dang_counter)
# # # print(messages)


# # # filter_messages(messages)
# # ################################################################################
# # # def double_string(string):
# # #     doubled = ""
# # #     for char in string:
# # #         doubled += char * 2
# # #     return doubled


# # # # Don't touch below this line

# # # print(double_string("Hello there"))
# # # print(double_string("General Kenobi"))
# # # print(double_string("I've been trained in your Jedi arts"))
# # ################################################################################
# # # def is_prime(number):
# # #     if number < 2:
# # #         return False
# # #     for i in range(2, number):
# # #         if number % i == 0:
# # #             return False

# # #     return True

# # # # Don't touch below this line


# # # for i in range(0, 25):
# # #     print(f"{i} is prime: {is_prime(i)}")
# # ################################################################################
# # def test_score(answer_sheet, student_answers):
# #     count = 0
# #     percentage = 0.0
# #     name = student_answers[0]
# #     for i in range(len(answer_sheet)):
# #         if answer_sheet[i] == (student_answers[i + 1]):
# #             count += 1
# #     percentage = count / len(answer_sheet) * 100
# #     return name, percentage


# # # Don't touch below this line


# # def test(answer_sheet, student_1_answers):
# #     name, percentage = test_score(answer_sheet, student_1_answers)
# #     print(f"{name}: {percentage:.1f}%")


# # def main():
# #     answer_sheet = [
# #         "A",
# #         "A",
# #         "C",
# #         "D",
# #         "D",
# #         "B",
# #         "C",
# #         "A",
# #         "C",
# #         "B",
# #         "A",
# #         "D",
# #         "C",
# #         "B",
# #         "D",
# #         "C",
# #         "B",
# #         "A",
# #         "D",
# #         "A",
# #     ]
# #     student_1_answers = [
# #         "Allan",
# #         "A",
# #         "C",
# #         "C",
# #         "B",
# #         "D",
# #         "B",
# #         "C",
# #         "A",
# #         "C",
# #         "B",
# #         "A",
# #         "A",
# #         "C",
# #         "B",
# #         "D",
# #         "C",
# #         "B",
# #         "A",
# #         "D",
# #         "A",
# #     ]
# #     student_2_answers = [
# #         "John",
# #         "A",
# #         "D",
# #         "A",
# #         "A",
# #         "D",
# #         "A",
# #         "C",
# #         "B",
# #         "D",
# #         "A",
# #         "F",
# #         "A",
# #         "C",
# #         "B",
# #         "D",
# #         "C",
# #         "D",
# #         "C",
# #         "D",
# #         "A",
# #     ]
# #     student_3_answers = [
# #         "Jeremy",
# #         "A",
# #         "B",
# #         "D",
# #         "C",
# #         "D",
# #         "B",
# #         "D",
# #         "A",
# #         "C",
# #         "C",
# #         "D",
# #         "A",
# #         "C",
# #         "B",
# #         "D",
# #         "C",
# #         "B",
# #         "A",
# #         "F",
# #         "A",
# #     ]
# #     student_4_answers = [
# #         "Sally",
# #         "A",
# #         "A",
# #         "D",
# #         "A",
# #         "A",
# #         "B",
# #         "C",
# #         "A",
# #         "C",
# #         "B",
# #         "A",
# #         "A",
# #         "C",
# #         "B",
# #         "D",
# #         "C",
# #         "F",
# #         "A",
# #         "D",
# #         "A",
# #     ]
# #     student_5_answers = [
# #         "Tim",
# #         "A",
# #         "A",
# #         "C",
# #         "D",
# #         "D",
# #         "B",
# #         "C",
# #         "A",
# #         "C",
# #         "B",
# #         "A",
# #         "D",
# #         "C",
# #         "B",
# #         "D",
# #         "C",
# #         "B",
# #         "A",
# #         "D",
# #         "A",
# #     ]

# #     test(answer_sheet, student_1_answers)
# #     test(answer_sheet, student_2_answers)
# #     test(answer_sheet, student_3_answers)
# #     test(answer_sheet, student_4_answers)
# #     test(answer_sheet, student_5_answers)


# # main()


# # DICTIONARIES
# # ################################################################################
# def get_character_record(name, server, level, rank):
#     my_dictionary = {
#         "name": name,
#         "server": server,
#         "level": level,
#         "rank": rank,
#         "id": name + "#" + server,
#     }
#     return my_dictionary


# # Don't edit below this line


# def main():
#     rec = get_character_record("bloodwarrior123", "server1", 5, 1)
#     print_rec(rec)

#     rec = get_character_record("fronzenboi", "server2", 2, 1)
#     print_rec(rec)

#     rec = get_character_record("slasher69", "server3", 2, 5)
#     print_rec(rec)


# def print_rec(rec):
#     print(f"name: {rec['name']}")
#     print(f"server: {rec['server']}")
#     print(f"level: {rec['level']}")
#     print(f"rank: {rec['rank']}")
#     print(f"id: {rec['id']}")
#     print("---")


# main()


# #################################################################################
# def count_enemies(enemy_names):
#     jackal_count = 0
#     kobold_count = 0
#     soldier_count = 0
#     gremlin_count = 0

#     for enemy in enemy_names:
#         if enemy == "jackal":
#             jackal_count += 1
#         elif enemy == "kobold":
#             kobold_count += 1
#         elif enemy == "soldier":
#             soldier_count += 1
#         else:
#             gremlin_count += 1
#     enemies = {
#         "jackal": jackal_count,
#         "kobold": kobold_count,
#         "soldier": soldier_count,
#         "gremlin": gremlin_count,
#     }
#     # return jackal_count, kobold_count, soldier_count, gremlin_count
#     return enemies


# # Don't edit below this line


# def main():
#     print(
#         count_enemies(
#             [
#                 "jackal",
#                 "kobold",
#                 "jackal",
#                 "kobold",
#                 "soldier",
#                 "kobold",
#                 "soldier",
#                 "soldier",
#                 "jackal",
#                 "jackal",
#                 "gremlin",
#                 "jackal",
#                 "jackal",
#             ]
#         )
#     )


# main()
# # Ch 8
# #################################################################################
# {
#     "type": {
#         "student": {
#             "name": "Allan",
#             "courses": {
#                 "math_1050": {
#                     "current_grade": "B",
#                 },
#                 "English_1010": {
#                     "current_grade": "A-",
#                 },
#             },
#         }
#     }
# }


# def get_english_grade(student):
#     courses = student["type"]["student"]["courses"]
#     if "English_1010" in courses:
#         return courses["English_1010"]["current_grade"]
#     else:
#         return None


# def get_english_grade(student):
#     return student["type"]["student"]["courses"]["English_1010"]["current_grade"]


# #################################################################################
# def calculate_total(items_purchased, grocery_list):
#     unpurchased_items = [item for item in grocery_list if item not in items_purchased]

#     total = sum(grocery_list[item] for item in items_purchased)
#     return unpurchased_items, total


# # Don't touch below this line


# def test(items_purchased, grocery_list):
#     unpurchased_items, total = calculate_total(items_purchased, grocery_list)
#     print(f"You didn't purchase: {sorted(unpurchased_items)}")
#     print(f"You paid: ${total:.2f}")


# test(
#     [
#         "milk",
#         "eggs",
#         "bread",
#         "cheese",
#         "apples",
#         "bananas",
#         "lettuce",
#         "cereal",
#     ],
#     {
#         "milk": 2.50,
#         "eggs": 3.25,
#         "bread": 2.21,
#         "cheese": 3.50,
#         "apples": 4.44,
#         "bananas": 2.88,
#         "carrots": 3.89,
#         "lettuce": 1.12,
#         "potatoes": 6.21,
#         "cereal": 4.99,
#     },
# )

# test(
#     [
#         "milk",
#         "bread",
#         "cheese",
#         "lettuce",
#         "cereal",
#     ],
#     {
#         "milk": 2.50,
#         "eggs": 3.25,
#         "bread": 1.21,
#         "cheese": 3.50,
#         "apples": 7.44,
#         "bananas": 3.88,
#         "carrots": 3.89,
#         "lettuce": 1.12,
#         "potatoes": 32.21,
#         "cereal": 5.99,
#     },
# )

# test(
#     [
#         "milk",
#         "bread",
#         "lettuce",
#         "cereal",
#     ],
#     {
#         "milk": 12.50,
#         "eggs": 2.21,
#         "bread": 1.23,
#         "cheese": 3.50,
#         "apples": 73.44,
#         "bananas": 23.88,
#         "carrots": 13.89,
#         "lettuce": 12.12,
#         "potatoes": 2.21,
#         "cereal": 1.99,
#     },
# )


# # ################################################################################
# def find_missing_ids(first_ids, second_ids):
#     diff = list(first_ids)

#     for el in second_ids:
#         if el not in diff:
#             diff.remove(el)
#         return diff


# # Don't touch below this line


# def test(first_ids, second_ids):
#     ids = sorted(find_missing_ids(first_ids, second_ids))
#     print(f"Customers with these ids were only in the first list:")
#     for id in ids:
#         print(f"- {id}")
#     print("---")


# test([1, 1, 1, 2, 2, 2, 3], [1, 2])
# test([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8])
# test(
#     [1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 15, 18],
#     [1, 2, 2, 3, 4, 5, 6, 7, 8, 100, 101, 103],
# )


# # ################################################################################
# class Archer:
#     def __init__(self, num_arrows, health, name):
#         self.num_arrows = num_arrows
#         self.health = health
#         self.name = name

#     def get_shot(self):
#         if self.health >= 1:
#             self.health -= 1
#         else:
#             print(f"{self.name} is dead")

#     def shoot(self, target):
#         if self.num_arrows <= 0:
#             raise Exception(f"{self.name} can't shoot")
#         else:
#             self.num_arrows -= 1
#             print(f"{self.name} {target.name}")
#             target.get_shot()


# # don't touch below this line


# def main():
#     bard = Archer(1, 3, "Bard")
#     legolas = Archer(10000, 3, "Legolas")

#     while bard.health > 0 and legolas.health > 0:
#         try:
#             print_status(bard)
#             print_status(legolas)
#             bard.shoot(legolas)
#         except Exception as e:
#             print(e)

#         try:
#             print_status(bard)
#             print_status(legolas)
#             legolas.shoot(bard)
#         except Exception as e:
#             print(e)


# def print_status(archer):
#     print(f"{archer.name} has {archer.health} health and {archer.num_arrows} arrows")


# main()


# # ################################################################################
# CLASSES
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def remove_book(self, book):
#         if book in self.books:
#             self.books.remove(book)

#     def search_books(self, search_string):
#         search_list = []
#         for book in self.books:
#             if (
#                 search_string.lower() in book.title.lower()
#                 or search_string.lower() in book.author.lower()
#             ):
#                 search_list.append(book)
#         return search_list


# # don't touch below this line


# def test_library(library_name, book_names, book_authors):
#     library = Library(library_name)
#     print(f"Created library: {library_name}")
#     for i in range(len(book_names)):
#         book = Book(book_names[i], book_authors[i])
#         library.add_book(book)
#         print(f"Added book: {book.title} by {book.author}")
#     print(f"Books in {library_name}:")
#     for book in library.books:
#         print(f"- {book.title} by {book.author}")
#     book_to_remove = library.books[0]
#     library.remove_book(book_to_remove)
#     print(f"Removed book: {book_to_remove.title} by {book_to_remove.author}")
#     print("Books in library after removing a book:")
#     for book in library.books:
#         print(f"- {book.title} by {book.author}")

#     # Search for books
#     search_query = "kill"
#     search_results = library.search_books(search_query)
#     if len(search_results) == 0:
#         print(f"No results found for search query: {search_query}")
#     else:
#         print(f"Search results for query '{search_query}':")
#         for book in search_results:
#             print(f"- {book.title} by {book.author}")


# test_library(
#     "John's Library",
#     ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"],
#     ["J.D. Salinger", "Harper Lee", "George Orwell"],
# )
# test_library(
#     "Ashley's Library",
#     ["The Great Gatsby", "Pride and Prejudice", "The Lord of the Rings", "Song of Six"],
#     ["F. Scott Fitzgerald", "Jane Austen", "J.R.R. Tolkien", "Harper D Kill"],
# )
# # ################################################################################
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         self.__courses = {}  # private class variable

#     def calculate_letter_grade(self, score):
#         if score >= 90:
#             return "A"
#         elif score >= 80 and score < 90:
#             return "B"
#         elif score >= 70 and score < 79:
#             return "C"
#         elif score > 60 and score < 69:
#             return "D"
#         else:
#             return "F"

#     def add_course(self, course_name, score):
#         grade = self.calculate_letter_grade(score)
#         self.__courses[course_name] = grade

#     def get_courses(self):
#         return self.__courses


# # don't touch below this line


# def test(student_name, courses, scores):
#     student = Student(student_name, scores)
#     print(f"Student created: {student_name}")

#     for i, course in enumerate(courses):
#         student.add_course(course, scores[i])
#         print(f"Added course: {course} with score: {scores[i]}")
#     courses = student.get_courses()
#     for course in courses:
#         print(f"{student_name}'s grade in {course} is a {courses[course]}")
#     test_encapsulation(student)
#     print("=====================================")


# def test_encapsulation(student):
#     try:
#         print(student.__courses)
#     except:
#         print("Private data member is encapsulated properly")


# def main():
#     test("John Thorton", ["Math", "English", "History"], [85, 92, 76])
#     test("Jasper Allen", ["Science", "Social Studies"], [90, 88])
#     test(
#         "Bobby Christensen",
#         ["Physics", "Chemistry", "Biology", "Geology"],
#         [80, 78, 85, 90],
#     )


# main()
# # # # ################################################################################
# # # CALCULATOR
# # class Calculator:
# #     def __init__(self):
# #         self.__result = 0

# #     def add(self, a):
# #         self.__result += a

# #     def subtract(self, a):
# #         self.__result -= a

# #     def multiply(self, a):
# #         self.__result *= a

# #     def divide(self, a):
# #         if a == 0:
# #             raise ValueError("Cannot divide by zero")
# #         else:
# #             self.__result /= a

# #     def modulo(self, a):
# #         if a == 0:
# #             raise ValueError("Cannot divide by zero")
# #         else:
# #             self.__result %= a

# #     def power(self, a):
# #         self.__result **= a

# #     def square_root(self):
# #         self.__result **= 0.5

# #     def clear(self):
# #         self.__result = 0

# #     def get_result(self):
# #         return self.__result


# # # don't touch below this line


# # def test(starting_num):
# #     calculator = Calculator()
# #     calculator.add(starting_num)
# #     print(f"Starting number: {starting_num}")
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print(f"Adding 5...")
# #     calculator.add(5)
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print(f"Modulo 7...")
# #     calculator.modulo(7)
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print(f"Power 2...")
# #     calculator.power(2)
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print(f"Square root...")
# #     calculator.square_root()
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print(f"Subtracting 3...")
# #     calculator.subtract(3)
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print(f"Multiplying by 2...")
# #     calculator.multiply(2)
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print(f"Dividing by 6...")
# #     calculator.divide(6)
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print(f"Clearing...")
# #     calculator.clear()
# #     print(f"Result: {calculator.get_result():.2f}")
# #     print("=====================================")


# # def main():
# #     test(11.0)
# #     test(6.0)
# #     test(0.0)


# # main()
# # # ################################################################################
# # import random


# # class DeckOfCards:
# #     SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
# #     RANKS = [
# #         "Ace",
# #         "2",
# #         "3",
# #         "4",
# #         "5",
# #         "6",
# #         "7",
# #         "8",
# #         "9",
# #         "10",
# #         "Jack",
# #         "Queen",
# #         "King",
# #     ]

# #     def __init__(self):
# #         self.__cards = []
# #         self.create_deck()

# #     def create_deck(self):
# #         for suit in self.SUITS:
# #             for rank in self.RANKS:
# #                 card = (rank, suit)
# #                 self.__cards.append(card)

# #     def shuffle_deck(self):
# #         random.shuffle(self.__cards)

# #     def deal_card(self):
# #         if len(self.__cards) == 0:
# #             return None
# #         return self.__cards.pop(0)

# #     # don't touch below this line
# #     def __str__(self):
# #         return f"The deck has {len(self.__cards)} cards"


# # def test(deck):
# #     print(deck)
# #     print("Dealing a hand:")
# #     hand = []
# #     for i in range(5):
# #         card = deck.deal_card()
# #         if card is None:
# #             print("Out of cards!")
# #             break
# #         print(f" - {card[0]} of {card[1]}")
# #     print("=====================================")
# #     return deck


# # def main():
# #     random.seed(1)
# #     deck = DeckOfCards()
# #     deck.shuffle_deck()
# #     deck = test(deck)
# #     deck = test(deck)
# #     deck = test(deck)


# # main()
# # # ################################################################################
# # class Human:
# #     def __init__(self, name):
# #         self.__name = name

# #     def get_name(self):
# #         return self.__name


# # class Archer(Human):
# #     def __init__(self, name, num_arrows):
# #         super().__init__(name)
# #         self.__num_arrows = num_arrows

# #     def get_num_arrows(self):
# #         return self.__num_arrows

# #     def use_arrows(self, num):
# #         if self.__num_arrows < num:
# #             raise Exception("not enough arrows")
# #         self.__num_arrows -= num


# # class Crossbowman(Archer):
# #     def __init__(self, name, num_arrows):
# #         super().__init__(name, num_arrows)

# #     def triple_shot(self, target):
# #         self.use_arrows(3)
# #         print(f"{target.get_name()} was shot by 3 crossbow bolts")


# # # don't touch below this line


# # def main():
# #     try:
# #         print("creating an archer named Bard")
# #         human2 = Archer("Bard", 1)
# #         identify(human2)
# #         print(f"Bard has {human2.get_num_arrows()} arrows")

# #         print("creating a crossbowman named Sir Not-Appearing-In-This-Film")
# #         human3 = Crossbowman("Sir Not-Appearing-In-This-Film", 4)
# #         identify(human3)
# #         print(f"{human3.get_name()} has {human3.get_num_arrows()} arrows")
# #         print(f"{human3.get_name()} attempts to shoot {human2.get_name()}")
# #         human3.triple_shot(human2)
# #         print(f"{human3.get_name()} has {human3.get_num_arrows()} arrows")
# #         print(f"{human3.get_name()} attempts to shoot {human2.get_name()}")
# #         human3.triple_shot(human2)

# #     except Exception as e:
# #         print(e)


# # def identify(human):
# #     print(f"Getting name: {human.get_name()}")


# # main()
# # # ################################################################################
# class Hero:
#     def __init__(self, name, health):
#         self.__name = name
#         self.__health = health

#     def get_name(self):
#         return self.__name

#     def get_health(self):
#         return self.__health

#     def take_damage(self, damage):
#         self.__health -= damage


# # Create Archer class here
# class Archer(Hero):
#     def __init__(self, name, health, num_arrows):
#         super().__init__(name, health)
#         self.__num_arrows = num_arrows

#     def shoot(self, target):
#         if self.__num_arrows <= 0:
#             raise Exception("not enough arrows")
#         self.__num_arrows -= 1
#         target.take_damage(10)


# # don't touch below this line


# def main():
#     try:
#         print("Creating a hero named Hercules with 200 health")
#         human1 = Hero("Hercules", 200)
#         identify(human1)

#         print("creating an Archer named Pericles with 100 health and 2 arrows")
#         human2 = Archer("Pericles", 100, 2)
#         identify(human2)

#         while human1.get_health() > 0 and human2.get_health() > 0:
#             print(f"{human2.get_name()} attempts to shoot {human1.get_name()}")
#             human2.shoot(human1)
#             identify(human1)
#             identify(human2)

#     except Exception as e:
#         print(e)


# def identify(human):
#     print(f"Name: {human.get_name()}, health: {human.get_health()}")


# main()
# # ################################################################################
# def main():
#     dragons = [
#         Dragon("Green Dragon", 0, 0, 1),
#         Dragon("Red Dragon", 2, 2, 2),
#         Dragon("Blue Dragon", 4, 3, 3),
#         Dragon("Black Dragon", 5, -1, 4),
#     ]

#     # don't touch above this line

#     for dragon in dragons:
#         describe(dragon)
#     dragons_copy = dragons.copy()

#     for dragon in dragons:
#         dragons_copy.remove(dragon)
#         dragon.breathe_fire(3, 3, dragons_copy)
#         dragons_copy.append(dragon)


# # don't touch below this line


# def describe(dragon):
#     print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


# class Unit:
#     def __init__(self, name, pos_x, pos_y):
#         self.name = name
#         self.pos_x = pos_x
#         self.pos_y = pos_y

#     def in_area(self, x_1, y_1, x_2, y_2):
#         return (
#             self.pos_x >= x_1
#             and self.pos_x <= x_2
#             and self.pos_y >= y_1
#             and self.pos_y <= y_2
#         )


# class Dragon(Unit):
#     def __init__(self, name, pos_x, pos_y, fire_range):
#         super().__init__(name, pos_x, pos_y)
#         self.__fire_range = fire_range

#     def breathe_fire(self, x, y, units):
#         print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
#         for unit in units:
#             in_area = unit.in_area(
#                 x - self.__fire_range,
#                 y - self.__fire_range,
#                 x + self.__fire_range,
#                 y + self.__fire_range,
#             )
#             if in_area:
#                 print(f"{unit.name} is hit by the fire")


# main()

# # ################################################################################
# import math


# def get_influencer_score(num_followers, average_engagement_percentage):
#     influencer_score = average_engagement_percentage * math.log(num_followers, 2)
#     return influencer_score


# # don't touch below this line


# def test(num_followers, average_engagement_percentage):
#     influencer_score = round(
#         get_influencer_score(num_followers, average_engagement_percentage)
#     )
#     print(f"- num_followers: {num_followers}")
#     print(f"- average_engagement_percentage: {average_engagement_percentage}")
#     print(f"Influencer score: {influencer_score}")
#     print("====================================")


# def main():
#     test(40000, 0.3)
#     test(43000, 0.1)
#     test(100000, 0.6)
#     test(200, 0.8)


# main()
# # ################################################################################
# def decayed_followers(intl_followers, percent_lost_daily, days):
#     return intl_followers * (1 - percent_lost_daily) ** days


# # don't touch below this line


# def test(intl_followers, percent_lost_daily, days):
#     final_value = round(decayed_followers(intl_followers, percent_lost_daily, days))
#     print(f"- Initial followers: {intl_followers}")
#     print(f"- Decay rate: {percent_lost_daily}")
#     print(f"- Days: {days}")
#     print(f"Final followers: {final_value}")
#     print("=====================================")


# def main():
#     test(200, 0.5, 1)
#     test(200, 0.5, 2)
#     test(200, 0.5, 3)

#     test(1000, 0.005, 2)
#     test(1000, 0.05, 3)

#     test(1200, 0.55, 8)
#     test(1200, 0.09, 16)


# main()
# # #####################################################################################

# import math


# def log_scale(data, base):
#     new_list = []
#     for num in data:
#         new = math.log(num, base)
#         new_list.append(new)
#     return new_list


# # don't touch below this line


# def test(data, base):
#     scaled_data = log_scale(data, base)
#     for i in range(0, len(scaled_data)):
#         scaled_data[i] = round(scaled_data[i], 2)

#     print(f"- Data: {data}")
#     print(f"- Base: {base}")
#     print(f"Scaled data: {scaled_data}")
#     print("=====================================")


# def main():
#     test([1, 10, 100, 1000], 10)
#     test([1, 2, 4, 8, 16], 2)
#     test([100, 1000, 10000], 4)


# main()


# # #####################################################################################
# def does_name_exist(first_names, last_names, full_name):
#     for first_name in first_names:
#         for last_name in last_names:
#             if first_name + " " + last_name == full_name:
#                 return True
#     return False


# don't touch below this line


# def test(first_names, last_names, full_name):
#     res = does_name_exist(first_names, last_names, full_name)
#     print(f"- num first_names: {len(first_names)}")
#     print(f"- num last_names: {len(last_names)}")
#     print(f"- full_name: {full_name}")
#     print(f"Name exists: {res}")
#     print("====================================")


# def main():
#     test(get_first_names(100), get_last_names(100), "bob0 gonzalez0")
#     test(get_first_names(500), get_last_names(500), "bob0 smith1")
#     test(get_first_names(1000), get_last_names(1000), "bob500 smith6")
#     test(get_first_names(2000), get_last_names(2000), "bob1999 wagner1998")
#     test(get_first_names(3000), get_last_names(3000), "sally2999 smith2998")


# def get_first_names(num):
#     names = []
#     for i in range(num):
#         m = i % 3
#         if m == 0:
#             names.append(f"bob{i}")
#         elif m == 1:
#             names.append(f"maria{i}")
#         if m == 2:
#             names.append(f"sally{i}")
#     return names


# def get_last_names(num):
#     names = []
#     for i in range(num):
#         m = i % 3
#         if m == 0:
#             names.append(f"gonzalez{i}")
#         elif m == 1:
#             names.append(f"smith{i}")
#         if m == 2:
#             names.append(f"wagner{i}")
#     return names


# main()

# # #####################################################################################
# import time


# def binary_search(target, arr):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#     while low <= high:
#         mid = (high + low) // 2
#         # if target is greater, ignore left half
#         if arr[mid] < target:
#             low = mid + 1
#         # if target is smaller, ignore right half
#         elif arr[mid] > target:
#             high = mid - 1
#         # means target is present at mid
#         else:
#             return True
#     if low < len(arr) and arr[low] == target:
#         return True
#     else:
#         return False


# # don't touch below this line


# def benchmark(names_dict, first_name):
#     start = time.time()
#     test(names_dict, first_name)
#     end = time.time()

#     timeout = 0.05

#     if (end - start) < timeout:
#         print(f"test completed in less than {timeout * 1000} milliseconds!")
#     else:
#         print(f"test took too long ({(end - start) * 1000} milliseconds). Speed it up!")
#     print("====================================")


# def test(target, arr):
#     res = binary_search(target, arr)
#     print(f"- len arr: {len(arr)}")
#     print(f"- target: {target}")
#     print(f"Result: {res}")
#     print("------------------------------------")


# def main():
#     complexity = 2000000
#     nums = get_nums(complexity)
#     benchmark(int(complexity * 0.2344), nums)
#     benchmark(int(complexity * 2), nums)
#     benchmark(int(complexity + 1), nums)
#     benchmark(int(complexity * 0.765), nums)


# def get_nums(num):
#     nums = []
#     for i in range(num):
#         nums.append(i)
#     return nums


# main()
# # #####################################################################################
# def exponential_growth(n, factor, days):
#     growth = []
#     growth.append(n**factor**days)
#     return growth


# # don't touch below this line


# def test(n, factor, days):
#     growth_sequence = exponential_growth(n, factor, days)
#     print(f"- Initial followers: {n}")
#     print(f"- Growth factor: {factor}")
#     print(f"- Days: {days}")
#     print(f"Growth sequence: {growth_sequence}")
#     print("=====================================")


# def main():
#     test(10, 2, 4)
#     test(20, 2, 6)
#     test(30, 3, 3)
#     test(40, 10, 10)


# main()
# # #####################################################################################
# TSP problem
# import random


# def tsp(cities, paths, dist):
#     all_paths = permutations(cities)

#     for path in all_paths:
#         total_distance = 0
#         for i in range(len(path) - 1):
#             cityA = path[i]
#             cityB = path[i + 1]
#             total_distance += paths[cityA][cityB]

#         if total_distance < dist:
#             return True
#     return False


# # #####################################################################################
# codewar - easy 8 kyu
# def string_to_number(s):
#     number = int(s)
#     return number
#     pass
# # #####################################################################################
# code war- medium
# return a list of the first n multiples of x
# def count_by(x, n):
#     multiples = [x * i for i in range(1, n + 1)]
#     return multiples


# # #####################################################################################
# 8kyu kata
def past(h, m, s):
    hours = h * 3.6e6
    minutes = m * 60000
    seconds = s * 1000
    return hours + minutes + seconds
