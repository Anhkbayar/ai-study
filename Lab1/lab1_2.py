import collections
from textblob import TextBlob
import string

sentence = """Ultra shorts - Our ever-popular long-cut, quick-drying Ultra Shorts use lightweight 50-denier 
polyester ripstop with a wicking finish to stay cool and comfortable, mile after mile. 
Pockets: two front drop-ins, two large"""

translator = str.maketrans('', '', string.punctuation)
clean_sentence = sentence.translate(translator)

words_list = clean_sentence.split()

unique_words = set(words_list)
print("Word counts:")
for word in unique_words:
    print(word, words_list.count(word))

word_counts = collections.Counter(words_list)
print("\nTop 10 words:")
print(word_counts.most_common(10))

ngram_object = TextBlob(sentence)

bigrams = ngram_object.ngrams(n=2)
print("\nBigrams:")
print(bigrams)

trigrams = ngram_object.ngrams(n=3)
print("\nTrigrams:")
print(trigrams)

    
