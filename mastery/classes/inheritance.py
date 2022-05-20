class ParentClass:
    def __init__(self,name):
        self.name = name

    def play():
        print("play pocker")


class ChildClass(ParentClass):
    def play():
        print("play puzzle")





c = ChildClass("youngstone")
c.play

if isinstance(c,ChildClass):
    print("instance")

if issubclass(c.__class__,ParentClass):
    print("subclass")