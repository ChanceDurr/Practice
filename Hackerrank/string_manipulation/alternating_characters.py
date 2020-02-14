'''
You are given a string containing characters A and B only. Your task is to
change it into a string such that there are no matching adjacent characters.
To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
'''

import sys

def alternatingCharacters(s):
    s = list(s)
    count = 0
    for i in range(len(s)-1, 0, -1):
        if s[i] == s[i-1]:
            count += 1
            del s[i]
    
    return count

s = sys.argv[1]

print('Characters to remove: ', alternatingCharacters(s))