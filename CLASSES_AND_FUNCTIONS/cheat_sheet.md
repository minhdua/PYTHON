# Empty function in python
- pass statement : is a special statement in Python that does nothing. can use in empty while, if else

# Use yield instead of return
- yield return_value
- 
# Modules
- import namefile (not contain .py)
# The from import Statement
-  import specific attributes from a module
# The dir() function
- The dir() built-in function returns a sorted list of strings containing the names defined by a module. The list contains the names of all the modules, variables and functions that are defined in a module.
# Object Oriented Programming
- The self : When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.
# The __int__ method
- The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
# Class and Instance Variables (Or attributes)
-  instance variables are variables whose value is assigned inside a constructor or method with self
# Data hiding
- we use double underscore
- We can access the value of hidden attribute by a tricky syntax myObject._MyClass__hiddenVariable
# Printing Objects
- In python this can be achieved by using __repr__ or __str__ methods print[t]), print(t)
- If no __str__ method is defined, print t (or print str(t)) uses __repr__. 
- If no __repr__ method is defined then the default is used
#  check if a class is subclass of another
- issubclass(Derived, Base)
- isinstance(b, Derived)
# Multiple Inheritance
- Python supports multiple inheritance. We specify all parent classes as comma separated list in bracket.
# access parent members in a subclass
- Using Parent class name
- Using super()
- Class or Static Variables in Python
# Python lambda (Anonymous Functions) | filter, map, reduce 
- lambda arguments: expression
- Use of lambda() with filter()
- Use of lambda() with map()
- Use of lambda() with reduce()



