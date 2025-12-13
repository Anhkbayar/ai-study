import re
from nltk import bigrams, trigrams
from collections import Counter


with open("essay.txt","r", encoding="utf-8") as file:
    text = file.read()
    
words = re.findall(r"\w+", text.lower()) 

bigram_counts = Counter(bigrams(words))
print("Bigram counts:")
for pair, count in bigram_counts.items():
    print(pair, ":", count)

trigram_counts = Counter(trigrams(words))
print("\nTrigram counts:")
for triplet, count in trigram_counts.items():
    print(triplet, ":", count)