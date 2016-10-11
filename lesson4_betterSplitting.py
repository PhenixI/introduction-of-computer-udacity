# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    splitedStr = []
    strLen = len(source)
    i = 0
    strTmp = '';
    while i< strLen:
        index = splitlist.find(source[i])
        if(index==-1):
            strTmp += source[i]
        else:
            if(strTmp != ''):
                splitedStr.append(strTmp)
            strTmp = ''
        i += 1
    if strTmp != '':
        splitedStr.append(strTmp)
    return splitedStr
