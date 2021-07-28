"""
Write a dummy class decorator with kwargs. For each of key in kwargs get value(kwargs[key]).
If value is function:
    create respective staticmethod in the decorated class with key name.
If string value:
    create respective class attribute.
Else:
    raise Error
If class already has attribute with such name:
    do not replace original one but print a warning with module warnings
"""
def classdecorator(**kwargs):
    def wrapper(cls):
        for key, value in kwargs.items():
            if getattr(cls,key, None):
                ...
            else:
                setattr(cls,key,value)


    return wrapper
if __name__ == "__main__":
    @classdecorator(a=2, b=lambda x:x+2, c = 3)
    class A:
        c=1