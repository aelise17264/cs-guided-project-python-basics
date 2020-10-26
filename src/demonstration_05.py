"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # Your code here
    
    #sort method defaults to sorting strings in alphabetical order
    # that's now what we want in this case
    # we need to tell the sort method how we want it to work
    #sort has a param called key which allows us to specify what we want to sort by
    lst.sort(key = len)

    return lst
print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["may", "april", "september", "august", "jun"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length([]))

#? what if 2 things have the same length
# If they're the same length, it will leave them in the same relative order
# We could sort twice to get it to sort by multiple parameters.