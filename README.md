# python_function_composition

Pointless - style function composition

Sample usage:

@composable
def a(x):
    return 3 * x

@composable
def b(x):
    return 5 + x

@composable
def c(x, y):
    return x + y

f = a * b
g = f * f
h = g * c
s = g * f

print f(3)
print g(10)
print h(3, 4)
print s(1)
