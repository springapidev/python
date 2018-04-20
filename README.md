# python
Get Started Python
Python Doc Url: https://docs.python.org/3/tutorial/index.html
Pyton Download Link for Windows: https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe

Python Basic for Beginners:
1. print("Hello Python.")

      output: Hello Python.

2.Indentation: 
Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python code to use four spaces. For example:
x = 1
if x == 1:
      # indented four spaces
      print("x is 1.")
      
      output: x is 1.
     
3. Variables and Types

Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

This tutorial will go over a few basic types of variables.
Numbers

Python supports two types of numbers - integers and floating point numbers. (It also supports complex numbers, which will not be explained in this tutorial).

To define an integer, use the following syntax:

myint = 7
print(myint)

            output: 7

To define a floating point number, you may use one of the following notations:

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

      Output: 
      7.0
      7.0

Strings: 
Strings are defined either with a single quote or a double quotes.

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

            Output: 

            hello
            hello

The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)

mystring = "Don't worry about apostrophes"

print(mystring)

            Output: 

            Don't worry about apostrophes


There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters. These are beyond the scope of this tutorial, but are covered in the Python documentation.

Simple operators can be executed on numbers and strings:

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

      Output: 

      3
      hello world
