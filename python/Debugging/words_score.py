n = int(input())
words = input()

vowels = "aeiouy"
score = 0

for word in words.split():
    vowel_count = sum(1 for letter in word if letter in vowels)
    if vowel_count % 2 == 0:
        score += 2
    else:
        score += 1

print(score)