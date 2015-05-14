__author__ = 'Yue'


class SuperClass(object):
    def __init__(self):
        print("I am SuperClass")
    def foo(self):
        print("I am foo in sup")



class SubClass(SuperClass):
    def __init__(self):
        print("I am SubClass")
    def foo(self):
        print("I am foo in sub")
        return "Yes"

c=SubClass();

# print(c.__class__)
# print(c.__bases__)
# print(c.foo())
# print(SuperClass.foo(c))
#
# help(range)
#
# handle = open("F://yaya.txt","r");
# handle.name
# handle.readline()

id(c)