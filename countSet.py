def countBySet(password, rules):
    data = {}
    sets = ['lower','upper','numerals','specialChars']
    for s in sets:
        count = 0
        for letter in password:
            if letter in rules[s]:
                count+=1
        data[s] = count
    return data
