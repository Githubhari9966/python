UMKC_bookstore = {"network communications":20, "analysis of algorithms":30, "introduction to statistical learning":50, "Regression analysis":80}
#avilable books in the umkc bookstore
list = []
min = int(input("Please enter the minimum price of the book"))#take the minimum price from the user
max = int(input("Please enter the maximum price of the book"))#take maximum price from the user
for (key,value) in UMKC_bookstore.items():#it run the FOR loop for the given key value pairs
    if value >= min and value <= max:
        list.append(key)#lists the key values in the dictionary
string = ','.join(list)# it create the list of books in the given price range
print("Available books for given price range are("+string+")")#it prints the list