import re

def find_vowel_substrings(s):
    pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
    matches = re.findall(pattern, s)
    
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)

s = input()
find_vowel_substrings(s)