from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

fw = open('sample.txt','w')
fw.write('hi hari how you doing man. \n')
fw.write('be prepared for anything. \n')
fw.write('hey hari cats are not dogs and money is not every thing.hi john how you doing man, you are planning to go to CA in the summer\n'
        '. hey I want to join with you \n ')
fw.close()

fr = open("sample.txt","r")
text = fr.read()
print(text)
fr.close()
print(sent_tokenize(text))
words = word_tokenize(text)
############################
print(words)
lemmatizers = ['NOUN LEMMATIZER', 'VERB LEMMATIZER']
lemmatizer_wordnet = WordNetLemmatizer()

formatted_row = '{:>24}' * (len(lemmatizers) + 1)
print('\n', formatted_row.format('WORD', *lemmatizers), '\n')
for word in words:
    lemmatized_words = [lemmatizer_wordnet.lemmatize(word, pos ='n'),
                        lemmatizer_wordnet.lemmatize(word, pos = 'v')]
    print(formatted_row.format(word, *lemmatized_words))


print("******************** bigrams part************************")
from nltk.util import ngrams
bigrams= list(ngrams(words,2))
print(bigrams)

import nltk
frequent_bigram = nltk.FreqDist(bigrams)
a = frequent_bigram.most_common(5)
print("top 5 bigrams in the given list of bigrams are\n",a)

concaten = ""
for i in a:
    p = i[0][0]
    q = i[0][1]
    with open('sample.txt',encoding = "utf-8")as f:
        for line in f.readlines():
            words = line.strip().split()
            for word1,word2 in zip(words,words[1:]):
                if word1==p and word2==q:
                    concaten = concaten + line
print(concaten)






