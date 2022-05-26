num = 23
print("Type of num is:", type(num))

lst = [1, 2, 4]
print("Type of lst is:", type(lst))

name = "Atul"
print("Type of name is:", type(name))


class Student:
    	pass
stu_obj = Student()

# Print type of object of Student class
print("Type of stu_obj is:", type(stu_obj))

# Defined class without any
# class methods and variables
class test:pass

# Defining method variables
test.x = 45

# Defining class methods
test.foo = lambda self: print('Hello')

# creating object
myobj = test()

print(myobj.x)
myobj.foo()



def test_method(self):
    	print("This is Test class method!")

# creating a base class
class Base:
	def myfun(self):
		print("This is inherited method!")

# Creating Test class dynamically using
# type() method directly
Test = type('Test', (Base, ), dict(x="atul", my_method=test_method))

# Print type of Test
print("Type of Test class: ", type(Test))

# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))

# calling inherited method
test_obj.myfun()

# calling Test class method
test_obj.my_method()

# printing variable
print(test_obj.x)


# our metaclass
class MultiBases(type):
	# overriding __new__ method
	def __new__(cls, clsname, bases, clsdict):
		# if no of base classes is greater than 1
		# raise error
		if len(bases)>1:
			raise TypeError("Inherited multiple base classes!!!")
		
		# else execute __new__ method of super class, ie.
		# call __init__ of type class
		return super().__new__(cls, clsname, bases, clsdict)

# metaclass can be specified by 'metaclass' keyword argument
# now MultiBase class is used for creating classes
# this will be propagated to all subclasses of Base
class Base(metaclass=MultiBases):
	pass

# no error is raised
class A(Base):
	pass

# no error is raised
class B(Base):
	pass

# This will raise an error!
class C(A, B):
	pass
