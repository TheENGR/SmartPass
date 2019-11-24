def getAllowedTypes(numChars, rules):
    allowed = []
    for i in range(numChars):
        allowedOptions = "lower,upper,numerals,specialChars"
        for rule in rules["chardex"]:
            if rule["index"] == i:
                allowedOptions = allowedOptions.replace(rule["set"],'').replace(',,','')
        allowed.append(allowedOptions.strip(','))
    return allowed
