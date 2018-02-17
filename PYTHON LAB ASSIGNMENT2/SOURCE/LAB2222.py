contact_list = [
{"name":"hari","ph_number":"5698741230","mail_id":"hnr@ymail.com"},
{"name":"rashmi","ph_number":"1234567890","mail_id":"rt@gmail.com"},
{"name":"arvind","ph_number":"1234567888","mail_id":"artt@gmail.com"},
{"name":"saria","ph_number":"9874563210","mail_id":"saria@mail.umkc.edu"},
{"name":"bala","ph_number":"0123012301","mail_id":"bala@gmail.com"}]#contact list
#********** part 3 ********************#
i = str(input("enter the contact name which you wants to modify their number"))#user will enter the name of the person he wants to modify their number
current_dict= (next(item for item in contact_list if item["name"] == i))#it checks all the dictionaries present in the dictionaries present in the list
print(current_dict)#it prints the dictionary which the user searching
def replace_value_with_new_phone(ph_number, new_phone):#defining the variables
    for key in current_dict.keys():#FOR loop is working to check all the keys present in the dictionary
        if key == ph_number:#'if' the condition key is same as phone number
            current_dict[key] = new_phone

new_phone_number = input("enter the new phone number") #new variable creating for updating mobile number
replace_value_with_new_phone('ph_number', new_phone_number)#it replaces the old phone number with new mobile number
print(current_dict)#print the dictionary with the updated mobile number
print(contact_list)#print contact list which with the updated mobile number
#************************* part 4 ***********************#
exit(print("now exit was done")) #exit the code by printing the " now exit was done"
