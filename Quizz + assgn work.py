# print("hello")


# # coding exercise 17

# # Declare a nested_extraction function that accepts a list of lists and an index position.
# #
# # The function should use the index as the basis of finding both the nested list 
# # and the element from that list with the given index position
# #
# # You can assume the number of lists will always be equal to 
# # the number of elements within each of them.
# #
# # nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# # nested_extraction(nl, 0)  => 3
# # nested_extraction(nl, 1)  => 8
# # nested_extraction(nl, 2)  => 12

# def nested_extraction(elements, index):
#     return elements[index][index]
# ------------------------------------------------------------------------
# # Declare a beginning_and_end function that accepts a list of elements.
# #
# # It should return True if the first and last elements in the list are equal and False if they are unequal.
# #
# # Assume the list will always have at least 1 element.
# #
# # beginning_and_end([1, 2, 3, 1])     => True
# # beginning_and_end([1, 2, 3, 4, 5])  => False
# # beginning_and_end(["a", "b", "a"])  => True
# # beginning_and_end([15])             => True


# def beginning_and_end(elements):
#     return elements[0] == elements[-1]

#------------------------------------------------------------------------------




# # Declare a long_word_in_collection function that accepts a list and a string. 
# # The function should return True if 
# #   - the string exists in the list AND
# #   - the string has more than 4 characters.
# #
# # words = ["cat", "dog", "rhino"]
# # long_word_in_collection(words, "rhino")  => True
# # long_word_in_collection(words, "cat")    => False
# # long_word_in_collection(words, "monkey") => False

# def Long_word_in_collection(elements, target):
#     return target in elements and len(target) > 4
#-------------------------------------------------------------
# # 18

# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

# def sum_of_lenght(strings):
#      total = 0
#      for string in strings:
#         total += len(string)
#      return total
        
# #--------------------------------------------------------------------------
    
# # Define a product function that accepts a list of numbers.
# # The function should return the product of the numbers.
# # The list will always have at least one value
# #
# # EXAMPLES
# # product([1, 2, 3])     => 6
# # product([4, 5, 6, 7])  => 840
# # product([10])          => 10

# def product(numbers):
#     total = 0
#     for number in numbers:
#         total *= len(number)

#-----------------------------------------------------------------------

# #

# songs = ["Proven", "Perseverance", "Defeatist", "Puritan"]
# songs[1:3] = ["I Will Be Heard"]
# print(songs)

# units_of_measurement = ["miles", "meters", "yards"]
# units_of_measurement = units_of_measurement.reverse()
# print(units_of_measurement)

# spices = ["paprika", "nutmeg", "ginger", "cinnamon", "turmeric"]
# spices.append(["garlic", "berbere", "sansho"])
# print(spices)

#------------------------------------------------------------------------
# ASS 15


# What’s the difference between the pop and remove methods?

# The pop() methos use the index of a element to delete it while the remove() take the value
#  of the element as an input argument to delete the element as# Given a list



# numbers = [1, 4, 5, 7, 9]
# numbers.remove(4)
# numbers.remove(5)

# numbers.insert(1, 6)
# numbers.insert(2, 8)

# print(numbers)

# Borris solution
# numbers = [1, 4, 5, 7, 9]

# how can you overwrite the values 4 and 5 with 6 and 8?

# Provide the code below.

# numbers[1:3] = [6, 8]

# numbers = [1, 4, 5, 7, 9]

# how can you overwrite the values 4 and 5 with 6 and 8?

# Provide the code below.

# What do the two arguments to the insert method represent?

# What does it mean for an object to be mutable?
# ------------------------------------------------------------------------------

# quiz 18

# print("heartless".count("e"))
# print([3, 5, 7, 5, 3, 1, 5].count(5))
# print([True, True, True, False].index(True))
# print([True, True, True, False, True].index(True, 2))

# quote = "Four score and seven years ago"
# words_of_wisdom = quote.split(" ")
# print(words_of_wisdom)


# print("!".join(["Who", "let", "the", "dogs", "out?"]))

# for a, b, c in zip([3, 2, 1], [1, 2, 3], [2, 3, 1]):
#   print("*-*".join([str(a), str(b), str(c)]))

#--------------------------------------------------------------------------------

# # quiz 19
# lotto = [
#   [10, 5, 8],
#   [8, 5, 10],
#   [10, 8, 5]
# ]
 
# print(lotto[-3])
# lotto = [
#   [10, 5, 8],
#   [8, 5, 10],
#   [10, 8, 5]
# ]
 
# print(lotto[-2][-2])
# lotto = [
#   [10, 5, 8],
#   [8, 5, 10],
#   [10, 8, 5]
# ]
 
# lotto[-3][3]

# lotto = [
#   [10, 5, 8],
#   [8, 5, 10],
#   [10, 8, 5]
# ]
 
# for el in lotto:
#   for value in el:
#     print(value)
# -------------------------------------------------------------------------------------
# assgn 16



# print(max(["A", "a", "Z", "z"]))

# # print(min(["A", "a", "Z", "z"]))
# # print(all(["A", "a", "Z", "z"]))
# print(any(["", "A", "a", "Z", "z"]))
# print(map(lambda val: val.swapcase(), ["Secret", "gARDEN", "GeNiUs"]))
# print(list(filter(lambda val: val.islower(), ["guybrush", "Threepwood", "LeChuck", "elaine"])))

# --------------------------------------------------------------------------------------------------

# # 21 + assgn 17


# qualities = ("Determination", "Grit", "Perseverance", "Optimism", "Excitement")
 
# traits, *skills = qualities
# print(skills)

# qualities = ("Determination", "Grit", "Perseverance", "Optimism", "Excitement")
 
# traits, *skills, characteristics = qualities
# print(skills)

# qualities = ("Determination", "Grit", "Perseverance", "Optimism", "Excitement")
 
# *skills, traits = qualities
# print(skills)

# def larger_number(one, two):
#   if one > two:
#     return one
#   else:
#     return two
 
# values = [5, 3]
# print(larger_number(values))

# ingredients = ("Chicken", "Beef", "Cumin", 375, 30)

# *meats, spice, temperature, cooking_time = ingredients
# print(meats)        # ['Chicken', 'Beef']
# print(spice)        # Cumin
# print(temperature)  # 375
# print(cooking_time) # 30

# ---------------------------------------------------------------------------------

# 22-19

# mystery = ["A", "B"]
# enigma = ["A", "B"]
# print(mystery == enigma)
# print(mystery is enigma)

# toppings = ["Mushrooms", "Onions"]
# cheesesteak = ["Steak", toppings, "Cheese"]
 
# dinner = cheesesteak
# toppings.append("Peppers")
 
# print(dinner)

# pizza = ["Crust", "Tomato Sauce", "Cheese"]
# lunch = pizza
# breakfast = ["Crust", "Tomato Sauce", "Cheese"]
 
# print(pizza is lunch)
# print(lunch is breakfast)

# web_dev = ["HTML", "CSS", "JavaScript"]

# frontend = web_dev



# web_dev.append("React")

# print(frontend)
# ------------------------------------------------------------------------
# 23
# sodas = {
#   "Pepsi": 41,
#   "Coke": 39,
#   "Sprite": 44,
# }

# print(sodas["coke"])

# confusion = {
#   "a": "b",
#   "b": "c",
#   "c": "d"
# }
 
# value = del confusion["b"]
# print(confusion)

# d1 = {

#   "a": 5,

#   "b": 10,

#   "c": 5

# }

# d2 = {

#   "a": 8,

#   "b": 12,

#   "d": 16

# }

# (d1.update(d2))
# print(d1)

# nba_finals = {

#   "Game 1": {

#     "date": "05/05/2019",

#     "location": "San Francisco",

#     "statistics": {

#       "points": 200,

#       "rebounds": 20,

#       "assists": 25

#     }

#   }

# }

# print(nba_finals["Game 1"]["statistics"]["rebounds"])

# my_dict = {

#   "a": {

#     1: 2,

#     3: 4,

#     5: {

#       6: 7,

#       8: 9

#     }

#   }

# }

# mystery = {

#   "a": 2

# }



# print(mystery.setdefault("A", 5))

# print(mystery.setdefault("a", 10))

# print(mystery.setdefault("B", 30))

# print(mystery.setdefault("B", 40))

# print(mystery)

#------------------------------------------------------------------------------------------

#quiz 24

# def my_func(a, b, *args, **kwargs):
#   print(kwargs)
 
# my_func(b = 5, a = 10, c = 15)

# def my_func(a, b, *args, **kwargs):
#   print(kwargs)
 
# my_func(20, 30, 40, 50)

# -------------------------------------------------------------------------------------
# quiz 25

# sentences = [
#   "Bobby went to the store on the corner",
#   "Sally ate a candy bar",
#   "Justin played on his deluxe piano"
# ]
 
# word_counts = { sentence: len(sentence.split(" ")) for sentence in sentences }
# print(word_counts)

# values = [1, 2, 3, 4, 5]
# print({ value: sum(values[:index + 2]) for index, value in enumerate(values) })

# prices = {
#   "Big Mac": 3.99,
#   "French Fries": 0.99,
#   "Soda": 0.99
# }
 
# calories = 
#   "Big Mac": 600,
#   "French Fries": 300,
#   "Soda": 200
# }
 
# cheap_options =
 
# print(cheap_options) # {'French Fries': 300, 'Soda': 200}
# ----------------------------------------------------------------

# assi21


# values = [0, 0.0, "0.0"]
# print(set(values))

# pages = { 10, 20, 30 }
# element = pages.remove(30)
# print(element)

# pages = { 10, 20, 30 }
# pages.add([30, 40, 50])


# print(set("zyx"))

gatorade_flavors = { "blue", "red", "orange" }
powerade_flavors = { "red", "green", "yellow" }
 
print(gatorade_flavors.intersection(powerade_flavors))

gatorade_flavors = { "blue", "red", "orange" }
powerade_flavors = { "red", "green", "yellow" }
 
print(gatorade_flavors.difference(powerade_flavors))

juice_flavors = { "Lemon", "Peach", "Raspberry", "Apple" }
tea_flavors = { "Peach", "Grape", "apple" }
 
print(juice_flavors & tea_flavors)

juice_flavors = { "Lemon", "Peach", "Raspberry", "Apple" }
tea_flavors = { "Peach", "Grape", "apple" }
print(juice_flavors - tea_flavors)

