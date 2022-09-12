# code #2 

# season = "fALL"

# SEASON = "Fall"
# lucky_number = "3"
# hard_math = 3 + 4 + 5
# my_str = "3"
# my_num = int(3)
# fancy_name = "Luc Clavet"
# print(fancy_name)


# -------------------------------------------------------


# # code exercise 3

# # Define a easy_money function that accepts no parameters 
# # and always returns the value 100.

   


# # Define a best_food_ever function that accepts 
# # no parameters and always returns the string “Sushi”.




# # Define a convert_to_currency function that accepts a single parameter (an integer). 
# # The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# # 
# # EXAMPLES:
# # convert_to_currency(15)    => "$15"
# # convert_to_currency(8)     => "$8"


#---------------------------------------------------------------------

# code 4
#-1


# print(string_adder("Hello", "World"))      
# print(string_adder("Emilio", "Estevez"))   
# print(string_adder())                      
# print(string_adder("Tiger"))               


#     #-2 



# print(multiplier(2, 2, 2))    
# print(multiplier())          
# print(multiplier(3))         
# print(multiplier(2, 5))      

#-------------------------------------------------------------------------------

# code exercise 5
# -1
# Define a long_word function that accepts a string. 
# The function should return a Boolean that reflects whether the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True



# print(Long_word("Python"))        # => False
# print(Long_word("magnificent"))    #=> True


#     #-2

# # Define a first_longer_than_second function that accepts two string arguments. 
# # The function should return a True if the first string is longer than the second 
# # and False otherwise (including if they are equal in length).
# #





# print(first_longer_than_second("Python", "Ruby"))     #=> True
# print(first_longer_than_second("cat", "mouse"))     #  => False
# print(first_longer_than_second("Steven", "Seagal"))  # => False

#------------------------------------------------------------------------------
#code 6


#-1

# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#






# # EXAMPLES:
# print(same_first_and_last_letter("runner"))  # => True
# print(same_first_and_last_letter("Runner"))   #=> False
# print(same_first_and_last_letter("clock"))    #> False
# print(same_first_and_last_letter("q"))       #=> True




# #-2

# # Define a three_number_sum function that accepts a 3-character string as an argument. 
# # The function should add up the sum of the digits of the string. 
# # HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
# #






# # EXAMPLES:
# print(three_number_sum("123"))  # => 6
# print(three_number_sum("567"))  # => 18
# print(three_number_sum("444"))  # => 12
# print(three_number_sum("000"))  # => 0

#--------------------------------------------------------------------------------

# code 7 -1

# # Define a first_three_characters function that accepts a string argument.
# # The function should return the first 3 characters of the string.
# #


# # EXAMPLES:
# print(first_three_characters("dynasty"))  # => "dyn"
# print(first_three_characters("empire"))    #=> "emp"

# #-2

# # Define a last_five_characters function that accepts a string argument. 
# # The function should return the last 5 characters of the string.
# #



# # EXAMPLES:
# print(last_five_characters("dynasty"))   #=> "nasty"
# print(last_five_characters("empire"))   # => "mpire"

# #-3

# # Define a is_palindrome function that accepts a string argument. 
# # The function should return True if the string is spelled 
# # the same backwards as it is forwards. 
# # Return False otherwise.
# #




# # EXAMPLES:
# print(is_palindrome("racecar"))   #=> True
# print(is_palindrome("yummy"))    # => False

#--------------------------------------------------------------------

#code 8 -1

# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#



# # EXAMPLES:
# print(vowel_count("estate"))       # => 3
# print(vowel_count("helicopter"))   # => 4
# print(vowel_count("ssh"))          # => 0


# -2

# # Define a find_my_letter function that accepts two arguments: a string and a character
# # The function should return the first index position of the character in the string
# # The function should return a -1 if the character does not exist in the string
# #



# # EXAMPLES:
# print(find_my_letter("dangerous", "a"))   # => 1
# print(find_my_letter("bazooka", "z"))     # => 2
# print(find_my_letter("lollipop", "z"))     #=> -1

#------------------------------------------------------------------------------------

# code 9-1

# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurrence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).
#





# print(fancy_cleanup("       geronimo crikey  "))  # => "zeronimo!crikey"
# print(fancy_cleanup("       nonsense  "))          #=> "nonsense"
# print(fancy_cleanup("grade"))                     # => "zrade"

#--------------------------------------------------------------------------------

#code 10-1

# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#




# print(even_or_odd(2))    #=> "even"
# print(even_or_odd(0))  #  => "even"
# print(even_or_odd(13))   #=> "odd"
# print(even_or_odd(9))   # => "odd"

# #-2

# # Define a truthy_or_falsy function that accepts a single argument.
# # The function should return a string that reads "The value _____ is ______" 
# # where the first space is the argument and the second space 
# # is either 'truthy' or 'falsy'. See the sample invocations below.
# # 




# print(truthy_or_falsy(0))       # => "The value 0 is falsy"
# print(truthy_or_falsy(5))       # => "The value 5 is truthy"
# print(truthy_or_falsy("Hello")) # => "The value Hello is truthy"
# print(truthy_or_falsy(""))      # => "The value  is falsy"

#----------------------------------------------------------------------------------

# code #11-1

# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
                          # always give a positive






# print(negative_energy(5))   # => 5
# print(negative_energy(10))   #=> 10
# print(negative_energy(-8))   #=> 8
# print(negative_energy(0))   # => 0
#--------------------------------------------------------------------------

# code #12-1

# Define a divisible_by_three_and_four function that accepts a number as its argument. 
# It should return True if the number is evenly divisible by both 3 and 4 . 
# It should return False otherwise.
#


   



# print(divisible_by_three_and_four(3))   #=> False
# print(divisible_by_three_and_four(4))   #=> False
# print(divisible_by_three_and_four(12))  #=> True
# print(divisible_by_three_and_four(18))  #=> False
# print(divisible_by_three_and_four(24))  #=> True

# # -2

# # Declare a string_theory function that accepts a string as an argument. 
# # It should return True if the string has more than 3 characters 
# # and starts with a capital “S”. It should return False otherwise.
# #





# print(string_theory("Sansa")) #=> True
# print(string_theory("Story")) #=> True
# print(string_theory("See")) #=> False
# print(string_theory("Fable")) #=> False
#------------------------------------------------------------------------------

# code  # 13-1

# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number. 
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops. 
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
#





# print(factorial(1)) #=> 1
# print(factorial(2)) #=> 2
# print(factorial(3))# => 6
# print(factorial(4)) #=> 24
# print(factorial(5)) #=> 120
#----------------------------------------------------------------------
#code #14-1

# Create an empty list and assign it to the variable "empty".


# Create a list with a single Boolean — True — and assign it to the variable "active".


# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".


# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".


# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise

#----------------------------------------------------------------------------------------------

#code # 15-1

# Define a first_and_last function that accepts a list of strings. 
# The function should return a concatenation of the first element and the last element. 
# Assume the list will always have 1 or more elements.
#





# print(first_and_last(["a", "b", "c"]))       # => "ac"
# print(first_and_last(["bob", "tom", "rob"])) # => "bobrob"
# print(first_and_last(["a"]))                  #=> "aa"

# # -2

# # Define a product_of_even_indices function that accepts a list of numbers. 
# # The list will always have 6 total elements. 
# # The function should return the product (multiplied total) of all numbers at an even index (0, 2, 4).
# #


 

# print(product_of_even_indices([1, 2, 3, 4, 5, 6]))  # =>  15
# print(product_of_even_indices([3, 4, 3, 5, 3, 6]))  # =>  27

# #-3

# # Define a first_letter_of_last_string function that accepts a list of strings. 
# # It should return one character — the first letter of the last string in the list. 
# # Assume the list will always have at least one string.
# #





# print(first_letter_of_last_string(["cat", "dog", "zebra"])) # => "z"
# print(first_letter_of_last_string(["nonsense"])) #=> "n"
#------------------------------------------------------------------------------
# code # 16 - 1

# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#




# # EXAMPLE:
# values = ["a", "b", "c", "d", "e", "f"]
# print(split_in_two(values, 3))    # => ["a", "b"]
# print(split_in_two(values, 4))    # => ["c", "d", "e", "f"]
# print(split_in_two(values, 1))    # => ["a", "b"]
# print(split_in_two(values, 10))   # => ["c", "d", "e", "f"]
#----------------------------------------------------------------------------
#code 17 - 1
# Declare a nested_extraction function that accepts a list of lists and an index position.
#
# The function should use the index as the basis of finding both the nested list 
# and the element from that list with the given index position
#
# You can assume the number of lists will always be equal to 
# the number of elements within each of them.
#





# nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# print(nested_extraction(nl, 0))  #=> 3
# print(nested_extraction(nl, 1))  #=> 8
# print(nested_extraction(nl, 2))  #=> 12

# #-2

# # Declare a beginning_and_end function that accepts a list of elements.
# #
# # It should return True if the first and last elements in the list are equal and False if they are unequal.
# #
# # Assume the list will always have at least 1 element.
# #





# print(beginning_and_end([1, 2, 3, 1]))     #=> True
# print(beginning_and_end([1, 2, 3, 4, 5]))  #=> False
# print(beginning_and_end(["a", "b", "a"]))  #=> True
# print(beginning_and_end([15]))            # => True

# # -3

# # Declare a long_word_in_collection function that accepts a list and a string. 
# # The function should return True if 
# #   - the string exists in the list AND
# #   - the string has more than 4 characters.
# #







# words = ["cat", "dog", "rhino"]
# print(long_word_in_collection(words, "rhino")) # => True
# print(long_word_in_collection(words, "cat"))   # => False
# print(long_word_in_collection(words, "monkey")) #=> False
#-----------------------------------------------------------------------------------------

#code 18 - 1

# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#






# # EXAMPLES
# print(sum_of_lengths(["Hello", "Bob"]))                 # => 8
# print(sum_of_lengths(["Nonsense"]))                     # => 8
# print(sum_of_lengths(["Nonsense", "or", "confidence"])) # => 20


# -2

# # Define a product function that accepts a list of numbers.
# # The function should return the product of the numbers.
# # The list will always have at least one value
# #





# # EXAMPLES
# print(product([1, 2, 3]))     #=> 6
# print(product([4, 5, 6, 7]))  #=> 840
# print(product([10]))          #=> 10

#----------------------------------------------------------------------------

#code 19 -1

# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#



# print(smallest_number([1, 2, 3]))    # => 1
# print(smallest_number([3, 2, 1]))    # => 1
# print(smallest_number([4, 5, 4]))     #=> 4
# print(smallest_number([-3, -2, -1]))  #=> -3

# # - 2

# # Define a concatenate function that accepts a list of strings. 
# #
# # The function should return a concatenated string which consists of
# # all list elements whose length is greater than 2 characters.
# #





# print(concatenate(["abc", "def", "ghi"]))      #=> "abcdefghi"
# print(concatenate(["abc", "de", "fgh", "ic"])) #=> "abcfgh"
# print(concatenate(["ab", "cd", "ef", "gh"]))  # => ""

# # - 3

# # Define a super_sum function that accepts a list of strings. 
# # The function should sum the index positions of the first occurence of the letter “s” in each word. 
# #
# # Not every word is guaranteed to have an “s”.
# # Don’t use "sum" as a variable name as it’s a built-in keyword.
# #




# print(super_sum([]))                                # => 0
# print(super_sum(["mustache"]))                     #  => 2
# print(super_sum(["mustache", "greatest"]))         #  => 8
# print(super_sum(["mustache", "pessimist"]))        #  => 4
#----------------------------------------------------------------------------------------


#code 20 -1

# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#




# # EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# print(in_list(strings, "enchanted"))  #==> 0
# print(in_list(strings, "sparks fly"))# ==> 1
# print(in_list(strings, "fifteen"))   # ==> -1
# print(in_list(strings, "love story"))# ==> -1

# # -2

# # Define a sum_of_values_and_indices function that accepts a list of numbers. 
# # It should return the sum of all of the elements along with their index values.
# #



# # EXAMPLES
# print(sum_of_values_and_indices([1, 2, 3]))    #=> (1 + 0) + (2 + 1) + (3 + 2) => 9
# print(sum_of_values_and_indices([0, 0, 0, 0])) #=> 6
# print(sum_of_values_and_indices([]))           #=> 0
#--------------------------------------------------------------------------------------

#code 21- 1


# # Given the great_directors list below, overwrite the “Steven Spielberg” string with a string of “Michael Bay”.
# great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]



# # Given the transformers list below, overwrite “Bumblebee” with “Grimlock”.
# transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]
# transformers[2] = "Grimlock"
# print(transformers)

# # Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
# camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]


# # Given the tech_companies list below, overwrite the Microsoft, Blueberry, and IBM strings 
# # with the strings “Facebook” and “Apple”. Use list slicing syntax.
# tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]

#-------------------------------------------------------------------------------------------
#code 22 -1

# Declare a Length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#




#     # EXAMPLES
# print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))  #=> 2
# print(length_match(["cat", "dog", "kangaroo", "mouse"], 5)) # => 1
# print(length_match(["cat", "dog", "kangaroo", "mouse"], 4)) # => 0
# print(length_match([], 5))                                  # => 0

# #-2
# # Declare a sum_from function that accepts two numbers as arguments.
# # The second number will always be greater than the first number.
# # The function should return the sum of all numbers from the first number to the second number (inclusive).




# # EXAMPLES
# print(sum_from(1, 2))   # 1 + 2                  => 3
# print(sum_from(1, 5))   # 1 + 2 + 3 + 4 + 5      => 15
# print(sum_from(3, 8))   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# print(sum_from(9, 12))  # 9 + 10 + 11 + 12       => 42

# # - 3

# # Declare a same_index_values function that accepts two lists.
# # The function should return a list of the index positions in which the two lists have equal elements


# # EXAMPLES
# print(same_index_values([1, 2, 3], [3, 2, 1]))                        # => [1]
# print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))  # => [1, 3]

#-------------------------------------------------------------------------------------------------
# # code 23 -1
# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#


      


# # EXAMPLES
# print(only_evens([4, 8, 15, 16, 23, 42])) #=> [4, 8, 16, 42]
# print(only_evens([1, 3, 5]))             # => []
# print(only_evens([]))                     #=> []

# #- 2

# # Define a long_strings function that accepts a list of strings. 
# # It should return a new list consisting of only the strings that have 5 characters or more.



# # EXAMPLES
# print(long_strings(["Hello", "Goodbye", "Sam"])) # => ["Hello", "Goodbye"]
# print(long_strings(["Ace", "Cat", "Job"]))       # => []
# print(long_strings([]))                          # => []
# #-------------------------------------------------------------------------------------
# #code 24 -1

# #code 24 -1
# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#




# # EXAMPLES
# print(factors(1))  #=> [1]
# print(factors(2))  #=> [1, 2]
# print(factors(10)) #=> [1, 2, 5, 10]
# print(factors(64)) #=> [1, 2, 4, 8, 16, 32, 64]
# #------------------------------------------------------------------------------
# #code 25 -1

# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# def delete_all(items, target):
#     while target in items:
#         items.remove(target)
#     return items


# # EXAMPLES
# print(delete_all([1, 3, 5], 3)) # => [1, 5]
# print(delete_all([5, 3, 5], 5))  #=> [3]
# print(delete_all([4, 4, 4], 4))  #=> []
# print(delete_all([4, 4, 4], 6)) # => [4, 4, 4]

# -2

# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list
#



# # EXAMPLES
# print(push_or_pop([10]))            #=> [10]
# print(push_or_pop([10, 4]))         #=> []
# print(push_or_pop([10, 20, 30]))   # => [10, 20, 30]
# print(push_or_pop([10, 20, 2, 30])) # => [10, 30]
#-------------------------------------------------------------------------------

# #code 26-1

# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# def encrypt_message(values)










# # # EXAMPLES
# print(encrypt_message("abc")) #=> "cde"
# print(encrypt_message("xyz"))  # => "zab"
# print(encrypt_message(""))     #    => ""
#-------------------------------------------------------------------------------
#code 27 -1

# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#



# EXAMPLES
# print(word_lengths("Mary Poppins was a nanny"))  #=> [4, 7, 3, 1, 5]
# print(word_lengths("Somebody stole my donut"))   #=> [8, 5, 2, 5]

# -2

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#



    



# print(cleanup(["cat", "er", "pillar"]))           #=> "cat er pillar"
# print(cleanup(["cat", " ", "er", "", "pillar"]))  #=> "cat er pillar"
# print(cleanup(["", "", " "]))    

# --------------------------------------------------------------------------------------------
# Code 28 -1

# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#




    




# # EXAMPLES
# print(nested_sum([[1, 2, 3], [4, 5]]))           # => 15
# print(nested_sum([[1, 2, 3], [], [], [4], [5]])) # => 15
# print(nested_sum([[]]))                          # => 0

# # -2

# # Define a fancy_concatenate function that accepts a list of lists of strings
# # The function should return a concatenated string
# # The strings in a list should only be concatenated if the length of the list is 3
# #




# # EXAMPLES
# print(fancy_concatenate([["A", "B", "C"]]))                       # => "ABC"
# print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]))      # => "ABCDEF"
# print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])) # => "ABC"
# print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))           # => "ABC"
# print(fancy_concatenate([["A", "B"], ["C", "D"]]))                # => ""

# -----------------------------------------------------------------------------------------
# code 29 -1

# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values 
# for each string in the values list.
# values = ["3.14", "9.99", "567.324", "5.678"]



# # The letters variable should store a list of 5 strings. 
# # Each of the strings should be a character from name concatenated together 3 times.
# # i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
# name = "Boris"


# # The 'lengths' list should store a list with the lengths
# # of each string in the 'elements' list
# elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]



# #  -2

# # Declare a destroy_elements function that accepts two lists.
# # It should return a list of all elements from the first list that are NOT contained in the second list.
# # Use list comprehension in your solution.
# #





# # EXAMPLES
# print(destroy_elements([1, 2, 3], [1, 2]))     # => [3]
# print(destroy_elements([1, 2, 3], [1, 2, 3]))  # => []
# print(destroy_elements([1, 2, 3], [4, 5]))      #=> [1, 2, 3]
# #--------------------------------------------------------------------------------------

# code 30-1

# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#

   



# # EXAMPLES:
# print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))     #=> ['cat', 'dog', 'ace']
# print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))    # => ['heart']
# print(right_words([], 4))    
# # 
# # -2
# # 
# #  # Declare an only_odds function.
# # It should accept a list of whole numbers.
# # It should return a list with only the odd numbers from the original list.
# # Do NOT use list comprehension.
# #

    



# # EXAMPLES:
# print(only_odds([1, 3, 5, 6, 7, 8]))     # =>  [1, 3, 5, 7]
# print(only_odds([2, 4, 6, 8]))           # =>  []
# # 
# # -3
# # 
# # # Declare a count_of_a function that accepts a list of strings.
# # It should return a list with counts of how many “a” characters appear per string.
# # Do NOT use list comprehension.
# #




# # EXAMPLES:
# print(count_of_a(["alligator", "aardvark", "albatross"]))  #  => [2, 3, 2]
# print(count_of_a(["plywood"]))                               #=> [0]
# print(count_of_a([]))          #                              => []    
#------------------------------------------------------------------------------------
# code 31 -1
# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.



# # EXAMPLES
# print(greater_sum([1, 2, 3], [1, 2, 4])) #=> [1, 2, 4]
# print(greater_sum([4, 5], [2, 3, 6]))    #=> [2, 3, 6]
# print(greater_sum([1], []))              #=> [1]

# # -2

# # Declare a sum_difference function that accepts two lists of numbers.
# # It should return the difference between the sum of values in the first list and the second list
# #





# # EXAMPLES
# print(sum_difference([1, 2, 3], [1, 2, 4]))# => 6 - 7 => -1
# print(sum_difference([4, 5], [2, 3, 6]))#    => 9 - 11 => -2
# print(sum_difference([1], []))#             => 1
#=--------------------------------------------------------------------------
# code 32 -1 

# Declare a months tuple with the last 4 months of the year (September, October, November, December) as strings.
# Make sure the first letter of each month is capitalized.


# Create a faves variable with a list of your 3 three favorite movies as strings. 
# Use the tuple function to convert the list to a tuple and save the result in a movies variable.


# Create a numbers_a, numbers_b, and numbers_c tuple. 
# Each tuple should contain 3 integers. 
# Declare an all_numbers tuple containing these three tuples.



#-------------------------------------------------------------------------------------
# # #code 33 - 1

# # Given the tuple below, destructure the three values and
# # assign them to position, city and salary variables
# # Do NOT use index positions (i.e. job_opening[1])

# job_opening = ("Software Engineer", "New York City", 100000)





# # Given the tuple below, 
# # - destructure the first value and assign it to a street variable
# # - destructure the last value and assign it to a zip_code variable
# # - destructure the middle two values into a list and assign it to a city_and_state variable
# address = ("35 Elm Street", "San Francisco", "CA", "94107")






# # Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
# # It should return a tuple with two numeric values:
# # -- the sum of the even numbers
# # -- the sum of the odd numbers.




# #  




# print(sum_of_evens_and_odds((1, 2, 3, 4)))   #   => (6, 4)
# print(sum_of_evens_and_odds((1, 3, 5)))  #      => (0, 9)
# print(sum_of_evens_and_odds((2, 4, 6)))    #      => (12, 0)
# #-----------------------------------------------------------\\\\\\\\\-

#code 34-1
# Create an empty dictionary and assign it to the variable empty.


# Create a dictionary with three key-value pairs. 
# The keys should be strings and the values should be integer values. 
# Assign the dictionary to a my_dict variable.



# A dictionary’s keys can be any immutable data structure. 
# Create a dictionary with two key-value pairs and assign it to
# a winning_lottery_numbers variable. 
# Both of the keys should be tuples. 
# One of the values should be True, the other value should be False.



    #-------------------------------------------------------------------------------

    
#code 35 -1

# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#




# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}


# -2

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.



    # "Argentina" ==> 9 ==>
    # courrent_count = 0
    # counts[9] = 1
    #{6:1, 9:1}
#-------------------------------------------------------------------------------------------------------------

#     # code 36 -1
# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
# #

# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
# # strings = ["A", "C"]





# # EXAMPLE:

# #
# # delete_keys(my_dict, strings) => {'B': 2}
# ----------------------------------------------------------------------------------------------------

# code 37- 1

# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#

# my_dict = {
#   "A": "B", 
#   "C": "D",
#   "E": "F"
# }



# EXAMPLE:

#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

# -2
# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# EXAMPLE:
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1





# -3
# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0



    #----------------------------------------------------------------------------------------------------------