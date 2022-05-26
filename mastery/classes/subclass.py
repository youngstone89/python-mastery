# Python program showing
# implementation of abstract
# class through subclassing

import abc

class parent:	
	def geeks(self):
		pass

class child(parent):
	def geeks(self):
		print("child class")

# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))


# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod

class R(ABC):
	def rk(self):
		print("Abstract Base Class")

class K(R):
	def rk(self):
		super().rk()
		print("subclass ")

# Driver code
r = K()
r.rk()


# Python program showing
# abstract properties

import abc
from abc import ABC, abstractmethod

class parent(ABC):
	@abc.abstractproperty
	def geeks(self):
		return "parent class"
class child(parent):
	
	@property
	def geeks(self):
		return "child class"


try:
	r =parent()
	print( r.geeks)
except Exception as err:
	print (err)

r = child()
print (r.geeks)
