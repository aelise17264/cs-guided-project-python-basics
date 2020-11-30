def csAlphanumericRestriction(input_str):
    if input_str.isalpha() or input_str.isnumeric():
        return True

    else:
        return False

print (csAlphanumericRestriction("Bold"))
print (csAlphanumericRestriction("123454321"))
print (csAlphanumericRestriction("H3LL0"))