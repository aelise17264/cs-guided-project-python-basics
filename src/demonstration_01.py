"""
Challenge #1:

Create a function that takes two numbers as arguments and return their sum.

Examples:
- addition(3, 2) ➞ 5
- addition(-3, -6) ➞ -9
- addition(7, 3) ➞ 10
"""
def addition(a: int, b: int) -> int: #we can anotate input params w/ types
    # Your code here
    #given 2 ints as input
    # we want to add them together `+`
    #return the result of the operation(very important) to make the result available outside the function

    #regardless of what language we are working in we should be able to complete the instructions that are given to us

    answer = a + b

    return answer
    
print(addition(5, 6))