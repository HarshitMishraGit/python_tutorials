# # functions
# a=[1,2,3]
# b=[2,3,4]
# c=sum(a+b) # built-in function
# print(c)

# user defined function
# def function1(a,b):
#     print('Hello you are in function 1',a+b)

# def average(a,b):
#     '''This is a function which will calculate the average of two numbers
#     This function doesn't work for three numbers'''
#     average=(a+b)/2
#     print(average)
#     return average

# print(average.__doc__)
# v=average(3,4)
# print(v)

# function1(5,7)

# num1=input('Enter num1: ')
# num2=input('Enter num2: ')
# try:
#     print('Sum of num1 and num2', int(num1)+int(num2))
# except Exception as e:
#     print(e)

# file io basics
# f = open('jobs.txt')
# print(f.readlines(),'w')
# f.close()

# open files for reading

'''
r --> for reading       default mode           
w --> for writing
x --> creates files if not exsists
a --> append
t --> text mode     default mode     
b --> binary
+ --> read and write
'''
# f=open('myfile.txt','w')
# content=f.write('anubhav you are great\n')
# print(content)
# print(type(content))
# for line in content:
#     print(line)

# f=open('myfile.txt','r+')
# print(f.read())
# f.write('thank you')
# print(f.read())
# f.close()

'''more on files'''
'''
f=open('myfile.txt')
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(2)
print(f.readlines())
f.close()
'''

with open('myfile.txt') as f:
    a=f.read()
    print(a)

f=open('myfile.txt')