def csSchoolYearsAndGroups(years, groups):
    alphaGroup = 'abcdefghijklmnopqrstuvwxyz'
    
    group = 0
    year = 0

    final = []

    for i in range(0, years * groups):
        if i % groups == 0:
            year += 1
            group = 0
        final.append(f'{year}{alphaGroup[group]}')

        group += 1

    return ', '.join(final)


    
print (csSchoolYearsAndGroups(7, 4))
