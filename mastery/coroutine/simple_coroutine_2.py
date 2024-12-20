from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> started: a=', a)
    b = yield a
    print('-> received b=', b)
    c = yield a+b
    print('-> recieved c=', c)


my_coro2 = simple_coro2(2)

print(getgeneratorstate(my_coro2))

next(my_coro2)

print(getgeneratorstate(my_coro2))

my_coro2.send(28)

my_coro2.send(99)
print(getgeneratorstate(my_coro2))
