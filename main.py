"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Matouš Segéň
email: matous.segen@gmail.com
"""

from sys import exit

# variable initialization
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

credentials = {"bob": "123",
               "ann": "pass123",
               "mike": "password123",
               "liz": "pass123"}

username = input("username:").strip().lower()   # handles uppercase letters and whitespaces
password = input("password:")
line = "-" * 40

# credentials verification
for loop_name, loop_password in credentials.items():
    if username == loop_name and password == loop_password:
        print(line)
        print(f"Welcome to the app, {username}")
        break
else:
    print("unregistered user, terminating the program..")
    exit()

# continue program
print("We have 3 texts to be analyzed.")
print(line)

# user input handling
try:
    text_num = int(input("Enter a number btw. 1 and 3 to select: "))
    text_num -= 1   # set the range from [1, 3] to [0, 2] for easier use

except ValueError:
    print("Wrong input, terminating the program..")
    exit()

if int(text_num) not in range(3):
    print("Number is not in range, terminating the program..")
    exit()

# text analysis and statistics
word_count = 0
word_title = 0
word_lower = 0
word_upper = 0
number_count = 0
number_sum = 0

words_lengths = {}  # Stores occurrences of each word length

text_analyzed = TEXTS[text_num].split()

for item in text_analyzed:
    word = item.translate(str.maketrans("", "", ",.-"))
    word_count += 1

    if word.isdigit():
        number_count += 1
        number_sum += int(word)

    elif word.isalpha():
        if word.istitle():
            word_title += 1
    
        if word.isupper():
            word_upper += 1
    
        if word.islower():
            word_lower += 1
        
        word_len = len(word)
        words_lengths[word_len] = words_lengths.get(word_len, 0) + 1

sorted_words_lengths = dict(sorted(words_lengths.items())) 

# formatted output of the results
print(f"""{line}
There are {word_count} words in the selected text.
There are {word_title} titlecase words.
There are {word_upper} uppercase words.
There are {word_lower} lowercase words.
There are {number_count} numeric strings.
The sum of all the numbers {number_sum}
{line}
LEN|  OCCURENCES  |NR.
{line}""")

for dict_key, dict_value in sorted_words_lengths.items():
    stars = "*" * dict_value
    print(f"{dict_key:3}|{stars.ljust(20)}|{dict_value}")