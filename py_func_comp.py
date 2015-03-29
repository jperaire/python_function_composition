class Function(object):

    """ Used for pointless-style function composition """

    def __init__(self, func, funcList=None):
        if not callable(func):
            raise TypeError("{0} object is not callable".format(str(type(func))))
            
        if funcList is None:
            self.funcList = []
        else:
            self.funcList = funcList[:]
            
        if hasattr(func, "funcList"):
            self.funcList += func.funcList
        else:
            self.funcList.append(func)

    def __call__(self, *args, **kwargs):
        f_list = self.funcList[:]
        val = f_list.pop()(*args, **kwargs)
        while f_list:
            f = f_list.pop()
            try:
                val = f(val)
            except TypeError as e:
                raise TypeError("Inputs of function {0} did not \
                                match outputs of other: \
                                {1}".format(f.__name__, e.message))
        
        return val

    def __mul__(self, obj):
        if callable(obj):
            return Function(obj, funcList = self.funcList)
        else:
            raise TypeError("{0} object is not callable".format(str(type(obj))))

    def __rmul__(self, obj):
        return Function(obj) * self


def composable(myFunc):
    return Function(myFunc)
    
    
if __name__ == "__main__":
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



