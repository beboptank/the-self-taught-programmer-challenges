# create a list of your favorite musicians

fav_musicians = ["Led Zeppelin", "Alan Jackson", "Days N Daze", "The Dead South", "Old Crow Medicine Show"]

# create a list of tuples, with each tuple containing the longitude and latitude of somewhere you've lived or visited

visited_places = [("35.6895° N, 139.6917° E"), ("35.1112° N, 81.2265° W"), ("36.0641° N, 136.2195° E"), ("20.4230° N, 86.9223° W")]

# create a dictionary that contains different attributes about you: height, favorite color, favorite author, etc.

about_me = {
    "height": "170 cm",
    "favorite color": "red",
    "favorite author": "Haruki Murakami",
    "favorite food": "scrambled eggs with cheese",
    "favorite movie": "Cowboy Beop The Movie"
}

# write a program that lets the user ask your height, favorite color, or favorite author, and returns the result from the
# dictionary you created in the previous challenge

want_to_know = input("What would you like to know? Please enter height, color, author, food, or movie:")

if want_to_know in about_me:
    seth_info = about_me[want_to_know]
    print (seth_info)
else:
    print("Information not available.")

# create a dictionary maping your favorite musicians to a list of your favorite songs by them

fav_musicians_and_songs = {
    "Led Zeppelin": ["Dazed and Confused", "Ramble On"],
    "Alan Jackson": ["Chattahoochie", "Remember When", "5 O'Clock Somewhere"],
    "Days N Daze": ["Misanthropic Drunken Loner", "Call In the Coroner"],
    "The Dead South": ["The Good Lord", "That Bastard Son"],
    "Old Crow Medicine Show": ["Take 'Em Away", "Brushy Mountain Conjugal Trailer"]
}

# Sets are a standard Python data type used to store values. They cannot have multiple occurences of the same
# element and store unordered values. They are useful when doing mathematical set operations, like union, intersection, 
# symmetric difference, and others.

