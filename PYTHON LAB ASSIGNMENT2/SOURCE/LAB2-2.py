contact_list = [
{"name":"hari","ph_number":"0000000000","mail_id":"hnr@ymail.com"},
{"name":"rashmi","ph_number":"1111111111","mail_id":"rt@gmail.com"},
{"name":"arvind","ph_number":"2222222222","mail_id":"artt@gmail.com"},
{"name":"saria","ph_number":"3333333333","mail_id":"saria@mail.umkc.edu"}]# this is the list of dictionaries
#******** part 1********#
i = str(input("enter the contact name which you wants to get the information")) #take the input from the user
x = (next(item for item in contact_list if item["name"] == i))#checks the each dictionary item in the list to get the desired value of name
print(x)#print the contact information
#***********part 2***********#
j = str(input("enter the person's contact number which you want to get the information"))#'j' is loaded with contact number which we want to search
y = (next(item for item in contact_list if item["ph_number"] == j))# checks the user given mobile number with the all the mobile numbers in tall dictionary
print(y)#print the output



