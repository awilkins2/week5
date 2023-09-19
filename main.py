#######################paired programmming###############################

# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = "abracadabra"
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find('c'))
# Advanced Slicing:
# Given the string 
alphabet = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(alphabet[7:10])

# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
print(alphabet[0::2])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the 
quote="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote[-15:])
# Manipulating Words:
# Given the string 
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.\
subjective=info.find("subjective")
print(subjective)
print(info[36:])
# b. Extract every third word.
info2=info.split()
print(info2)
print(info2[::-1])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase:
text="MAY THE FORCE BE WITH YOU."
print(text.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the 
sentence="Life is what happens when you are busy making other plans."
print(sentence.replace("busy", "distracted"))
print(sentence.replace("plans","mistakes"))
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.


