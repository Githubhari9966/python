def mymain():
    #import remainder
 m = input("Enter the sentence\n")
 p = m.split()
 n = len(m.split())
print ("number of words",n)
remainder = n % 2
if remainder == 1:
    print("middle word is \n",p[int((n-1)/2)])
else:
    print("middle words are\n",p[int((n-2)/2)],p[int(n/2)])