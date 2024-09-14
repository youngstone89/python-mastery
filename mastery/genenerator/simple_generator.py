
def call_back(val):
    return val

# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


def simpleGeneratorFun():
    yield call_back(1)
    yield call_back(2)
    yield call_back(3)


def simpleGenerator():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


for v in simpleGenerator():
    print(v)
