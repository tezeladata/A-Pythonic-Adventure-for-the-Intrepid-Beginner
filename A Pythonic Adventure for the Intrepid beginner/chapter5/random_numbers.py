# Several of the most powerful machine learning methods
# (including random forests and neural networks) rely heavily on
# random selections to function properly.

# The same goes for
# powerful statistical methods, like bootstrapping, that use
# randomness to make a static dataset better resemble the
# chaotic world.

# The list goes on; there’s a huge, constant demand
# for randomness in most technological fields.

# Since a computer cannot deliver true randomness, we’ve
# designed algorithms that can deliver the next-best thing:
# pseudorandomness.




# LINEAR CONGRUENTIAL GENERATORS
# One of the simplest examples of a pseudorandom number
# generator(PRNG) is the linear congruential generator(LCG)

# To implement this algorithm, you’ll have to choose three
# numbers, which we’ll call n , n , and n . The LCG starts with
# some natural number (like 1) and then simply applies the
# following equation to get the next number:

# next = (previous * this_number + following_number) % third_number

def next_random(previous,n1,n2,n3):
    the_next = (previous * n1 + n2) % n3
    return the_next

# Note that the next_random() function is deterministic, meaning
# that if we put the same input in, we’ll always get the same
# output. Once again, our PRNG has to be this way because
# computers are always deterministic. LCGs do not generate truly
# random numbers, but rather numbers that look random, or are
# pseudorandom.


# Instead of getting one random number at a
# time, we could compile an entire list with a function that
# repeatedly calls the next_random() function we just created, as
# follows:
def list_random(n1,n2,n3):
    output = [1]
    while len(output) <=n3:
        output.append(next_random(output[len(output) - 1],n1,n2,n3))
    return output

print(list_random(29, 23, 32))

# The number of unique values that we obtain before
# they repeat is called the period of our PRNG. In this case, the
# period of our LCG is 32.