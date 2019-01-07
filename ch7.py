#print each item in the following list: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

tvShows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for show in tvShows:
    print(show)


#print all the numbers from 25 to 50

for i in range(25, 51):
    print(i)


#print each item from the first challenge and their indexes

tvShows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

i = 0

for show in tvShows:
    print(show, i)
    i += 1


#write a program with an infinite loop (with the option to type q to quit) and a list of numbers.
#each time through the loop ask the user to guess a number on the list and tell them whether or not
#they guessed correctly

numberList = [5, 7, 12, 15, 18, 20]

#Still working on this problem!



#multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in the list [9, 1, 33, 83]
#and append each result to a third list

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i * j)

print(list3)

