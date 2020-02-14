'''
Sherlock considers a string to be valid if all characters of the string appear
the same number of times. It is also valid if he can remove just 1 character
at 1 index in the string, and the remaining characters will occur the same
number of times. Given a string s, determine if it is valid. If so, return YES,
otherwise return NO.
'''

import sys

def isValid(s):
    counts = {}
    for i in set(s):
        counts[i] = s.count(i)

    if len(set(counts.values())) > 2:
        return 'NO'

    if len(set(counts.values())) == 1:
        return 'YES'

    if len(set(counts.values())) == 2:
        for i in range(len(counts.values())):
            temp = list(counts.values())
            if temp[i] == 1:
                del temp[i]
                if len(set(temp)) == 1:
                    return 'YES'
            else:
                temp[i] -= 1
                if len(set(temp)) == 1:
                    return 'YES'
        return 'NO'

s = sys.argv[1]
print('Is string valid? ', isValid(s))