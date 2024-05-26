# Russian peasant
# multiplication(RPM) is a method that enables people to
# multiply large numbers without knowing most of the
# multiplication table.

# The first column is called the halving
# column and starts with 89. The second column is the doubling
# column and starts with 18

# We’ll fill out the halving column first. Each row of the halving
# column takes the previous entry and divides it by 2, ignoring
# the remainder

# We continue dividing by 2 until we reach 1, dropping the
# remainder every time and writing the result in the next row. As
# we continue, we find that 44 divided by 2 is 22, then half of that
# is 11, then half of that (dropping the remainder) is 5, then 2,
# then 1.

# We’ve completed the halving column. As the name suggests,
# each entry in the doubling column will be double the previous
# entry.

# We continue to add entries to the doubling column by following
# the same rule: just double the previous entry. We do this until
# the doubling column has as many entries as the halving column

# The final step is to take the sum of the remaining entries in the
# doubling column.


def rpm(num1, num2):
    # halver
    def halver(num):
        arr = []

        while num != 1:
            arr.append(num)
            num //= 2
        arr.append(1)

        return arr

    def doubler(num):
        arr = [num]

        for _ in range(len(halver(num1)) -1):
            arr.append(num*2)
            num *= 2

        return arr

    rows = [[halver(num1)[i], doubler(num2)[i]] for i in range(len(halver(num1)))]

    updated = [rows[i] for i in range(len(rows)) if rows[i][0] %2 != 0]

    final = sum([updated[i][1] for i in range(len(updated))])

    return final

print(rpm(89, 18))


# easier way
import math
import pandas as pd
import random

n1, n2 = 89, 18

# halving array
halving = [n1]
while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))

# doubling array
doubling = [n2]
while(len(doubling) < len(halving)):
    doubling.append(max(doubling) * 2)

# adding together
half_double = pd.DataFrame(zip(halving,doubling))

# reorganising rows
half_double = half_double.loc[half_double[0]%2 == 1,:]

# result
answer = sum(half_double.loc[:,1])
print(answer)





# Euclid’s algorithm is a method for finding the greatest common
# divisor of two numbers.


# If we divide
# a/b, we’ll get an integer quotient and an integer remainder.
# Let’s call the quotient q , and the remainder c. We can write
# this as follows:

# a = q1 * b + c


# we say that b is larger than c.
# We then find the quotient and remainder when dividing b/c. If
# we say that b/c is q , with remainder d, we can write our result
# as follows:

# b = q2 * c + d
# c = q3 * d + e


# at every step, we’re working with
# smaller and smaller integers, so we must eventually get to zero.
# When we get a zero remainder, we stop the process, and we
# know that the last nonzero remainder is the greatest common
# divisor.

# implementation:
def gcd(x,y):
    larger = max(x,y)
    smaller = min(x,y)

    remainder = larger % smaller

    if(remainder == 0):
        return(smaller)

    if(remainder != 0):
        return(gcd(smaller,remainder))
    
print(gcd(21, 12))

# Notice that this function calls itself if the remainder is nonzero
# The act of a function calling itself is known as recursion.





# A magic square is an array of unique, consecutive natural
# numbers such that all rows, all columns, and both of the main
# diagonals have the same sum.

# Algorithms are often easy to verify and use, but
# they can be difficult to design from scratch.

# We can implement magic square algorithm:
# first, we create matrix:
luoshu = [[4,9,2],[3,5,7],[8,1,6]]

# then we create verifier function:
def verifysquare(square):
    sums = []

    rowsums = [sum(square[i]) for i in range(0,len(square))]
    sums.append(rowsums)

    colsums = [sum([row[i] for row in square]) for i in
    range(0,len(square))]
    sums.append(colsums)

    maindiag = sum([square[i][i] for i in range(0,len(square))])
    sums.append([maindiag])

    antidiag = sum([square[i][len(square) - 1 - i] for i in range(0,len(square))])
    sums.append([antidiag])

    flattened = [j for i in sums for j in i]

    return(len(list(set(flattened))) == 1)


# One of the most elegant algorithms for generating magic
# squares, Kurushima’s algorithm is named for Kurushima
# Yoshita, who lived during the Edo period.


# We can begin the process of creating a magic square by creating
# an empty square matrix that we’ll fill up.



# n = 7
# square = [[float('nan') for i in range(0,n)] for j in range(n)]

# We can make output better by following function:
# def printsquare(square):
#     labels = ['[' + str(x) + ']' for x in range(len(square))]
#     format_row = "{:>6}" * (len(labels) + 1)
#     print(format_row.format("", *labels))

#     for label, row in zip(labels, square):
#         print(format_row.format(label, *row))

# We can fill in the central five squares with simple commands.
# center_i = math.floor(n/2)
# center_j = math.floor(n/2)

# square[center_i][center_j] = int((n**2 +1)/2)
# square[center_i + 1][center_j] = 1
# square[center_i - 1][center_j] = n**2
# square[center_i][center_j + 1] = n**2 + 1 - n
# square[center_i][center_j - 1] = n

# printsquare(square)


# Then we have to fill in rest of nan spaces with numbers by following rules:


# 1.
# So for any x in the magic square, we can determine the entry
# that is situated in this diagonal relationship to x by simply
# adding n and taking the result mod n (mod refers to the
# modulo operation).

# 2.
# For any x in the magic square, the entry below and to the right
# of x is 1 greater than x, mod n .
# not follow the second rule if we are crossing the magic square’s
# antidiagonal, the bottom-left-to-top-right line

# 3.
# We need
# the exceptional third rule only when starting in a cell that is
# fully above the antidiagonal and crossing to a cell that is fully
# below it, or vice versa.



# Now we can make functions that represent each rule:
# def rule1(x,n):
#     return((x + n)% n**2)

# we could
# improve it by enabling it to go “in reverse,” determining not
# only the entry on the bottom left of a given entry, but also the
# entry to the top right (that is, being able to go from 8 to 5 in
# addition to going from 5 to 8).


# Rule 1:
# def rule1(x,n,upright):
#     return((x + ((-1)**upright) * n) %n**2)
# As we know, True is equal to 1, and False is equal to 0


# Rule 2:
# For Rule 2, we can create an analogous function. Our Rule 2
# function will take x and n as arguments, just like Rule 1. But
# Rule 2 is by default finding the entry below and to the right of
# x. So we will add an upleft argument that will be True if we
# want to reverse the rule.
# def rule2(x,n,upleft):
#     return((x + ((-1)**upleft))%n**2)

# def rule3(x,n,upleft):
#     return((x + ((-1)**upleft * (-n + 1)))%n**2)


# Now that we know how to fill the five central squares, and we
# have a rule to fill out the remaining squares based on
# knowledge of those central squares, we can fill out the rest of
# the square.

# entry_i = center_i
# entry_j = center_j
# where_we_can_go = ['up_left','up_right','down_left','down_right']
# where_to_go = random.choice(where_we_can_go)

# if(where_to_go == 'up_right'):
#     new_entry_i = entry_i - 1
#     new_entry_j = entry_j + 1
#     square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j],n,True)
# if(where_to_go == 'down_left'):
#     new_entry_i = entry_i + 1
#     new_entry_j = entry_j - 1
#     square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j],n,False)
# if(where_to_go == 'up_left'):
#     new_entry_i = entry_i - 1
#     new_entry_j = entry_j - 1
#     square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j],n,True)
# if(where_to_go == 'down_right'):
#     new_entry_i = entry_i + 1
#     new_entry_j = entry_j + 1
#     square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j],n,False)


# These ones for rule3
# if(where_to_go == 'up_left' and (entry_i + entry_j) == (n)):
#     new_entry_i = entry_i - 1
#     new_entry_j = entry_j - 1
#     square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j],n,True)
# if(where_to_go == 'down_right' and (entry_i + entry_j) == (n-2)):
#     new_entry_i = entry_i + 1
#     new_entry_j = entry_j + 1
#     square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j],n,False)


# By creating our list of where it’s possible to travel based on our
# current location, we can add some simple logic to ensure that
# we travel only in allowed directions:

# where_we_can_go = []
# if(entry_i < (n - 1) and entry_j < (n - 1)):
#     where_we_can_go.append('down_right')
# if(entry_i < (n - 1) and entry_j > 0):
#     where_we_can_go.append('down_left')
# if(entry_i > 0 and entry_j < (n - 1)):
#     where_we_can_go.append('up_right')
# if(entry_i > 0 and entry_j > 0):
#     where_we_can_go.append('up_left')


# Now we can see final result:
# Create an example magic square (Luoshu)
luoshu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

# Verify function to check if a square is magic
def verifysquare(square):
    sums = []
    n = len(square)
    
    rowsums = [sum(square[i]) for i in range(n)]
    sums.append(rowsums)
    
    colsums = [sum(row[i] for row in square) for i in range(n)]
    sums.append(colsums)
    
    maindiag = sum(square[i][i] for i in range(n))
    sums.append([maindiag])
    
    antidiag = sum(square[i][n - 1 - i] for i in range(n))
    sums.append([antidiag])
    
    flattened = [j for sublist in sums for j in sublist]
    return len(set(flattened)) == 1

# Function to print the square
def printsquare(square):
    labels = ['[' + str(x) + ']' for x in range(len(square))]
    format_row = "{:>6}" * (len(labels) + 1)
    print(format_row.format("", *labels))
    
    for label, row in zip(labels, square):
        print(format_row.format(label, *row))

# Functions representing each rule
def rule1(x, n, upright):
    return (x + ((-1) ** upright) * n) % n**2

def rule2(x, n, upleft):
    return (x + ((-1) ** upleft)) % n**2

def rule3(x, n, upleft):
    return (x + ((-1) ** upleft * (-n + 1))) % n**2

# Fill the square based on the rules
def fillsquare(square, entry_i, entry_j, howfull):
    n = len(square)
    n2 = n**2
    while sum(math.isnan(i) for row in square for i in row) > howfull:
        where_we_can_go = []
        if entry_i < (n - 1) and entry_j < (n - 1):
            where_we_can_go.append('down_right')
        if entry_i < (n - 1) and entry_j > 0:
            where_we_can_go.append('down_left')
        if entry_i > 0 and entry_j < (n - 1):
            where_we_can_go.append('up_right')
        if entry_i > 0 and entry_j > 0:
            where_we_can_go.append('up_left')
        
        where_to_go = random.choice(where_we_can_go)
        
        if where_to_go == 'up_right':
            new_entry_i = entry_i - 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, True)
        elif where_to_go == 'down_left':
            new_entry_i = entry_i + 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, False)
        elif where_to_go == 'up_left' and (entry_i + entry_j) != n:
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, True)
        elif where_to_go == 'down_right' and (entry_i + entry_j) != n2:
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, False)
        elif where_to_go == 'up_left' and (entry_i + entry_j) == n:
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j], n, True)
        elif where_to_go == 'down_right' and (entry_i + entry_j) == n2:
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j], n, False)
        
        entry_i = new_entry_i
        entry_j = new_entry_j
    
    return square

# Initialize the square
n = 7
square = [[float('nan') for _ in range(n)] for _ in range(n)]

# Fill the central five squares
center_i = math.floor(n / 2)
center_j = math.floor(n / 2)

square[center_i][center_j] = int((n**2 + 1) / 2)
square[center_i + 1][center_j] = 1
square[center_i - 1][center_j] = n**2
square[center_i][center_j + 1] = n**2 + 1 - n
square[center_i][center_j - 1] = n

# Fill the rest of the square
entry_i = center_i
entry_j = center_j
howfull = n**2 - 5  # Remaining spaces to fill
square = fillsquare(square,entry_i,entry_j,(n**2)/2 - 4)
square=[[n**2 if x == 0 else x for x in row] for row in square]

# Print the final square and verify it
printsquare(square)
print("Is the square magic?", verifysquare(square))

printsquare(luoshu)
print("Is the square magic?", verifysquare(luoshu))





# In this chapter, we discussed some historical algorithms that
# range from a few centuries to a few millenia old.