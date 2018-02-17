import numpy as np# importing the "numpy" library as np
n = np.random.randint(0, 20, 15)# this generate the random integer set between 0 to 20 with the size of 15
print("The generated array is:\n")#it prints the integer set
print(n)
print("Most frequent value in the above array:\n")
print(np.bincount(n).argmax())#it will find the number which comes maximum number of times