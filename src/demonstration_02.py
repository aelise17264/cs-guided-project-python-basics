"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes: int) -> int:
    # Your code here
    #there are 60 seconds in a min
    # we need to take `minutes` & multiply by 60 in order to perform the conversion
    # return the converted result
    seconds = minutes * 60

    return seconds

print(convert(5))