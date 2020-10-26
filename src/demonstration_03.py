"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt: str):
    # Your code here
    # Your code here
    #take the string input & convert it to an integer
    # the `int` function does this for us in python
    # call the `int` function, passing it the `txt` input
    #return the converted result
        if txt.isnumeric() is True:
            converted_int = int(txt)
            return converted_int
        else:
            return f"'{txt}' is not a valid number"

        return converted_int or f"'{txt}' is not a valid number"
                           # bool and bool
print(string_int("1000"))
print(string_int("hi"))