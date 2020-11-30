def csWhereIsBob(names):
    name = "Bob"
    this_list = names
    
    if (name in this_list) == False:
        return -1 
    else:
        return names.index(name)
print(csWhereIsBob(["Jimmy", "Layla", "Mandy"]))
print (csWhereIsBob(["Bob", "Nathan",  "Hayden"]))