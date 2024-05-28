# To say that an algorithm runs in more or less n steps is a
# reasonable balance between the precision we want and the
# conciseness we want

# The way
# we express this type of “more or less” relationship formally is
# by using big O notation(the O is short for order).

# When we used insertion sort, the formula for maximu steps was sum of
# multiple of n**2 plus multiple of n.
# the term that is a multiple of n will matter less and
# less as n grows, and the n term will come to be the only one
# that we are concerned with.

# So the worst case of insertion sort
# is that it is a O(n ) (“big O of n ”) algorithm.


# If we could find a way to alter insertion sort so that it
# is O(n ) instead of O(n ), that would be a major breakthrough
# that would make a huge difference in runtimes for large values
# of n.



# In this chapter, we’ll focus on gaining speed
# and designing algorithms to have runtimes that are big O of the
# smallest possible functions, without regard to memory
# requirements.