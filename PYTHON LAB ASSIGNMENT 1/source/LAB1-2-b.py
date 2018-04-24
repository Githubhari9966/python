 #defining the sentence
def reverseWordSentence(Sentence):

    # Seperate the given sentence into list of words.
    words = Sentence.split(" ")

    # Reversing each word and creating the new list
    newWords = [word[::-1] for word in words]

    # Joining the new list of words
    # to for a new Sentence
    newSentence = " ".join(newWords)

    return newSentence

#take the input from the customer
Sentence = input("please enter the sentence\n")
# print the result reverse sentence
print("Reversed sentence is:", reverseWordSentence(Sentence))
