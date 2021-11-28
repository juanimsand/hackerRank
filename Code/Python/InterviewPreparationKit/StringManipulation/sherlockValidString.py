
# Problem

#* Sherlock considers a string to be valid if all characters of the string appear the same number of times.
# It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
# Example
# s = abc
# This is a valid string because frequencies are {a:1, b:1, c:1}.
# s = abcc
# This is a valid string because we can remove one c and have 1 of each character in the remaining string.
# s = abccc
# This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a:1, b:1, c:2}.
# Function Description:
# Complete the isValid function in the editor below.
# isValid has the following parameter(s):
# string s: a string
# Returns:
# string: either YES or NO#

# Example for not valid string s = "mariana"
def validString1 (s):
    # create a dictionary
    dic={}
    for c in s:
        if c in dic.keys():
            dic[c] += 1
        else:
            dic[c] = 1
    
    # If got the dictionary dic = {'m': 1, 'a': 3, 'r': 1, 'i': 1, 'n': 1}
    # compare two keys, if the values are not equal i check if the difference is 1 or -1
    # if it is, i need to look for a third key and its value I should compare it as same way that was before
    # for example i could make the difference (diff = dic.values()[2] - dic.values()[1]), then it should be done
    # diff = dic.values()[3] - dic.values()[1].
    # If the difference is the same as before (-1 or 1) we continue but now, with only one valid value for the rest of keys.
    # An example of this: dic = {'m': 2, 'a': 1, 'e': 3}
    # diff1 = 1 - 2 = -1
    # diff2 = 3 - 2 = 1
    # So we know that it is not a valid string because be need to change at least 2 keys
    # Another example: dic = {'m': 2, 'a': 1, 'e': 1}
    # diff1 = 1 - 2 = -1
    # diff2 = 1 - 2 = -1
    # so the differences are equals (-1) then I know that the rest of values must be the same as 2nd and 3rd key (value = 1)
    
    
    # EXAMPLE: dic = {'p': 2, 'k': 2, 'l': 1, 'm': 2, 'a': 1, 'e': 2}
    values = []
    for v in dic.values():
        values.append(v)
    print(values)
    # EXAMPLE: values = [2, 2, 2, 2, 2, 2]
    if len(values) < 2:
        return "YES"
    elif len(values) == 2:
        # Compare just the two values
        diff = values[0] - values[1]
        if diff < 2 and diff > -2:
            return "YES"
        else:
            return "NO"
    else:   # len(values) >= 3
        i = 0
        while i < (len(values) - 2):    # len(values) - 2 = 4
            diff1 = values[i + 1] - values[i]
            diff2 = values[i + 2] - values[i]
            if diff1 == 0 and diff2 == 0:
                i += 1
            else:   # diff1 = diff2 then i need to check if that difference is between 1 and -1
                if abs(diff1) > 1 or abs(diff2) > 1:
                    return "NO"
                else:   # check if diff1 and diff2 are equals, if so, then to next item to final must be equal to them
                    if diff1 == diff2:
                        for j in range(i+3, len(values) - 1):
                            if values[j] != values[i+1]:    # values[i+2]
                                return "NO"
                        return "YES"
                    else:   #[diff1 = 1, diff2 = 0] [diff1 = 1, diff2 = -1] [diff1 = 0, diff2 = 1] [diff1 = 0, diff2 = -1] [diff1 = -1, diff2 = 1] [diff1 = -1, diff2 = 0]
                        if (diff1 == 1 and diff2 == -1) or (diff1 == -1 and diff2 == 1):
                            return "NO"
                        else:   # [diff1 = 1, diff2= 0] [diff1 = 0, diff2 = 1] [diff1 = 0, diff2 = -1] [diff1 = -1, diff2 = 0]
                            # so we need to if after those values the rest is same as values[i]
                            for j in range(i + 3, len(values)):
                                if values[j] != values[i]:
                                    return "NO"
                                else:
                                    return "YES"
        # One last step
        diff = values[len(values) - 1] - values[len(values) - 2]
        if abs(diff) <= 1:
            return "YES"
        else:
            return "NO"
        
def validString2(s):
    
    if len(s) == 0:
        return "NO"
    elif len(s) == 1:
        return "YES"
    
    dic = {}
    for c in s:
        if c in dic.keys():
            dic[c] += 1
        else:
            dic[c] = 1
    # If got the dictionary
    
    # Extract the max nd min values in dic, if the difference is 0, "YES", if it 2 or greater "NO", if it is 1, it could be
    # another key with same amount "YES", but only of max or min, if there is more values of max AND min, "NO"
    values = []
    for v in dic.values():
        values.append(v)
    
    # Extracting the max value
    maximo = max(values)
    minimo = min(values)
    diff = maximo - minimo
    if diff == 0:
        return "YES"
    elif diff > 1:
        return "NO"
    else:
        countMaxs = values.count(maximo)
        countMins = values.count(minimo)
        if countMaxs > 1 and countMins > 1:
            return "NO"
        else:
            return "YES"
        
def main():
    #s = "ppkklmmaaee"
    s = "aabbcd"
    #print(validString1(s))
    print(validString2(s))

main()