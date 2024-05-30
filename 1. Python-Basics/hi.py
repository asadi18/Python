#print ('Hi I am running');

###This is comment line, so I am writing variables bellow

"""
This is a Multiline 
Comment. green line for one line comment and this color for 
multiline....... 
"""

###Simple add operation

# a = 5
# b = 8 
# print(a+b)

# c = 9.6
# d = 4.5
# print(c+d)

### String Checking
#stre = "I am Asad Ishteaque checking few string things"
#print(stre)

#Replace old value in here 

#print (stre.replace("WE", "I"))
# print(stre.find("s"))
#print(stre.count("s"))

###Type Casting

# firstNum = 7
# secondNum = input ("Enter a number: ")

# print("sum: ", firstNum + int(secondNum)) ## We have to take int for ty,ll be a string because paythong takes input as string 


###Operators --- 3 types of Operators 1.Arithmetic(+,-,*,/)  2. Comparator: <,>,<=,>=  3. logical: and, or, not

# val1 = input("Enter the first value: ")
# val2 = input ("Enter the second value: ")

# print( "The Result is : "  ,int(val1)*int(val2))  # we can do all operaions here


# Condition Statement Check

# a = 9
# b = 5

# if a>b:
#     print("a is BIG")
    
# else: 
#     print("b is BIG")




#Loop 

# for i in range(1,10,2): #(Iteration Start, Iteration End, If Need to skip)
#     print(i)

# sum = 0
# for i in range(101):
#     sum = i+sum
#     print(sum)

# sum = 0
# for i in range(1,101):
#     if i%2==0: #if we wants to print even number then make it not equal and remove continue with sum operation
#         continue
#     else:
#         sum = sum + i
#         print(sum)

#while LOOP

# i = 1
# sum = 0
# while i<101:
#     sum = sum+i
#     i = i+2
# print(sum)

#List LOOP

# fruits = ['mango', 'banana', 'jackfruit', 'watermelon']

# for x in fruits:
#     print(x)




#function or method

# def add(a,b):  # use sub tract, multiply etc
#     return a + b 

# c = int(input("Enter the value: "))
# d = int(input("Enter the value: "))

# print ("The Result is : ", add(c,d))


###String Practice 
#WAP to input users first name and print its length 

# user = input("Enter your Name: ")
# print(len(user))

#WAP to find the occuraence of '$' in a String
# strr = "hey , testing out the occurances of $$$"
# print(strr.count("$"))


### If Else Problem 

#WAP to check if a number entered by the user is odd or even. 

#user = int(input("Enter the number: "))

# if(user %2 == 0 ):
#     print("This is Even Number")
# else: 
#     print("This is Odd Number")
    

#WAP to find the greatest of 3 numbers entered by the user. 
# num1 = input("Enter First Number:" )
# num2 = input("Enter Second Number:" )
# num3 = input("Enter 3rd Number:" )

# if(num1>=num2 and num1>=num3):
#     print("Num1 is the Big")
    
# elif(num2>=num3 and num2>=num1):
#     print("Num2 is the Big")
    
# else: 
#     print("Num3 is Big")

#WAP to check if a number is a multiple of 7 or not.
# user = 21
# if(user %7 == 0 ):
#     print("This is Right Number")
# else: 
#     print("This is Wrong Number")


### Practice of Turtle
# import turtle
# turtle.shape("turtle")
# turtle.speed(1)

# for side_length in range(50, 100, 10):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)
        
# turtle.exitonclick()




###while loop and turtle color

#program for printing a multiplication table

# n = int(input("Enter a positive integer : "))
# m = 1

# while m<=10:
#     print(n,"x",m, "=", n*m)
#     m = m+1 #also write as m+=1
    
#Nested loop and turtle

# import turtle
# turtle.color("orange")
# turtle.speed(5)
# counter = 0
# while counter< 40:
#     for i in range(4):
#         turtle.forward(178)
#         turtle.right(190)
        
#     turtle.right(100)
#     counter = counter + 1
    
# turtle.exitonclick()

#WAP to print square usingbreak

 
# while True: 
#     n = int(input("Please Enter a Number (0 to exit) : "))
#     if n == 0: 
#         break
#     else:
        
#         print("Square of ", n , "is : ", n*n)


#Break and Continue Full details

# terminate = False
# while not terminate: 
#     num1 = int(input("Please Enter the First Number: "))
#     num2 = int(input("Please Enter the Second Number: "))
#     while True: 
#         operation = input("Please enter add / sub or quit to exit : ")
#         if operation == "quit": 
#             terminate = True
#             break
#         if operation not in ["add", "sub"]:
#             print("Unknown Operation!")
#             continue
#         if operation == "add":
#             print("Result is : ", num1+ num2)
#             break
#         if operation == "sub": 
#             print("Result is : ", num1 - num2)
#             break

#WAP for 3 favourte school name and add them into a list

# schools = []
# school1 = "Firozsha School"
# schools.append(school1)
# school2 = "Ispahani School"
# schools.append(school2)
# school3 = "Victoria School"
# schools.append(school3)

# print(schools)

# Can rewrite it as 
# schools = []
# schools.append(input("Enter the First String: "))
# schools.append(input("Enter the Second String: "))
# schools.append(input("Enter the Third String: "))

# print(schools)

#WAP to check if a list contains a palindrome of elements. (Hint: use copy() mthod)

# list1 = [1,2,1]
# list2 = [1,2,3]
# str1 = ['m', 'a','d','a','m']

# reverse_list = str1.copy()
# reverse_list.reverse()
# if str1 == reverse_list: # use both str1 , list1 and 2 to check one by one 
#     print("It is a palindrome ")
    
# else: 
#     print("Not a palindrome")

#WAP to check number of occurance in a tuple

# grade = ("C", "B", "A", "C", "A", "A", "B", "A", "D")
# print(grade.count("A"))

#WAP to store values in a list and sort them from A to D for ("C", "B", "A", "C", "A", "A", "B", "A", "D")

# grade = ["C", "B", "A", "C", "A", "A", "B", "A", "D"]
# grade.sort()
# print(grade)


#WAP to enter marks of 3 subjects from the user and store them in a dictonary. start with an empty dictionary & add one by one. use subject name as key & marks as value. 

# marks = {}

# x = int(input("enter phy : "))
# marks.update({"Phy" : x})

# y = int(input("Enter Che : "))
# marks.update({"Che" : y})

# z = int(input("Enter Bio : "))
# marks.update({"Bio " : z})

# print(marks)
# print(type(marks))

#Figure out a way to store 9 and 9.0 as separate values in the set. 
# values = {9, 98, 99, '9.0'}
# print(values)

#While loop Problem

# i = 1
# while i<101: 
#     print(i)
#     i+=1

# i = 100
# while i>0: 
#     print(i)
#     i-=1

#Multiplication Table of a number n 

# n = int(input("Enter the Number you want the multiplication Table:"))
# m = 1
# while m<=10:
#     print(n, "x" , m , " = ", m*n)
#     m+=1
  

#List Print

# lists = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(lists):
#     print(lists[i])
#     i+=1
    
#Search For a Number
# lists = [1,4,9,16,25,36,49,64,81,100]

#x = int(input("Enter the number to search: "))
#i = 0
#while i <len(lists):
    #if (lists[i]==x):
     #   print("The index is : ", i)
  #  i+=1
  
#For loop use case

# lists = [1,4,9,16,25,36,49,64,81,100]

# for nums in lists: 
#     print(nums)
    
    
#Find a number using for loop 
lists = [1,4,9,16,25,36,49,64,81,100]
num = int(input("Enter the Number to search: "))
i = 0
for x in lists: 
    if(x == num):
        print("The Number is found at index:", i)
        break
    i+=1
    print("Finding...........")