class myproperty:

    def __init__(self, 
                 fget=None, 
                 fset=None, 
                 fdel=None, 
                 doc=None):

        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):

        print("getter is called")
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        print("setter is called")
        #if self.fset is None:
         #   raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


#### class for testing purposes only !!!

class C:

    def __init__(self, x=None):
        self.x = x

    @myproperty
    def n(self):
        return self.__x 

    @n.setter
    def n(self, x):
        self.__x = x

c = C()
c.n = 3
print(c.n)
print(type(C.n))
