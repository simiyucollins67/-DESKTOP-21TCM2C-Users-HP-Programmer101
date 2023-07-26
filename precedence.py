#name='Collins'
#Age=0
#if name=='Alex' or name=='John' and age>=2:
 #   print('Hello! Welcome.')
#else:
  #  print('Goodbye')
#expr=10+20*30
#print(expr)
#print(100/10*10)
#print(5-2+3)
#print(2**3**2)
#print(2**9)
#name = input("Enter your name: ")
#print (f"Hello, {name}")
#name = input ("Enter your other name: ")
#print ("Hello, " ," ",end="***")
#print(name)
#print("Hello, world!")""
#print ("apple", "banana", "Cherry", sep=", ")
#input().split(separator, maxsplit)
#x, y=input("Enter two values:").split(",")
#print("Number of boys:", x)
#print("Number of girls:", y)
#print("First number is {} and second number is {}".format(x,y))
"""Taking multiple inputs at atime and type casting using list()function"""
#x=list(map(int, input("Enter multiple values:").split()))
#print("List of students:", x)
#List comprehension
"Program showing how to take multiple input using List comprehension taking two at a time"
x, y, z = [int(x) for x in input ("Enter three values: \n").split()]
print("The first number is: ",x)
print("\nThe second number is: ",y)
print("\nThe third number is: ",z, end="")
#Taking two inputs at time
m, n=[int(m) for m in input("Enter two values:").split()]
print("The first number is {} and the second number is {}".format(m,n))
#Taking multiple inputs at a time
x=[int(x) for x in input("Enter multiple values of x:").split()]
print("The values of x are: ", x)