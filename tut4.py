# variable scope
l=10 # this is global variable
def function1(n):
    # l=5
    def num():
        global l
        l=100
        print('1\n',l)
    global l
    print(l)
    print(n, 'I have printed')

function1('This is me')
print(l)