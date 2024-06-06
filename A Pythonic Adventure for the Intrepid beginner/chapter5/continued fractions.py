# Like pi and a
# few other famous constants, such as the exponential base e, phi
# has a tendency to show up in unexpected places. People have
# found phi in many places in nature, and have painstakingly
# documented where it occurs in fine art


# Unfortunately, the golden ratio is what’s called
# an irrational number, meaning that there are no two integers x
# and y that enable us to say that phi is equal to x/y.


# How we can represent phi:
# phi**2 - phi - 1 = 0
# phi - 1 - 1/phi = 0
# phi = 1 + 1/phi

# when we write 1/phi in right part, we can substitute 1 + 1/phi in part of /phi
# phi = 1 + 1 / (1 + 1/ phi)

# If we imagine continuing this process, we can push phi infinity levels in.



# A continued fraction consists of sums and reciprocals nested in
# multiple layers - Just as phi


# Continued fractions are especially useful for our purposes
# because they enable us to express the exact value of phi without
# needing to chop down an infinite forest to manufacture enough
# paper.


# Instead of writing all the fraction
# bars in a continued fraction, we can use square brackets ([ ]) to
# denote that we’re working with a continued fraction, and use a
# semicolon to separate the digit that’s “alone” from the digits
# that are together in a fraction.

# phi = [1; 1,1,1,1 . . . ]

# We can have another number like that:
# e = [2; 1,2,1,1,4,1 . . . ]


# Our continued fraction for phi came from a special equation
# that works only for phi. But in fact, it is possible to generate a
# continued fraction representation of any number.



# We take 105 / 33. It is equal to 3 + 6/33
# 3 + 6/33 = a + 1 / (b + 1 / (c + 1 / (. . . ))) 
# 3 and a are equal so 6/33 = 1 / (b + 1/ (c + 1/ (. . . )))

# If we take reciprocal of divisions: 33 / 6 = b + 1 / (c + 1/ (d + 1/ (. . . )))

# Our task is now to find b and c. We can do a division again; 33
# divided by 6 is 5, with remainder 3, so we can rewrite 33/6 as 5
# + 3/6

# We can conclude that the integer parts are equal, so b = 5.


# If you can’t tell immediately
# that 3/6 is equal to 1/2, you could follow the same process we
# did for 6/33: say that 3/6 expressed as a reciprocal is 1/(6/3),
# and we find that 6/3 is 2 remainder 0. The algorithm we’re
# following is meant to complete when we have a remainder of 0,
# so we will realize that we’ve finished the process

# 105 / 33 = 3 + 1 / (5 + 1/2)

# in the continued fraction
# generation algorithm, we recorded every quotient (every letter
# of the alphabet) along the way.


# Now we can finally implement that algorithm:
import math


# x = 105
# y = 33
# big = max(x,y)
# small = min(x,y)

# output = []
# quotient = math.floor(big/small)
# output.append(quotient)

# Remember that 33 was previously the small variable, but now
# it’s the big one, and the remainder of our division process is the
# new small variable. Since the remainder is always smaller than
# the divisor, big and small will always be correctly labeled:
# new_small = big % small
# big = small
# small = new_small


def continued_fraction(x,y,length_tolerance):
    output = []
    big = max(x,y)
    small = min(x,y)

    while small > 0 and len(output) < length_tolerance:
        quotient = math.floor(big/small)
        output.append(quotient)
        new_small = big % small
        big = small
        small = new_small

    return output

print(continued_fraction(105, 33, 20))

# Here, we took x and y as inputs, and we defined a
# length_tolerance variable. Remember that some continued
# fractions are infinite in length, and others are extremely long.
# By including a length_tolerance variable in the function, we
# can stop our process early if the output is getting unwieldy, and
# thereby avoid getting caught in an infinite loop.


# We can also implement function to get number from fraction array
def get_number(continued_fraction):
    index = -1
    number = continued_fraction[index]

    while abs(index) < len(continued_fraction):
        next = continued_fraction[index - 1]
        number = 1/number + next
        index -= 1

    return number

print(get_number(continued_fraction(105, 33, 20)))



# What if, instead of starting with some x/y as an input to our
# continued fraction algorithm, we start with a decimal number,
# like 1.4142135623730951? We’ll need to make a few
# adjustments, but we can more or less follow the same process
# we followed for fractions

# x = 1.4142135623730951
# output = []
# first_term = int(x)
# leftover = x - int(x)
# output.append(first_term)
# print(output)


# Our next term, b, will be the integer part to the left of the
# decimal point in this new term—in this case, 2. And then we
# will repeat the process: taking a reciprocal of a decimal part,
# finding the integer part to the left of the decimal, and so on.

# next_term = math.floor(1/leftover)
# leftover = 1/leftover - next_term
# output.append(next_term)
# print(output)


def continued_fraction_decimal(x,error_tolerance,length_tolerance):
    output = []
    first_term = int(x)
    leftover = x - int(x)
    output.append(first_term)
    error = leftover

    while error > error_tolerance and len(output) <length_tolerance:
        next_term = math.floor(1/leftover)
        leftover = 1/leftover - next_term
        output.append(next_term)
        error = abs(get_number(output) - x)

    return output

print(continued_fraction_decimal(1.4142135623730951,0.00001,100))