# RESOURCES - USE THESE
# W3Schools | https://www.w3schools.com/python/
# If...Else | https://www.w3schools.com/python/python_conditions.asp
# for Loops | https://www.w3schools.com/python/python_for_loops.asp
# Operators | https://www.w3schools.com/python/python_operators.asp
#
# Do not modify the present code.
# It is there to chunk your output into easily understandable
# 	segments.

print('\n1\n-----------------------------------------------\n')
# Accept input from the user in the form of three
# 	different whole numbers. These number will represent

# 	the length of a Triangle. Output whether or not this
# 	Triangle is equilateral, isosceles, or scalene.
#	Example Output:
#
# side a: 4
# side b: 4
# side c: 6
# this is an isoceles triangle



# Do it again using the same values before, but use compound 
#	conditionals instead if you used complex ones. If you
#	used compound conditionals originally, use complex.



print('\n2\n-----------------------------------------------\n')
# Accept input from the user in the form of a String.
# This string will be a password. Confirm that the user
# has entered a password that is at least 8 characters
# long, and has at least one of the following characters
# !, @, #, or $
#
# Example Output (valid password)
#
# please enter a password: hdsj341!
# this password is valid
#
# Example Output (valid password)
#
# please enter a password: lmklmnio
# this password is invalid

print('\n3\n-----------------------------------------------\n')
# Write a for loop that generates the example pattern with
#	any character the you choose.
#
# symbol: -
#
#  -----  i=0
# -     - i=1
# -     - i=2
# -     - i=3
# -     - i=4
#  -----  i=5

for i in range(6):
  # print(f'i: {i}')
  if i == 0 or i == 5:
    print(' ----- ')
  else:
    print('-     -')


print('\n4\n----------------------------------------------\n')
# Write a for loop that generates the example pattern with
#	any character you choose.
#
# symbol: ~
#
#   ~~~~  i
#  ~    ~ i
# ~      ~i
# ~~~~~~~~i=
# ~      ~i=
# ~      ~i=
# ~      ~i=



print('\n5\n-----------------------------------------------\n')
# Write a for loop that generates the example pattern with
#	any character you choose.
#
# CHALLENGE: You must do this with a single if - else
#				statement.
#
# symbol: ^
#
# ^^^^^^^^
#       ^ 
#      ^  
#     ^   
#    ^    
#   ^     
#  ^      
# ^^^^^^^^

print('\n6\n-----------------------------------------------\n')
# Accept input from the user in the form of a string. This
#	will be a random assortment of letters and numbers.
#   
#   Transform this string into a list, using the list() function.
#
#	Iterate over this list, replacing the numbers in the list
#	with the characters in the list provided. The character that
#	replaces the number should be the character at that numbers
#	position. Example Output:
#
# plain text: a23fva07ol
# cipher text: acdfvaahol
#
# ! Notice the changed letters.


letters = ['a','b','c','d','e','f','g','h','i','j','k']

print('\n6\n-----------------------------------------------\n')
# Accept input from the user in the form of a string. This
#	will be a sentence that the user enters.
#   
#   Transform this sentence into a list, with the items in the
#	list being each word in the sentence.
#
#	Iterate over this list, popping the words in the list
#	if they contain the letters 'c', 'h', 'o', 'n', or 's'.
#	Insert these items to the FRONT of the list, after they have
#	been popped.
#
#	Print the changed list in the form of a string.
#
# original: Hello, my dear old friend!
# modified: old Hello, my dear friend!


