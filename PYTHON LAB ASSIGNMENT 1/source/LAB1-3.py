def func(a,n):# function define
    found  = False # here by default finding the triplet in the list as False
    for p in range(0, n-2): # the value of p checks the range from 0 to (n-1)
        for q in range(p +1, n - 1):# it also check the range
            for r in range(q +1, n):#it also check r range
                if (a[p] +a[q] + a[r] ==0): # if the sum is zero
                    print(a[p],a[q],a[r])# print those triplets
                    found = True# after that by default found is loaded with True
    if(found == False):# if this condition is true it prints no 'triplets'
        print("no triplets")
a = [0,2,1,-1,-2,-3,3]
n = len(a)
func(a,n)



