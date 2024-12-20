def simple_coroutine():
    print('-> coroutine started')
    x = yield  # recevie from send()
    print('-> coroutine received', x)


my_simple_coro = simple_coroutine()
print(my_simple_coro)
# start coroutine
next(my_simple_coro)

# send a value to yield
my_simple_coro.send(42)
