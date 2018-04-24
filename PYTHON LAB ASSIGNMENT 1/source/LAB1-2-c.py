#defining the variable
def Largest_word(Sentence):
#the words in the sentence are splitted and stored in the variable "large"
    large = Sentence.split()
#sort the words present in the "large" variable according to the length
    large.sort(key=len, reverse=True)
#return the word which has index 0
    return large[0]
#take the input from the user
Sentence = input("Enter a sentence\n")
#print the largest word
print("Largest Word:",Largest_word(Sentence))

