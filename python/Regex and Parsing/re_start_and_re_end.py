import re

def find_substring_indices(text, pattern):
    regex = re.compile(pattern)
    
    results = []
    for i in range(len(text)):
        match = re.match(regex, text[i:])
        if match:
            start_index = i + match.start()
            end_index = i + match.end() - 1
            results.append((start_index, end_index))

    return results if results else [(-1, -1)]

text = input().strip()
pattern = input().strip()

indices = find_substring_indices(text, pattern)

for idx in indices:
    print(idx)
