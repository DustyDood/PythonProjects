
"""
mySentence = 'loves the color'
color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name, mySentence, i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name?')
        if name == "":
            print('ERR. Try again.')
        elif name == "Sally":
            print("Sally, you may not use this software.")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()


def helloFunction():
    name = input("Hello, who's this?")
    print("Hello, {}!".format(name))


helloFunction()
"""

TWEWY = ['Neku', 'Shiki', 'Beat', 'Rhyme']

for i in TWEWY:
    print(i)

print(TWEWY.count("Neku"))
TWEWY.sort()
print(TWEWY)

def multLambda():
    x = input('Enter a number')
    y = input('Enter another number')
    z = lambda a, b: a * b
    print(z(int(x), int(y)))


multLambda()
