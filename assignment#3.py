# Q.2 Write a Python program to get the Python version you are using.

# import sys
# print("Python version")
# print (sys.version)



# Q.3 Write a Python program to display the current date and time.

# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%d-%m-%y %H:%M:%S"))



# Q.4 Write a Python program which accepts the radius of a circle from the user and compute the area.

# radius = input(("Enter Radius in cm: "))
# area = (float(3.14))*(float(radius)**2)
# print("Area of circle is:", area,"cm")



# Q.5 Write a Python program which accepts the user's first and last name and print them in
#     reverse order with a space between them.

# first_name = input("First Name: ")
# last_name = input("Last Name: ")
# print(last_name , first_name)



# Q.6 Write a python program which takes two inputs from user and print them addition

# input_first = input("First entry: ")
# input_second = input("Secont input: ")
# add = input_first + input_second
# print(add) 



# Q.7 Write a program which takes 5 inputs from user for different subject’s marks, total it
#     and generate mark sheet using grades ?



# english = int(input("Enter english marks: "))
# maths = int(input("Enter maths marks: "))
# physics = int(input("Enter physics marks: "))
# islamiat = int(input("Enter islamiat marks: "))
# computer = int(input("Enter computer marks: "))

# total_marks = 500

# obtained_marks = english + islamiat + maths + computer + physics

# percentage = (int(obtained_marks)/int(total_marks))*int(100)
# print("Percentage:",percentage)

# if (percentage <= 100 and percentage >= 80):
#     print("Your Grade is: A+")

# elif (percentage < 80 and  percentage >= 70):
#     print("Your Grade is: A")

# elif (percentage < 70 and  percentage >= 60):
#     print("Your Grade is: B")

# elif(percentage < 60 and percentage >= 50):
#     print("Your Grade is: C")

# elif(percentage < 50 and percentage >= 40):
#     print("Your Grade is: D")

# elif(percentage < 40 and percentage >= 33):
#     print("Your Grade is: E")

# else:
#     print("Fail")



# Q.8 Write a program which take input from user and identify that the given number is even or odd?

# num = int(input("Enter number: "))
# x = (num % 2)
# if (x > 0):
#     print("Number is odd")
# else:
#     print("Number is even")



# Q.9 Write a program which print the length of the list?

# list = ["A", "B", 1, 2]
# print("Number of items in list:", len(list))



# Q.11 Write a Python program to get the largest number from a numeric list.

# list = [1, 4, 3, 2]
# print("Largest number: ",max(list))



# Q.12 Write a program that prints out all the elements of the list that are less than 5.

# a = [1, 2, 3, 4, 5, 6, 2, 3, 10, 60, 9]
# for j in a:
#     if j < 5:
#         print(j)