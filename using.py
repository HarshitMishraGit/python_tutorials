# f-strings
'''f-string means string formatting'''
me='Anubhav'
a=5
import math
# a='this is %s %s'%(me, a)
# a='This is {1} {0}'
a=f'this is {me} {a} {math.cos(65)}' # this is f-string
# b=a.format(me, a)
print(a)