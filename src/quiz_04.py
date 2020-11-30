def csSquareAllDigits(n):
    intiger = ''
    for digit in str(n):
        intiger += str(int(digit)**2)
    return int(intiger)
print (csSquareAllDigits(9119))
print (csSquareAllDigits(2483))