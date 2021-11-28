
# Problem

#* Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting.
# He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
# The words in his note are case-sensitive and he must use only whole words available in the magazine.
# He cannot use substrings or concatenation to create the words he needs.
# Given the words in the magazine and the words in the ransom note, print 'Yes' if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print 'No'.
# 
# Example:
# magazine = "attack at dawn" note = "Attack at dawn".
# The magazine has all the right words, but there is a case mismatch. The answer is 'No'.
# 
# Function Description:
# Complete the checkMagazine function in the editor below. It must print 'Yes' if the note can be formed using the magazine, or 'No'.
# checkMagazine has the following parameters:
# string magazine[m]: the words in the magazine
# string note[n]: the words in the ransom note
# Prints
# string: either 'Yes' or 'No', no return value is expected#

def checkMagazine(magazine, note):
    # create two dictionaries with the arrays
    mdic = {}
    ndic = {}
    for m in magazine:
        if mdic.get(m) == None:
            mdic[m] = 1
        else:
            mdic[m] += 1
    for n in note:
        if ndic.get(n) == None:
            ndic[n] = 1
        else:
            ndic[n] += 1
    # now check if the value of all ndic keys are less or equal than the ones in mdic
    for k in ndic.keys():
        if mdic.get(k) == None:
            return print("No")
        elif mdic[k] < ndic[k]:
            return print("No")
    return print("Yes")


