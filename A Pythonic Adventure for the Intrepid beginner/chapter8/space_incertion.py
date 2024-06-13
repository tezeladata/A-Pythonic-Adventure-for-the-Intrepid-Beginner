# The algorithms in this chapter rely heavily on two tools that we
# haven’t used before: list comprehensions and corpuses. List
# comprehensions enable us to quickly generate lists using the
# logic of loops and iterations. They’re optimized to run very
# quickly in Python and they’re easy to write concisely, but they
# can be hard to read and their syntax takes some getting used to.
# A corpus is a body of text that will “teach” our algorithm the
# language and style we want it to use.


# In order to use algorithms with language, we must either make
# language simpler, so that the short mathematical algorithms
# we have explored so far can reliably work with it, or make our
# algorithms smarter, so that they can deal with the messy
# complexity of human language as it has developed naturally.

text = "The oneperfectly divine thing, the oneglimpse of God's paradisegiven on earth, is to fight a losingbattle - and notlose it."

# We can start by creating a list of words
word_list = ['The','one','perfectly','divine']


# We’ll use Python’s re module to access text manipulation tools.
# One of re’s useful functions is finditer(), which can search our
# text to find the location of any word in our word_list. We use
# finditer() in a list comprehension like so:

import re
locs = list(set([(m.start(),m.end()) for word in word_list for m in re.finditer(word, text)]))
print(locs)



# We can use re.finditer() again to find all the spaces in our
# text, which we’ll store in a variable called spacestarts.
spacestarts = [m.start() for m in re.finditer(' ', text)]
spacestarts.append(-1)
spacestarts.append(len(text))
spacestarts.sort()
print(spacestarts)


# It will be useful to have
# another list that records the locations of characters that come
# just after a space; these will be the locations of the first
# character of each potential word. We’ll call that list
# spacestarts_affine, since in technical terms, this new list is an
# affine transformation of the spacestarts list.
spacestarts_affine = [ss+1 for ss in spacestarts]
spacestarts_affine.sort()
print(spacestarts_affine)


# Next, we can get all the substrings that are between two spaces:
between_spaces = [(spacestarts[k] + 1,spacestarts[k + 1]) for k in range(0,len(spacestarts) - 1 )]
print(between_spaces)


# This one finds words that are not in our words list
between_spaces_notvalid = [loc for loc in between_spaces if text[loc[0]:loc[1]] not in word_list]
print(between_spaces_notvalid)


# remember that we
# want this space insertion algorithm to work for millions of
# pages of scanned text, and they may contain many thousands of
# unique words. It would be helpful if we could import a word list
# that already contained a substantial body of valid English
# words. Such a collection of words is referred to as a corpus.





# Luckily, there are existing Python modules that allow us to
# import a full corpus with just a few lines. First, we need to
# download the corpus:
import nltk
from nltk.corpus import brown
wordlist = set(brown.words())
word_list = list(wordlist)


# We have imported the corpus and converted its collection of
# words into a Python list. Before we use this new word_list,
# however, we should do some cleanup to remove what it thinks
# are words but are actually punctuation marks:
word_list = [word.replace('*','') for word in word_list]
word_list = [word.replace('[','') for word in word_list]
word_list = [word.replace(']','') for word in word_list]
word_list = [word.replace('?','') for word in word_list]
word_list = [word.replace('.','') for word in word_list]
word_list = [word.replace('+','') for word in word_list]
word_list = [word.replace('/','') for word in word_list]
word_list = [word.replace(';','') for word in word_list]
word_list = [word.replace(':','') for word in word_list]
word_list = [word.replace(',','') for word in word_list]
word_list = [word.replace(')','') for word in word_list]
word_list = [word.replace('(','') for word in word_list]
word_list.remove('')


partial_words = [loc for loc in locs if loc[0] in spacestarts_affine and loc[1] not in spacestarts]
# Now that we have a suitable word list, we’ll be able to
# recognize invalid words more accurately. We can rerun our
# check for invalid words using our new word_list and get better
# results:
between_spaces_notvalid = [loc for loc in between_spaces if text[loc[0]:loc[1]] not in word_list]
print(between_spaces_notvalid)


# Next, let’s look for words that end with a space. These could be
# the second half of an invalid word. To find them, we make
# some small changes to the previous logic:
partial_words_end = [loc for loc in locs if loc[0] not in spacestarts_affine and loc[1] in spacestarts]



# Let’s start by inserting a space into oneperfectly. We’ll define a
# variable called loc that stores the location of oneperfectly in
# our text:
loc = between_spaces_notvalid[0]

# We’ll write a list
# comprehension that finds the ending location of every valid
# word that begins at the same location as oneperfectly:
endsofbeginnings = [loc2[1] for loc2 in partial_words if loc2[0] == loc[0] and (loc2[1] - loc[0]) > 1]


# Let’s use a list comprehension to create a similar variable,
# called beginningsofends, that will find the beginning location of
# every valid word that ends at the same place as oneperfectly:
beginningsofends = [loc2[0] for loc2 in partial_words_end if loc2[1] == loc[1] and (loc2[1] - loc[0]) > 1]


# We’re almost home; we just need to find whether any locations
# are contained in both endsofbeginnings and beginningsofends.
# If there are, that means that our invalid word is indeed a
# combination of two valid words without a space. We can use
# the intersection() function to find all elements that are shared
# by both lists:
pivot = list(set(endsofbeginnings).intersection(beginningsofends))


# In our case, we’ll take the
# smallest element of pivot, not because this is certainly the
# correct one, but just because we have to take one:
import numpy as np
pivot = np.min(pivot)

textnew = text
textnew = textnew.replace(text[loc[0]:loc[1]],text[loc[0]:pivot]+''+text[pivot:loc[1]])
print(textnew)