# Imagine that you are doing algorithm consulting work for a
# startup that is trying to add features to a search engine they are
# building. They want to add phrase completion so that they can
# provide search suggestions to users. For example, when a user
# types in peanutbutter and, a search suggestion feature might
# suggest adding the word jelly. When a user types in squash,
# the search engine could suggest both court and soup.


# An n-gram is simply a collection of n
# words that appear together. For example, the phrase “Reality is
# not always probable, or likely” is made up of seven words once
# spoken by the great Jorge Luis Borges.


# We’ll use a Python module called nltk to make n-gram
# collection easy. We’ll first tokenize our text. Tokenizing simply
# means splitting a string into its component words, ignoring
# punctuation.
# import numpy as np
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import sent_tokenize, word_tokenize
# text = "Time forks perpetually toward innumerable futures"
# print(word_tokenize(text))


# from nltk.util import ngrams
# token = nltk.word_tokenize(text)
# bigrams = ngrams(token,2)
# trigrams = ngrams(token,3)
# fourgrams = ngrams(token,4)
# fivegrams = ngrams(token,5)
# grams = [ngrams(token,2),ngrams(token,3),ngrams(token,4),ngrams(token,5)]
# print(grams)


# The brown corpus we used for space insertion
# won’t work because it consists of single words and so we can’t
# get its n-grams.

# import requests
# file = requests.get('http://www.bradfordtuckfield.com/shakespeare.txt')
# file = file.text
# text = file.replace('\n', '')

# token = nltk.word_tokenize(text)
# bigrams = ngrams(token,2)
# trigrams = ngrams(token,3)
# fourgrams = ngrams(token,4)
# fivegrams = ngrams(token,5)
# grams = [ngrams(token,2),ngrams(token,3),ngrams(token,4),ngrams(token,5)]




# In order to find the n + 1-grams that will constitute our search
# suggestions, we need to know how long the user’s search term
# is
# from nltk.tokenize import sent_tokenize, word_tokenize
# search_term = 'life is a'
# split_term = tuple(search_term.split(' '))
# search_term_length = len(search_term.split(' '))

# We will search for 4 word phrases
# from collections import Counter
# counted_grams = Counter(grams[search_term_length - 1])

# Search for most repeated fourgram
# print(list(counted_grams.items())[10])


# We need to find the subset of n + 1-grams
# whose first n elements match our search term. 
# matching_terms = [element for element in list(counted_grams.items()) if element[0][:-1] == tuple(split_term)]
# print(matching_terms)




# SELECTING A PHRASE BASED ON FREQUENCY
# if(len(matching_terms)>0):
#     frequencies = [item[1] for item in matching_terms]
#     maximum_frequency = np.max(frequencies)
#     highest_frequency_term = [item[0] for item in matching_terms if item[1] ==  maximum_frequency][0]
#     combined_term = ' '.join(highest_frequency_term)

# print(combined_term)





import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize

# Ensure the necessary NLTK data packages are downloaded
nltk.download('punkt')

import numpy as np
from collections import Counter

def search_suggestion(search_term, text):
    token = word_tokenize(text)
    
    # Create n-grams
    bigrams = list(ngrams(token, 2))
    trigrams = list(ngrams(token, 3))
    fourgrams = list(ngrams(token, 4))
    fivegrams = list(ngrams(token, 5))
    
    # Store n-grams in a list for easy access
    grams = [bigrams, trigrams, fourgrams, fivegrams]

    split_term = tuple(search_term.split(' '))
    search_term_length = len(split_term)

    # Get the correct n-gram based on the length of the search term
    if search_term_length - 1 < len(grams):
        counted_grams = Counter(grams[search_term_length - 1])
    else:
        return 'No suggested searches'
    
    matching_terms = [element for element in list(counted_grams.items()) if element[0][:-1] == split_term]
    
    if len(matching_terms) > 0:
        frequencies = [item[1] for item in matching_terms]
        maximum_frequency = np.max(frequencies)
        highest_frequency_term = [item[0] for item in matching_terms if item[1] == maximum_frequency][0]
        combined_term = ' '.join(highest_frequency_term)
    else:
        combined_term = 'No suggested searches'
    
    return combined_term

# Fetch the text file
import requests
file = requests.get('http://www.bradfordtuckfield.com/shakespeare.txt')
file = file.text
text = file.replace('\n', '')

# Example usage
print(search_suggestion("astonishing", text))