def hello(name='Grace'):
    print("Hello {}".format(name))


def returnEx(name):
    return 'Welcome {}'.format(name)


hello('Mary')

greeting = returnEx('Peter')

print(greeting)
