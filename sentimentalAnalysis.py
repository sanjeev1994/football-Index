from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk.tokenize import word_tokenize, RegexpTokenizer

headlines = set()

for i in range(5614):
    j = i+1
    file = open("/Users/sanjeev/Desktop/football-Index/Headlines/%d.text" % j , "r")
    lines = file.readline()
    print j
    headlines.add(lines)
    display.clear_output()
print len(headlines)
sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)
fixedIndex = len(results) - 1
print results[fixedIndex]


df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()

df2 = df[['headline', 'label']]
df2.to_csv('football_headlines_labels.csv', mode='a', encoding='utf-8', index=False)

#print(df.label.value_counts())
#
#print(df.label.value_counts(normalize=True) * 100)


checkScore = sia.polarity_scores("Tottenham 5-3 Chelsea: Two-goal Harry Kane inspires Spurs to victory in thriller at the Lane")
print "decent score"
print checkScore

fig, ax = plt.subplots(figsize=(8, 8))

counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

plt.show()


