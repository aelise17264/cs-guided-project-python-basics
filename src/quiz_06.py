def csMakeItJazzy(chords):
    ogList = chords
    # magicNumber = '7'
    # for chord in chords:           
    if any('7' in word for word in chords):
        return ogList
    else:
        newChords = [i + '7' for i in chords]
        return newChords
print (csMakeItJazzy(["G", "F", "C"]))
print(csMakeItJazzy(["G7", "F7", "C7"]));
 