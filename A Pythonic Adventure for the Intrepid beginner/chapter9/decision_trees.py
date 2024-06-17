# In this chapter, we explore machine
# learning. Machine learning refers to a broad
# range of methods, but they all share the
# same goal: finding patterns in data and
# using them to make predictions.



# Decision trees are diagrams that have a branching structure
# resembling a tree

# The process of creating a decision tree that
# leads to optimal decisions is a paradigmatic example of a
# machine learning algorithm.

# Triage is difficult because you have to make a reasonably
# accurate diagnosis with very little information or time

# binary branching process resembles a tree whose trunk
# branches into smaller offshoots until reaching the ends of the
# farthest branches


# If we could design a thorough, well-researched decision tree
# that always led to good triage decisions, it’s possible that
# someone without medical training could perform triage of
# heart attack patients, which would save every emergency room
# in the world plenty of money because they would no longer
# need to hire and train judicious, highly educated triage
# professionals.


# A good decision
# tree may even lead to better decisions than the average human
# would make, since it could potentially eliminate the
# unconscious biases that we fallible humans possess.

# The branching decision steps described in a decision tree
# constitute an algorithm. Executing such an algorithm is very
# simple: just decide which of the two branches you should be on
# at every node, and follow the branches to the end.



# Building a Decision Tree
# Machine learning algorithms find useful patterns in data, so
# they require a good dataset. We’ll use data from the European
# Social Survey (ESS) for our decision tree.

# we can use the pandas
# module to work with data, storing it in our Python session in a
# variable called ess:

import pandas as pd
ess = pd.read_csv('ess.csv')

# Remember, in order to read the CSV file, you’ll have to be
# storing it in the same place as you’re running Python from, or
# you’ll have to change 'ess.csv' in the previous snippet to
# reflect the exact filepath where you’re storing the CSV file. We
# can use the shape attribute of a pandas dataframe to see how
# many rows and columns are in our data:
print(ess.shape)


# The output should be (44387, 534), indicating that our dataset
# has 44,387 rows (one for each respondent) and 534 columns
# (one for each question in the survey). We can look more closely
# at some of the columns that interest us by using the pandas
# module’s slicing functions. For example, here’s how we look at
# the first five answers to the “happy” question:
print(ess.loc[:,'happy'].head())


# Here, the loc() function has sliced the variable called
# happy from the pandas dataframe. In other words, it takes out
# only that column and ignores the other 533. Then, the head()
# function shows us the first five rows of that column.


# Now one for social meetings:
print(ess.loc[:,'sclmeet'].head())


# We can
# restrict the ess data so that it contains only full responses for
# the variables we care about as follows:
ess = ess.loc[ess['sclmeet'] <= 10,:].copy()
ess = ess.loc[ess['rlgdgr'] <= 10,:].copy()
ess = ess.loc[ess['hhmmb'] <= 50,:].copy()
ess = ess.loc[ess['netusoft'] <= 5,:].copy()
ess = ess.loc[ess['agea'] <= 200,:].copy()
ess = ess.loc[ess['health'] <= 5,:].copy()
ess = ess.loc[ess['happy'] <= 10,:].copy()
ess = ess.loc[ess['eduyrs'] <= 100,:].copy().reset_index(drop=True)


# One of the simplest approaches is a binary split: we compare
# the happiness levels of people with highly active social lives to
# those of people with less active social lives

import numpy as np
social = list(ess.loc[:,'sclmeet'])
happy = list(ess.loc[:,'happy'])
low_social_happiness = [hap for soc,hap in zip(social,happy) if soc <= 5]
high_social_happiness = [hap for soc,hap in zip(social,happy) if soc > 5]

meanlower = np.mean(low_social_happiness)
meanhigher = np.mean(high_social_happiness)


# we imported the numpy module in order to
# calculate means. We defined two new variables, social and
# happy, by slicing them from the ess dataframe. Then, we used
# list comprehensions to find the happiness levels of all people
# with lower ratings of social activity (which we saved in the
# variable low_social_happiness) and the happiness levels of all
# people with higher ratings of social activity (which we saved in
# the variable high_social_happiness).

# Finally, we calculated the
# mean happiness rating of unsocial people (meanlower) and the
# mean happiness rating of highly social people (meanhigher)
print(meanlower, meanhigher)


# If their sclmeet value is 5
# or less, then we can predict that their happiness is 7.2. If it is
# higher than 5, then we can predict that their happiness is 7.8. It
# will not be a perfect prediction, but it’s a start and it’s more
# accurate than random guessing.



# In machine learning problems, there are a few different ways to
# measure accuracy. The most natural way is to find the sum of
# our errors. In our case, the error that interests us is the
# difference between our prediction of someone’s happiness
# rating and their actual happiness rating. If our decision tree
# predicts that your happiness is 6 but it’s actually 8, then that
# tree’s error for your rating is 2. If we add up the prediction
# errors for every respondent in some group, we can get an error
# sum that measures the decision tree’s accuracy for predicting
# the happiness of members of that group.

# This snippet shows a simple way to find the error sum:
# lowererrors = [abs(lowhappy - meanlower) for lowhappy in low_social_happiness]
# highererrors = [abs(highhappy - meanhigher) for highhappy in high_social_happiness]

# total_error = sum(lowererrors) + sum(highererrors)
# print(total_error)



def get_splitpoint(allvalues, predictedvalues):
    lowest_error = float('inf')
    best_split = None
    best_lowermean = np.mean(predictedvalues)
    best_highermean = np.mean(predictedvalues)

    for pctl in range(0, 100):
        split_candidate = np.percentile(allvalues, pctl)

        loweroutcomes = [outcome for value, outcome in zip(allvalues, predictedvalues) if value <= split_candidate]
        higheroutcomes = [outcome for value, outcome in zip(allvalues, predictedvalues) if value > split_candidate]

        if np.min([len(loweroutcomes), len(higheroutcomes)]) > 0:
            meanlower = np.mean(loweroutcomes)
            meanhigher = np.mean(higheroutcomes)

            lowererrors = [abs(outcome - meanlower) for outcome in loweroutcomes]
            highererrors = [abs(outcome - meanhigher) for outcome in higheroutcomes]

            total_error = sum(lowererrors) + sum(highererrors)

            if total_error < lowest_error:
                best_split = split_candidate
                lowest_error = total_error
                best_lowermean = meanlower
                best_highermean = meanhigher

    return best_split, lowest_error, best_lowermean, best_highermean

# allvalues = list(ess.loc[:,'hhmmb'])
# predictedvalues = list(ess.loc[:,'happy'])
# print(get_splitpoint(allvalues,predictedvalues))


# We’ll use the same principle we used to get optimal split points
# to decide the best split variable: the best way to split is the one
# that leads to the smallest error. In order to determine that, we
# need to iterate over each available variable and check whether
# splitting on that variable leads to the smallest error. We then
# determine which variable leads to the split with the lowest
# error.
# def getsplit(data,variables,outcome_variable):
#     best_var = ''
#     lowest_error = float('inf')
#     best_split = None
#     predictedvalues = list(data.loc[:,outcome_variable])
#     best_lowermean = -1
#     best_highermean = -1

#     for var in variables:
#         allvalues = list(data.loc[:,var])
#         splitted = get_splitpoint(allvalues,predictedvalues)

#         if(splitted[1] < lowest_error):
#             best_split = splitted[0]
#             lowest_error = splitted[1]
#             best_var = var
#             best_lowermean = splitted[2]
#             best_highermean = splitted[3]

#     generated_tree = [[best_var,float('-inf'),best_split,best_lowermean],[best_var,best_split, float('inf'),best_highermean]]

#     return(generated_tree)

# variables = ['rlgdgr','hhmmb','netusoft','agea','eduyrs']
# outcome_variable = 'happy'
# print(getsplit(ess,variables,outcome_variable))


# We’ve completed everything we need to make the best possible
# split at each branch point and generate a tree with two
# branches. Next, we need to grow the tree beyond just one
# branching node and two terminal nodes.


# The final step of our decision tree generation process is to
# specify a depth that we want to reach, and build new branches
# until we reach that depth. The way we accomplish this is by
# making the additions to our getsplit() function


def getsplit(depth,data,variables,outcome_variable):
    # Part1
    best_var = ''
    lowest_error = float('inf')
    best_split = None
    predictedvalues = list(data.loc[:,outcome_variable])
    best_lowermean = -1
    best_highermean = -1

    for var in variables:
        allvalues = list(data.loc[:,var])
        splitted = get_splitpoint(allvalues,predictedvalues)

        if(splitted[1] < lowest_error):
            best_split = splitted[0]
            lowest_error = splitted[1]
            best_var = var
            best_lowermean = splitted[2]
            best_highermean = splitted[3]
    generated_tree = [[best_var,float('-inf'),best_split,[]], [best_var, best_split,float('inf'),[]]]

    # Part2
    if depth < maxdepth:
        splitdata1=data.loc[data[best_var] <= best_split,:]
        splitdata2=data.loc[data[best_var] > best_split,:]
        if len(splitdata1.index) > 10 and len(splitdata2.index) > 10:
            generated_tree[0][3] = getsplit(depth + 1,splitdata1,variables,outcome_variable)
            generated_tree[1][3] = getsplit(depth + 1,splitdata2,variables,outcome_variable)
        else:
            depth = maxdepth + 1
            generated_tree[0][3] = best_lowermean
            generated_tree[1][3] = best_highermean
    else:
        generated_tree[0][3] = best_lowermean
        generated_tree[1][3] = best_highermean

    return(generated_tree)

# outcome_variable = 'happy'
# print(getsplit(0,ess,variables,outcome_variable))




# In order to generate our decision tree, we compared error rates
# for each potential split point and each potential splitting
# variable, and we always chose the variable and split point that
# led to the lowest error rate for a particular branch.


# It will be helpful
# for us to write code that can determine the predicted level of
# happiness for a person based on what we know about them
# from their ESS answers.
def get_prediction(observation,tree):
    j = 0
    keepgoing = True
    prediction = - 1
    while(keepgoing):
        j = j + 1
        variable_tocheck = tree[0][0]
        bound1 = tree[0][1]
        bound2 = tree[0][2]
        bound3 = tree[1][2]

        if observation.loc[variable_tocheck] < bound2:
            tree = tree[0][3]

        else:
            tree = tree[1][3]

        if isinstance(tree,float):
            keepgoing = False
            prediction = tree

    return(prediction)


# Next, we can create a loop that goes through any portion of our
# dataset and gets any tree’s happiness prediction for that
# portion.

predictions=[]
variables = ['rlgdgr','hhmmb','netusoft','agea','eduyrs']
outcome_variable = 'happy'
maxdepth = 4
thetree = getsplit(0,ess,variables,outcome_variable)
for k in range(0,30):
    observation = ess.loc[k,:]
    predictions.append(get_prediction(observation,thetree))

print(predictions)


# Finally, we can check how these predictions compare to the
# actual happiness ratings, to see what our total error rate is.
predictions = []
for k in range(0,len(ess.index)):
    observation = ess.loc[k,:]
    predictions.append(get_prediction(observation,thetree))

ess.loc[:,'predicted'] = predictions
errors = abs(ess.loc[:,'predicted'] - ess.loc[:,'happy'])
print(np.mean(errors))



# However, there is a danger that if we aren’t careful, we
# can encounter a common, dastardly peril called overfitting, the
# tendency of machine learning models to achieve very low error
# rates on the datasets used to create them (like data from the
# past) and then unexpectedly high error rates on other data (like
# the data that actually matters, from the future).

import numpy as np
np.random.seed(518)
ess_shuffled = ess.reindex(np.random.permutation(ess.index)).reset_index(drop = True)
training_data = ess_shuffled.loc[0:37000,:]
test_data = ess_shuffled.loc[37001:,:].reset_index(drop = True)
