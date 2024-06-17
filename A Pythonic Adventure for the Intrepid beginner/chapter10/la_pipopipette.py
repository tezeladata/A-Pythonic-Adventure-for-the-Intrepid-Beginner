import matplotlib.pyplot as plt
from matplotlib import collections as mc

# The term artificial intelligence has an aura about it that can
# make people think that it’s mysterious and highly advanced.

# The AI that we’ll build is much simpler and will be capable of
# playing a game well, but not of writing sincerely felt love poems
# or feeling despondency or desire (as far as I can tell!).



# Our AI will be able to play dots and boxes, a simple but
# nontrivial game played worldwide. We’ll start by drawing the
# game board. Then we’ll build functions to keep score as games
# are in progress. Next, we’ll generate game trees that represent
# all possible combinations of moves that can be played in a
# given game. Finally, we’ll introduce the minimax algorithm, an
# elegant way to implement AI in just a few lines.

# A player’s goal in dots and boxes is to draw line segments that
# complete squares.



# Though not strictly necessary for our algorithmic purposes,
# drawing the board can make it easier to visualize the ideas
# we’re discussing. A very simple plotting function can make an
# n×n lattice by looping over x and y coordinates and using the
# plot() function in Python’s matplotlib module:



# def drawlattice(n,name):
#     for i in range(1,n + 1):
#         for j in range(1,n + 1):
#             plt.plot(i,j,'o',c = 'black')

#     plt.savefig(name)


# In this code, n represents the size of each side of our lattice, and
# we use the name argument for the filepath where we want to
# save the output. The c = 'black' argument specifies the color
# of the points in our lattice. We can create a 5×5 black lattice
# and save it with the following command:
# drawlattice(5, "lattice.png")


# we can represent the line
# between (1,2) and (1,1) as this list:
# [(1,2),(1,1)]



# We can add to our drawlattice() function to create a
# drawgame() function. This function should draw the points of
# the game board as well as all line segments that have been
# drawn between them in the game so far. The function in Listing
# 10-1 will do the trick.

# All of the lines:
game = [[(1,2),(1,1)],[(3,3),(4,3)],[(1,5),(2,5)],[(1,2),(2,2)], [(2,2),(2,1)],[(1,1),(2,1)], [(3,4),(3,3)],[(3,4),(4,4)]]


def drawgame(n,name,game):
    colors2 = []
    for k in range(0,len(game)):
        if k%2 == 0:
            colors2.append('red')
        else:
            colors2.append('blue')

    lc = mc.LineCollection(game, colors = colors2, linewidths = 2)
    fig, ax = plt.subplots()
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            plt.plot(i,j,'o',c = 'black')

    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    plt.savefig(name)

# Calling our function
drawgame(5,'gameinprogress.png',game)



# Next, we’ll create a function that can keep score for a dots and
# boxes game. We start with a function that can take any given
# game and find the completed squares that have been drawn,
# and then we create a function that will calculate the score.

def squarefinder(game):
    countofsquares = 0


    for line in game:
        parallel = False
        left=False
        right=False

        if line[0][1]==line[1][1]:
            if [(line[0][0],line[0][1]-1),(line[1][0],line[1][1] -1)] in game:
                parallel=True
            
            if [(line[0][0],line[0][1]),(line[1][0]-1,line[1][1] -1)] in game:
                left=True

            if [(line[0][0]+1,line[0][1]),(line[1][0],line[1][1] -1)] in game:
                right=True

            if parallel and left and right:
                countofsquares += 1

    return(countofsquares)


# You can see that the function returns the value of
# countofsquares, which we initialized with a 0 value at the
# beginning of the function. The function’s for loop iterates over
# every line segment in a game.

# If a given line is a horizontal line, we check
# for the existence of those parallel, left, and right lines. If all four
# lines of the square we’ve checked are listed in the game, then
# we increment the countofsquares variable by 1. In this way,
# countofsquares records the total number of squares that have
# been completely drawn in the game so far.



# Now we can write a short function to calculate the score of a
# game. The score will be recorded as a list with two elements,
# like [2,1].

def score(game):
    score = [0,0]
    progress = []
    squares = 0

    for line in game:
        progress.append(line)
        newsquares = squarefinder(progress)
        if newsquares > squares:
            if len(progress)%2 == 0:
                score[1] = score[1] + 1
            else:
                score[0] = score[0] + 1
        squares=newsquares

    return(score)

print(score(game))







# The essence of a winning strategy is simply to
# systematically analyze the future consequences of our current
# actions, and to choose the action that will lead to the best
# possible future.

# Considering these possibilities, within two moves the game
# could be at any of three different scores: 1–1, 0–2, or 0–1. In
# this tree, it’s clear that we should choose the left branch,
# because every possibility that grows from that branch leads to a
# better score for us than do the possibilities growing from the
# right branch. This style of reasoning is the essence of how our
# AI will decide on the best move. It will build a game tree, check
# the outcomes at all terminal nodes of the game tree, and then
# use simple recursive reasoning to decide what move to make, in
# light of the possible futures that decision will open up.



# Remember that in Chapter 9 we had
# to select a variable and a split point to decide every branch in
# the tree. Here, knowing what branches will come next is easy,
# since there will be exactly one branch for every possible move.
# All we need to do is generate a list of every possible move in our
# game. We can do this with a couple of nested loops that
# consider every possible connection between points in our
# lattice:


allpossible = []
gamesize = 5
for i in range(1,gamesize + 1):
    for j in range(2,gamesize + 1):
        allpossible.append([(i,j),(i,j - 1)])

for i in range(1,gamesize):
    for j in range(1,gamesize + 1):
        allpossible.append([(i,j),(i + 1,j)])




# If you think about a game that’s in progress, like the game
# illustrated in Figure 10-2, you’ll realize that not every move is
# always possible. If a player has already played a particular
# move during a game, no player can play that same move again
# for the rest of the game. We’ll need a way to remove all moves
# that have already been played from the list of all possible
# moves, resulting in a list of all possible moves remaining for
# any particular in-progress game. This is easy enough:

for move in allpossible:
    if move in game:
        allpossible.remove(move)


# game tree structure:
# full_tree = [[[(4,4),(4,3)],[[(1,3),(2,3)],[(3,1),(4,1)]]],[[(1,3), (2,3)],[[(4,4),(4,3)],[(3,1),(4,1)]]]]


# Instead of writing out game trees manually, we can build a
# function that will create them for us. It will take our list of
# possible moves as an input and then append each move to the
# tree

# def generate_tree(possible_moves,depth,maxdepth):
#     tree = []
#     for move in possible_moves:
#         move_profile = [move]
#         if depth < maxdepth:
#             possible_moves2 = possible_moves.copy()
#             possible_moves2.remove(move)
#             move_profile.append(generate_tree(possible_moves2,depth + 1,maxdepth))
#         tree.append(move_profile)


#     return(tree)


# This function, generate_tree(), starts out by defining an empty
# list called tree. Then, it iterates over every possible move. For
# each move, it creates a move_profile. At first, the move_profile
# consists only of the move itself. But for branches that are not
# yet at the lowest depth of the tree, we need to add those moves’
# children. We add children recursively: we call the
# generate_tree() function again, but now we have removed one
# move from the possible_moves list. Finally, we append the
# move_profile list to the tree.

# allpossible = [[(4,4),(4,3)],[(4,1),(5,1)]]
# thetree = generate_tree(allpossible,0,1)
# print(thetree)


# Next, we’ll make two additions to make our tree more useful:
# the first records the game score along with the moves, and the
# second appends a blank list to keep a place for children

def generate_tree(possible_moves,depth,maxdepth,game_so_far):
    tree = []
    for move in possible_moves:
        move_profile = [move]
        game2 = game_so_far.copy()
        game2.append(move)
        move_profile.append(score(game2))
        if depth < maxdepth:
            possible_moves2 = possible_moves.copy()
            possible_moves2.remove(move)
            move_profile.append(generate_tree(possible_moves2,depth +
            1,maxdepth,game2))
        else:
            move_profile.append([])
        tree.append(move_profile)

    return(tree)

allpossible = [[(4,4),(4,3)],[(4,1),(5,1)]]
thetree = generate_tree(allpossible,0,1,[])
print(thetree)




# The algorithm we’ll use for choosing a winning strategy is
# called minimax (a combination of the words minimum and
# maximum), so called because while we’re trying to maximize
# our score in the game, our opponent is trying to minimize our
# score. The constant fight between our maximization and our
# opponent’s minimization is what we have to strategically
# consider as we’re choosing the right move.



# The reasoning process we just went through is known as the
# minimax algorithm. Our decision in the present is about
# maximizing our score. But in order to maximize our score, we
# have to consider all the ways that our opponent will try to
# minimize our score. So the best choice is a maximum of
# minima.

# the minimax code starts at the top of the tree. It
# calls itself recursively on each of its child branches. The child
# branches, in turn, call minimax recursively on their own child
# branches. This recursive calling continues all the way to the
# terminal nodes, where, instead of calling minimax again, we
# calculate the game score for each node. So we’re calculating the
# game score for the terminal nodes first; we’re starting our game
# score calculations in the far future. These scores are then
# passed back to their parent nodes so that the parent nodes can
# calculate the best moves and corresponding score for their part
# of the game. These scores and moves are passed back up
# through the game tree until arriving back at the very top, the
# parent node, which represents the present.


import numpy as np
def minimax(max_or_min,tree):
    allscores = []
    for move_profile in tree:
        if move_profile[2] == []:
            allscores.append(move_profile[1][0] - move_profile[1][1])
        else:
            move,score=minimax((-1) * max_or_min,move_profile[2])
            allscores.append(score)
            
    newlist = [score * max_or_min for score in allscores]
    bestscore = max(newlist)
    bestmove = np.argmax(newlist)
    return(bestmove,max_or_min * bestscore)

# let’s define the game, and get all possible moves, using exactly
# the same code we used before:

allpossible = []
game = [[(1,2),(1,1)],[(3,3),(4,3)],[(1,5),(2,5)],[(1,2),(2,2)], [(2,2),(2,1)],[(1,1),(2,1)], [(3,4),(3,3)],[(3,4),(4,4)]]
gamesize = 5

for i in range(1,gamesize + 1):
    for j in range(2,gamesize + 1):
        allpossible.append([(i,j),(i,j - 1)])

for i in range(1,gamesize):
    for j in range(1,gamesize + 1):
        allpossible.append([(i,j),(i + 1,j)])
for move in allpossible:
    if move in game:
        allpossible.remove(move)

thetree = generate_tree(allpossible,0,3,game)
move,score = minimax(1,thetree)
print(thetree[move][0])
