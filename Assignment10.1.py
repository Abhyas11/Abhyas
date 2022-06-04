'''
Abhyas Maharjan
CIS 245
Bellevue University
4/8/2022
Purpose : To create a file in given directory
'''
import os

directory = input("Enter the directory you would like to use: ")
filename = input("Enter the filename: ")
name = input("Enter your name: ")
address = input("Enter your address: ")
phnumber = input("Enter your phone number: ")
file = os.path.join(directory, filename + ".txt")
f = open(file, "w")
f.write(name + ', ' + address + ', ' + "phnumber")
f.close()
readf = open(file, "r")
print(readf.read())
