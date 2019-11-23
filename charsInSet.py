def charsInSet(old, new):
    retVal = ""
    for i in new:
        if i in old and i not in retVal:
            retVal += i
    return retVal
