"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt:str):
    # Your code here
    # ?how do we keep track of the 'o's & 'x's
    # let's keep 2 variables, one that tracks the number of x's & the other tracks the number of o's
    #figure out the number of 'o's & 'x's in the input string
    xs = 0
    os = 0
    # we need to look at every character in the txt string
    #iterate over the txt 
        # if we see an x increment xs
        # if we see an o increment os
     #check if the number of 'o's & 'x's is the same
    # return true if they are, false otherwise

    for character in txt:
        if character == "x" or character == "X":
            xs += 1
        if character == "o" or character == "O":
            os += 1
    # if xs == os:
    #     return True
    # else:
    #     return False
    return xs == os

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))