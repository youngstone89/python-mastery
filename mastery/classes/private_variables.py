class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)




m = Mapping(["a","b","c"])
# m.__update(["asdfasdf"]) # private variable is not accessible

print(m.items_list)

m.update(["c","d"])

print(m.items_list)

keys=["a","b","c"]
values=[1,2,3]
ms = MappingSubclass(["x","y","z"])
ms.update(keys,values)
print(ms.items_list)