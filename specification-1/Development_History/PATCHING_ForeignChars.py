'''
num = int(input("Input Numerator: "))
dom = int(input("Input Denominator: "))
try:
    result = num/dom
except ZeroDivisionError:
    print("BLASPHEMY!")
try:
    print(num,"/",dom,"=",result)
except NameError:
    print("...")

num = int(input("Input Numerator: "))
dom = int(input("Input Denominator: "))
try:
    result = num/dom
    print(num, "/", dom, "=", result)
except ZeroDivisionError:
    print("BLASPHEMY!") '''
'''The "try-except" method stops at the first error it finds. Replacing "ZeroDivisionError" with "NameError" causes the
error ZeroDivisionError to be returned instead.'''
import sys

f = open("textfile1","r",encoding="utf8")   # Opens the specified textfile and reads from it
theString = f.read()    # Assigns everything from the textfile to a str-variable #6583
print(theString)

#print(theString)