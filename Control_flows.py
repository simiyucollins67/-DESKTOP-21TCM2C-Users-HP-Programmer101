i=20 
if (i<15):
    print("i is smaller than 15")
    print("I am in the if block")
else:
    print("i is greater than 15")
    print("i'm in the else block")
"pyhton if else statement in a list comprehension"
def digitSum(n):
    dsum=0
    for ele in str(n):
        dsum +=int(ele)
        return dsum
    #initializing list
    List=[367, 111, 562, 945, 6726, 873]
    #Using the funtion on odd elements of the list
    newList=[digitSum(i) for i in List if i & 1]
    #Displaying new list
    print(newList)
