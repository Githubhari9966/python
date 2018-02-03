#define the variable
def students():
    #the student list from the python class
    python=['vivek','arvind','mourya','hari','navya']
    #student list from the web application class
    webapplication=['vivek','hari','rahul']
    #the common students in the bith classes are stored into the varible a
    a=list(set(python).intersection(set(webapplication)))

    print('common students in both python and web application are')
    #print a
    print(a)
   #the union operator here joining thr students present in both classes
    b=list(set(python).union(set(webapplication)))
    #it gives the result of students who are not common in both classes
    c=list(set(b).difference(set(a)))
    print('the list of students who are not common in both the classes are')
    print(c)
students()