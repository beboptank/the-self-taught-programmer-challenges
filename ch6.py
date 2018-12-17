# print every character in the string "Camus"

lets_print = "Camus"

print (
    lets_print[0],
    lets_print[1],
    lets_print[2],
    lets_print[3],
    lets_print[4]
)

# write a program that collects two strings from a user, inserts them into the string "Yesterday I wrote a [response_one].
# I sent it to [response_two]!" and prints a new string

writing = input("Enter a type of literature (book, pamphlet, etc):")
person = input("Enter a person's name:")

new_sentence = "Yesterday I wrote a {}. I sent it to {}.".format(writing, person)

print (new_sentence)

# use a method to make the string "aldous Huxley was born in 1894." grammatically correct by capitalizing the first letter in the sentence

huxley = "aldous Huxley was born in 1894."

huxley = huxley.capitalize()

print (huxley)

# take the string "Where now? Who now? When now?" and call a method that returns a list that looks like: 
# ["Where now?", "Who now?", "When now?"]

"Where now? Who now? When now?".split(" ")

# take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a grammactically correct string.
# There should be a space between the word fence and the period that follows it. 

words = ["The", "fox", "jumped", "over", "the", "fence", "."]

fox_sentence = " ".join(words)

fox_sentence = fox_sentence[:29] + fox_sentence[-1]

# replace every instance of "s" in "A screaming comes across the sky." with a dollar sign

scream_sentence = "A screaming comes across the sky."

scream_sentence = scream_sentence.replace("s", "$")

print (scream_sentence)

# use a method to find the first index of the character "m" in the string "Hemingway"

"Hemingway".index("m")

# find dialogue in your favorite book (containing quotes) and turn it into a string

norwegian_wood = '''"How did you like my song?" she asked.
I answered cautiously, "It was unique and original and very expressive of your personality."
"Thanks," she said. "The theme is that I have nothing."
"Yeah, I kinda thought so."'''

# create the string "three three three" using concatenation, and then again using multiplication

three_concat = "three " + "three " + "three"

three_mult = "three " * 3

three_mult = three_mult.strip()

# slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to only include the
# characters before the comma

quote = "It was a bright cold day in April, and the clocks were striking thirteen."

quote = quote[0:33]

print (quote)