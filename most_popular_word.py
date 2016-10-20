""" Attempts to find word with maximum similarity to other words """

WORD_SURVEY = 100

words = {}
with open('data/words.txt', 'r') as f:
    for line in f:
        words[line.strip()] = 0


def get_all(test_word):
    count = 0
    for i in range(0, len(test_word)):
        for word in words:
            if test_word[:i+1] == word[:i+1]:
                count += 1
    words[test_word] = count

for i, word in enumerate(words.keys()):
    if i > WORD_SURVEY:
        break
    print(str(round(float(i/WORD_SURVEY)*100, 2))+'%')
    get_all(word)
print()

sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
for word in reversed(sorted_words[:WORD_SURVEY]):
    print(word[1], '-', word[0])

print('\nBest Word: '+sorted_words[0][0]+', Score:', sorted_words[0][1])
