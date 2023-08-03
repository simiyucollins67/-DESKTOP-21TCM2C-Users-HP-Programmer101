#i=20 
#if (i<15):
    #print("i is smaller than 15")
   # print("I am in the if block")
#else:
  #  print("i is greater than 15")
   # print("i'm in the else block")
#pyhton if else statement in a list comprehension"
#def digitSum(n):
  #  dsum=0
  #  for ele in str(n):
      #  dsum +=int(ele)
    #    return dsum
    #initializing list
   # List=[367, 111, 562, 945, 6726, 873]
    #Using the funtion on odd elements of the list
   # newList=[digitSum(i) for i in List if i & 1]
    #Displaying new list
   # print(newList)
#Python program to illustrate iterating over a list
#l=["geeks", "for", "geeks"]
#for i in l:
 #   print(i)
  #  #Iterating over dictionary print("Dictonary Iteration")
#d=dict()
#['xyz']=123
#d['abc']=345
#for i in d:
 #   print("% s % d"%(i, d[i]))
#s="Geeks"
#for i in s:
 #   print(i)
#Continue statement 
#Prints all letters except 'e' and 's' for letter in 'geeksforgeeks'"
#Work more on continue, break and pass. Also work on dictionary data types and practice more on lists and loops"
#python program show range basics and prints out  number 
#for i in range(10):
 #   print(i, end="")
  #  sum=0
   # for i in range(1, 10):
    #    sum=sum+i
     #   print(i)
#print("\nThe sum of the first 10 numbers is :",sum)
#for i in range(0,100):
    #i=i+1
   # print(i)
#for i in range(0, 100):
 #   sum= i
  #  sum=sum+sum
#print("The sum is:", sum)
#print(f"The list of 100 numbers is:", i)
#Python program to illustrate while loop
#count =0
#while (count<3):
#count =count+1
  #  print("Hello Geek")
#Check if list contains any element
#a=[1, 2, 3, 4, 5]
#while a:
 #   print(a.pop())
#count=0
#while(count<5): count +=1; print ("Hello Geek")
#prints all letters except e and s
#i=0
#a="geeksforgeeks"
#while i<len(a):
 #   if a[i]=='e' or a[i]=='s':
  #      i +=1
   #     continue
    #print('current Letter:', a[i])
    #i +=1
#i=0
#b=[0,3,4,5,6,7,8,6,5,4]
#while i<len(b):
 # if 0<=b[i] or b[i]<=10:
  #  i +=1
   # continue
#print('The current number is:', b)
#i +=1
#pass statement used to write empty loops
#An empty loop
#a="geeksforgeeks"
#i=0
#while i<len(a):
 #  i +=1
  # pass
#print('Value of i:', i)
#python program to demonstrate
#while-else loop
#i=0
#while i<4:
 #  i +=1
  # print(i)
#else: 
 #  print("No Break\n")
#i=0
#while i<4:
  # i +=1
  # print(i)
  # break
#else: 
 #  print("No break")
#a=int(input("Enter a number (-1 to quit):"))
#while a!=-1:
 #  a=int(input("Enter a number (-1 to quit):"))
#initialize a counter
#count=0
#loop infinitely
#while True:
 #  count +=1
  # print(f"count is {count}")
   #if count ==10:
    #  break
   
#num=0
#for i in range(10):
 #  num +=1
  # if i==5:
   #   break
   #print("The num value is:", num)
#print("Out of the loop")
#num1=0
#while True:
 # num1 +=1
  #print(num1)
  #if num1==10:
   #  break
#print("End of loop")
#for i in range(10):
 # num1 =+1
 # if i<=10:
  # print("The number is:", i)
 #  pass 
#c=0
#for i in range(100):
 #  c +=1
#print("The number is:", i)
#for var in "Bengohub":
 #  if var =="e":
 #     continue
  # print(var)
#loop from 1 to 10
#for i in range(0,100):
 #  if i==6:
  #    continue
 #  else:
  #    print(i+1, end=" ")
#n = 26
#if n >=26:
    # write code your here
  #print("hubs")
#def funtion:
 # pass
#class hubClass:
 #   pass
#n=10
#for i in range(n):
 #   pass
#a=10
#b=20
#if (a<b):
 #   pass
#else:
 #   print("b>a")
#li = ['a', 'b', 'a', 'd']
#for i in li:
 #   if (i=='a'):
  #      pass
   # else: 
    #    print(i)
#def my_function():
 #   pass
#class Myclass:
 #   def _init_(self):
  #  pass
# python code to demonstrate working of enumerate()
#for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    #print(key, value)
#for key, value in enumerate(['Geeks', 'for', 'Geeks', 'is', 'the', 'best', 'coding', 'platform']):
 # print(value, end=' ')

# python code to demonstrate working of zip()
# initializing list
#questions = ['name', 'colour', 'shape']
#answers = ['apple', 'red', 'a circle']
# using zip() to combine two containers
# and print values
#for question, answer in zip(questions, answers):
  #  print('What is your {0}?  I am {1}.'.format(question, answer))

# python code to demonstrate working of items()
#d = {"geeks": "for", "only": "geeks"}
# iteritems() is renamed to items() in python3
# using items to print the dictionary key-value pair
#print("The key value pair using items is : ")
#for i, j in d.items():
  #  print(i, j)

#d = {"students": "board", "windows": "table",}
#print("The key-value pair is: ")
#for i, j in d.items():
 #   print(i, j)
# python code to demonstrate working of items()
#king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
 #       'Modi': 'The Changer'}
# using items to print the dictionary key-value pair
#for key, value in king.items():
 #   print(key, value)

# python code to demonstrate working of sorted()
# initializing list
#lis = [1, 3, 5, 6, 2, 1, 3]
# using sorted() to print the list in sorted order
#print("The list in sorted order is : ")
#for i in sorted(lis):
  #  print(i, end=" ")
#print("\r")
# using sorted() and set() to print the list in sorted order
# use of set() removes duplicates.
#print("The list in sorted order (without duplicates) is : ")
#for i in sorted(set(lis)):
 #   print(i, end=" ")
# python code to demonstrate working of sorted()
# initializing list
#basket = ['guave', 'orange', 'apple', 'pear',
 #         'guava', 'banana', 'grape']
# using sorted() and set() to print the list
#  in sorted order
#for fruit in sorted(set(basket)):
 #   print(fruit)
# python code to demonstrate working of reversed()
# initializing list
#lis = [1, 3, 5, 6, 2, 1, 3]
# using reversed() to print the list in reversed order
#print("The list in reversed order is : ")
#for i in reversed(lis):
 #   print(i, end=" \t")
  #  pass

#for i in reversed(range(2, 3, 4)):
 #   print(f'\n\n{i}')

# Example variable
count = 0
# Loop while count is less than 5
while count < 5:
    if count == 3:
        print("Count is 3")
    count += 1
    
