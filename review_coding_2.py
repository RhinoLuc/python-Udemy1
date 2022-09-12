# code 38 -1
# code 38 -1

# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

#----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# code -39-1

# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
# The lists can be of any length.
        

#-------------------------------------------------------------------------------------------

#code 40 -1

# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#






# EXAMPLES:
# print(plenty_of_arguments(20, 30))  #                          => False
# print(plenty_of_arguments(a = 50, b = 75)) #                 => True
# print(plenty_of_arguments(a = 50, b = 25, c = 50))  #        => True
# print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)) # => False
# print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)) # => True

#------------------------------------------------------------------------------------
#code 41 -1


# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
# channels = {
#   2: "CBS",
#   4: "NBC",
#   5: "FOX",
# #   7: "ABC"
# # }
# # The stations_to_numbers function should return an
# # inverted dictionary where the keys are the station names
# # and the values are the channel numbers
# #
# # def stations_to_numbers(channels):
# #     inverted = { channel: station for station, channel in channels.items() }
# #     return inverted



    





# # print(stations_to_numbers(channels)) # => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

# # -2

# # Declare a coaster_conversion function that accepts a dictionary
# # The keys of the dictionary will be strings representing roller coasters
# # The values will be the heights of each coaster in meters
# #
# # Return a new dictionary with the same keys.
# # The values should be the heights converted from meters to feet,
# # The final values (in feet) should also be rounded to the closest integer
# # HINT: 1 meter is equal to 3.28084 feet
# # HINT: The round function rounds a number to the nearest integer
# # #
# # coasters = {
# #   "Kingda Ka": 139,
# #   "Top Thrill Dragster": 130,
# #   "Superman: Escape From Krypton": 126
# # }
# # #





# print(coaster_conversion(coasters)) #=> {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}

# #----------------------------------------------------------------------------------------

# code 42 -1# code 42 -1

# Declare a set with 3 of your favorite movies as strings.
# Assign it to a movies variable.





# Declare a set with the first four months of the year as strings.
# Assign it to a months variable.
# Make sure the first letter of each month is capitalized.


# Create an empty set and assign it to an empty variable.

 
# Define a remove_duplicates function that accepts a single list as an argument. 
# The function should return a list with all of the duplicates from the original list removed. 
# The order of elements in the returned list is irrelevant.
#

   



# EXAMPLES:
# print(remove_duplicates([1, 2, 1, 2])) # => [1, 2] or [2, 1]
# print(remove_duplicates([1, 2, 3, 4]))  #=> [1, 2, 3, 4] in some order

#---------------------------------------------------------------------------------------------------