import math

# Searching, like sorting, is fundamental to a variety of tasks in
# computer science (and in the rest of life). We may want to
# search for a name in a phone book, or (since we’re living after
# the year 2000) we may need to access a database and find a
# relevant record.


# Binary search is a quick and effective method for searching for
# an element in a sorted list. 

# For binary search implementation, we ought to have array, lower and upper bounds
# sorted_cabinet = [1,2,3,4,5]
# upperbound = len(sorted_cabinet)
# lowerbound = 0

# Now we guess the middle one:
# guess = math.floor(len(sorted_cabinet)/2)

# Main logic of our code:
# looking_for = 3
# if(sorted_cabinet[guess] > looking_for):
#     upperbound = guess
#     guess = math.floor((guess + lowerbound)/2)

# if(sorted_cabinet[guess] < looking_for):
#     lowerbound = guess
#     guess = math.floor((guess + upperbound)/2)


sortedcabinet = [1,2,3,4,5,6,7,8,9,10]

def binarysearch(sorted_cabinet,looking_for):
    guess = math.floor(len(sorted_cabinet)/2)
    upperbound = len(sorted_cabinet)
    lowerbound = 0


    while(abs(sorted_cabinet[guess] - looking_for) > 0.0001):
        if(sorted_cabinet[guess] > looking_for):
            upperbound = guess
            guess = math.floor((guess + lowerbound)/2)
        if(sorted_cabinet[guess] < looking_for):
            lowerbound = guess
            guess = math.floor((guess + upperbound)/2)

    return(guess)

print(binarysearch(sortedcabinet,10))


# The binary search method presented here,
# by contrast, can work for any function, and with its O(log(n))
# runtime, it’s also lightning fast.