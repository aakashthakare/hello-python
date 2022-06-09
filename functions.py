def firstFunction(input='Default Input'):
    print(input)


def multiArgFunction(a, b, c):
    """ Doc String!"""
    print(a, b, c)


firstFunction("Hello!")
firstFunction()

multiArgFunction('a', 'b', 'c')
multiArgFunction(b='a', a='b', c='c')


help(firstFunction)

help(multiArgFunction)