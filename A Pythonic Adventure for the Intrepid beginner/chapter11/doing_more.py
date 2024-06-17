# In this chapter, we’ll build a simple chatbot that can talk to us
# about previous chapters of the book. Then we’ll discuss some of
# the hardest problems in the world and how we might make
# progress toward crafting algorithms to solve them.

# For example, the many algorithms for information
# compression can store a long book in a coded form that is only
# a fraction of the size of the original, and they can compress a
# complex photograph or film file into a manageable size with
# either minimal or no loss of quality.


# Recently, innovative algorithms have been developed to
# perform parallel distributed computing. Instead of performing
# one operation at a time, millions of times, distributed
# computing algorithms split up a dataset into many little parts
# and then send them to different computers, which perform the
# needed operation simultaneously and return the results, to be
# recompiled and presented as the final output.


# Quantum computers, if we can engineer
# them to work properly, have the potential to perform extremely
# difficult calculations (including the calculations needed to
# break state-of-the-art cryptography) in a tiny fraction of the
# time required on today’s nonquantum supercomputers.


# For chatbot
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
import numpy as np
import nltk, string



# query = 'I want to learn about geometry algorithms.'
# print(query.lower()) # for lowercase

# Another thing we can do is remove punctuation. To do that,
# first we’ll create a Python object called a dictionary:
# remove_punctuation_map = dict((ord(char), None) for char in
# string.punctuation)
# print(remove_punctuation_map)


# This snippet creates a dictionary that maps every standard
# punctuation mark to the Python object None, and it stores the
# dictionary in a variable called remove_punctuation_map. We then
# use this dictionary to remove punctuation like so:
# print(query.lower().translate(remove_punctuation_map))

# Here, we’ve used the translate() method to take all the
# punctuation marks we find in the query and replace them with
# nothing—or in other words, remove the punctuation marks.


# Next, we can perform tokenization, which converts a
# text string to a list of coherent substrings:
# print(nltk.word_tokenize(query.lower().translate(remove_punctuation_map)))

# next we do stemming
# stemmer = nltk.stem.porter.PorterStemmer()
# def stem_tokens(tokens):
#     return [stemmer.stem(item) for item in tokens]
# print(stem_tokens(nltk.word_tokenize(query.lower().translate(remove_punctuation_map))))

# Our stemmer has converted
# algorithms to algorithm and geometry to geometri.


# Finally, we put our normalization steps together in one
# function, normalize():


# 1
query = 'I want to learn about geometry algorithms.'

# 2
remove_punctuation_map = dict((ord(char), None) for char in
string.punctuation)

# 3
stemmer = nltk.stem.porter.PorterStemmer()
def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

# 4
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))
print(normalize(query))





# We’ll use a simple method called TFIDF, or term frequencyinverse document frequency, which converts documents into
# numeric vectors. Each document vector has one element for
# each term in a corpus.



# This line has created a TfidfVectorizer() function, which is
# capable of creating TFIDF vectors from sets of documents. To
# create the vectorizer, we have to specify an ngram_range. This
# tells the vectorizer what to treat as a term. We specified (1, 1),
# meaning that our vectorizer will treat only 1-grams (individual
# words) as terms. If we had specified (1, 3), it would treat 1-
# grams (single words), 2-grams (two-word phrases), and 3-
# grams (three-word phrases) as terms and create a TFIDF
# element for each of them. We also specified a tokenizer, for
# which we specified the normalize() function we created before.
# Finally, we have to specify stop_words, the words that we want
# to filter out because they’re not informative. In English, stop
# words include the, and, of, and other extremely common
# words. By specifying stop_words = 'english', we’re telling our
# vectorizer to filter out the built-in set of English stop words and
# vectorize only less common, more informative words.

vctrz = TfidfVectorizer(ngram_range = (1, 1),tokenizer = normalize,
stop_words = 'english')



# Now, let’s configure what our chatbot will be able to talk about.
# Here, it will be able to talk about the chapters of this book, so
# we’ll create a list that contains very simple descriptions of each
# chapter. In this context, each string will be one of our
# documents.


alldocuments = ['Chapter 1. The algorithmic approach to problem solving, including Galileo and baseball.',
 'Chapter 2. Algorithms in history, including magic squares, Russian peasant multiplication, and Egyptian methods.',
 'Chapter 3. Optimization, including maximization, minimization, and the gradient ascent algorithm.',
 'Chapter 4. Sorting and searching, including merge sort, and algorithm runtime.',
 'Chapter 5. Pure math, including algorithms for continued fractions and random numbers and other mathematical ideas.',
 'Chapter 6. More advanced optimization, including simulated annealing and how to use it to solve the traveling salesman problem.',
 'Chapter 7. Geometry, the postmaster problem, and Voronoi triangulations.',
 'Chapter 8. Language, including how to insert spaces and predict phrase completions.',
 'Chapter 9. Machine learning, focused on decision trees and how to predict happiness and heart attacks.',
 'Chapter 10. Artificial intelligence, and using the minimax algorithm to win at dots and boxes.',
 'Chapter 11. Where to go and what to study next, and how to build a chatbot.']


# We’ll continue by fitting our TFIDF vectorizer to these chapter
# descriptions, which will do the document processing to get us
# ready to create TFIDF vectors whenever we wish. We don’t
# have to do this manually, since there’s a fit() method defined
# in the scikit-learn module:
vctrz.fit(alldocuments)


# Now, we’ll create TFIDF vectors for our chapter descriptions
# and for a new query asking for a chapter about sorting and
# searching:
query = 'I want to read about how to search for items.'
tfidf_reports = vctrz.transform(alldocuments).todense()
tfidf_question = vctrz.transform([query]).todense()

# Our new query is a natural English language text about
# searching. The next two lines use the built-in translate() and
# todense() methods to create the TFIDF vectors for the chapter
# descriptions and the query.



# If the vectors are very similar to each other, the
# angle between them will be quite small. If the vectors are very
# different, the angle will be large. It’s strange to think that we
# can compare English language texts by finding the “angle”
# between them, but this is precisely why we created our numeric
# TFIDF vectors—so that we can use numeric tools like angle
# comparison for data that doesn’t start out numeric.