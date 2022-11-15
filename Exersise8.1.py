#Exercise 1: Write a function called chop that takes a list and
 #modifies it, removing the first and last elements, and returns None. 
 #Then write a function called middle that takes a list and returns a
 # new list that contains all but the first and last elements.

# By Zackary Paulson


def chop():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    print(list1[1:-1])
   

def middle():
    list2 = [11,22,33,44,55,66,77,88,99,100]
    newList = list2[1:-1]
    return newList

chop()
print(middle())