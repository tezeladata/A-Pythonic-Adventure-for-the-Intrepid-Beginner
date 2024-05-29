# Sleep sort wasn’t designed to resemble any real-world
# situation, like inserting files into a filing cabinet.


# A sleep-sort approach to the Titanic lifeboats would be the
# following. We would announce, “Everyone please stand still
# and count to your age: 1, 2, 3, . . . . As soon as you have counted
# up to your current age, step forward to get on a lifeboat.” We
# can imagine that 8-year-olds would finish their counting about
# one second before the 9-year-olds, and so would have a onesecond head start and be able to get a spot on the boats before
# those who were 9. The 8- and 9-year-olds would similarly be
# able to get on the boats before the 10-year-olds, and so on.


# This Titanic lifeboat process shows the idea of sleep sort: allow
# each element to insert itself directly, but only after a pause in
# proportion to the metric it’s being sorted on. 


# From a
# programming perspective, these pauses are called sleeps and
# can be implemented in most languages.


import threading
from time import sleep

def sleep_sort(i):
    sleep(i)
    global sortedlist
    sortedlist.append(i)

items = [2, 4, 5, 2, 1, 7]
sortedlist = []

# Start threads
ignore_result = [threading.Thread(target=sleep_sort, args=(i,)).start() for i in items]

# Add a sleep to ensure all threads complete
sleep(max(items) + 1)
print(sortedlist)

# Here are disadvantages of sleep sort:
# Big runtime, dependent on array size, uses threading, cannot work on negative values, is bad for simillar values


# If we had to express sleep sort’s runtime in big O notation, we
# might say that it is O(max(list)). Unlike the runtime of every
# other well-known sorting algorithm, its runtime depends not
# on the size of the list but on the size of the elements of the list.


# There may never be a practical use for sleep sort, even on a
# sinking ship.