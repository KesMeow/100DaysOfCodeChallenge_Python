def add(*args):
    sum = 0
    for arg in args:
        sum+= arg
    return sum


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)