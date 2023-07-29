# # def myFun(arg1, *argv):
# #     print("First argument :", arg1)
# #     for arg in argv:
# #         print("Next argument through *argv :", arg)
# # myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')
# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)
# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)
# def myFun(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

# defining car class
class car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]
# # creating objects of car class
# audi = car(200, 'red')
# bmw = car(250, 'black')
# mb = car(190, 'white')
# # printing the color and speed of the cars
# print(audi.color)
# print(bmw.speed)
# defining car class
# class car():
#     # args receives unlimited no. of arguments as an array
#     def __init__(self, **kwargs):
#         # access args index like array does
#         self.speed = kwargs['s']
#         self.color = kwargs['c']
# # creating objects of car class
# audi = car(s=200, c='red')
# bmw = car(s=250, c='black')
# mb = car(s=190, c='white')
# # printing the color and speed of cars
# print(audi.color)
# print(bmw.speed)

# A Simple Python program to demonstrate working
# of yield
# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
# # Driver code to check above generator function
# for value in simpleGeneratorFun():
#     print(value)
# A Python program to generate squares from 1
# to 100 using yield and therefore generator
# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
        # from this point
# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)