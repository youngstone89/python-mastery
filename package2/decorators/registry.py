registry = []

def register(func):
    registry.append(func)
    return func

@register
def f1():
    print('You often feel tired,')

@register
def f2():
    print('not because you\'ve done too much')

@register
def f3():
    print('but because you\'ve done to little of what sparks a light in you.')

def main():
    for f in registry:
        f()

if __name__ == '__main__':
    main()