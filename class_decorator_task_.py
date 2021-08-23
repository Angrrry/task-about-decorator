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
import warnings


def classdecorator(**kwargs):
    def wrapper(cls):
        for key, value in kwargs.items():
            if getattr(cls, key, None):
                warnings.warn(f"{key} already in {cls.__name__}")
            else:
                if isinstance(value, str):
                    setattr(cls, key, value)
                elif callable(value):
                    setattr(cls, key, staticmethod(value))
                else:
                    print(key, value)
                    print(type(value))
                    raise Exception("value is not a function nor string")
        return cls

    return wrapper


if __name__ == "__main__":
    @classdecorator(a="s", w=lambda: 2, s=lambda x: x + 2)
    class A:
        w = "sss"


    print(A.w)
    print(A.a)
    print(A.s(2))
    a = A()
    print(a.s(2))