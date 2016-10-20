""" A word cloud of Hillary Clinton's emails """

import operator
import matplotlib.pyplot as plt

from wordcloud import WordCloud

BLACKLIST = ['with', 'on', 'for', 'after', 'at', 'by', 'in', 'against',
             'instead', 'of', 'near', 'between', 'as', 'off', 'from', 'under',
             'down', 'below', 'through', 'over', 'up', 'according', 'to',
             'across', 'beyond', 'above', 'about', 'behind', 'beside', 'into',
             'throughout', 'with', 'within', 'your', 'you', 'more', 'and',
             'yet', 'the', 'com', 'this', 'what', 'has', 'have', 'a', 'an',
             'is', 'are', 'it', 'we', 'he', 'him', 'his', 'they', 'i', 'h',
             'd', 'be', 'but', 'had', 'she', 'her', 'will', 'fw', 'that',
             'how', 'were', 'j', '&', '']

words = {}

with open("data/hillary_emails.csv", "r") as f:
    count = 0
    for line in f:
        if count > 1000:
            break
        count += 1

        for word in line.split():
            punct = " ,.?;:\"'()[]{}!/\\|-_=+`~"
            key = word.strip(punct).replace(',', '').lower()
            if key not in words.keys():
                words[key] = 1
            else:
                words[key] += 1

words = {k: v for k, v in words.items() if k not in BLACKLIST}

word_tuples = sorted(words.items(), key=operator.itemgetter(1), reverse=True)

text = ""
for word, count in word_tuples[:20]:
    print(word, '-', count)
    text += str(word+' ')*count+'\n'

wordcloud = WordCloud(max_font_size=40, relative_scaling=.1).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
