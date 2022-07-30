import os
##############
print("this tool created by yazan najeb jaber")
name = input("enter your name")
print("hello " + name)
print("in this tool you can see where are you")
print("your pash is " + os.getcwd())
print("In this path are these files: ")
print(os.listdir())

