
# unpacking
```python
years = (2022,2021,2020,2019)
lastest, *rest = years
'''
lastest = 2022
*rest = 2021.2020,2019
'''
```

# Difference of List, Tuple, Set
| | Mutable| Ordered | Indexing | Duplicates|
|-----|-----|-----|-----|-----|
|List | Y | Y | Y | Y |
|Tuple | F | Y | Y | Y |
|Set | Y | F | F | F|

# set
Sets are unordered and don't support indexing or slicing. If you run these code, you will get an error:
```python
guests = {"Mery","Anna","Jonathan"}
print(guests)
print(guests[0])  #error
```

The `clear()` function doesn't accept an argument and removes all the items from a set.
```python
student = {"Addy","Nex","Jone"}
student.clear()
```

The `union()` function is called on a set and accepts another set as an argument. Then return a now set with all elemets from both sets, omitting duplicates.
```python
set1 = {1,2,3,4}
set2 = {2,4,5}
set1.union(set2)  # {1,2,3,4,5}
```

The `difference()` function returns a set containing elements that are only in the first set and not in the second.
```python
set1 = {1,2,3,4}
set2 = {2,4,5}
unique = set1.differenrce(set2)  # {1,3}
```

Sets are mutable, meaning you can add or remove items from them.
```python
guests = {"Mery","Anna","Jonathan"}
guests.add("Robert")
guests.remove("Anna")
print(guests)  # {"Mery","Jonathan","Robert"}
```

# Dictionary
Dictinaries are collection types used to store data in `key:value` pairs, which are considered are items. They are ideal for organizing data into pairs, where each piece of data(value) has its unique identifier(key).


The `update()` function can accept dictionaries with multiple items. If an item is new, it will be added to the original dictionary.
```python
user = {"Age":20, "Surname": "Json"}
user.update({"Age":32, "surname":"Helen"})
```

The `pop()` function removes the item with the specified key name. It accepts the key of the item you want to remove as an argument.
```python
car = {
    "Brand" : "Ford",
    "Model" : “Mustang",
    "Color" : "red"
}

car.pop("Color")  # {"Brand" : "Ford","Model" : “Mustang"}
```

You can use the `in` operator to check if a key or a value occurs in a dictionary.
```python
car = {
    "Brand" : "Ford",
    "Model" : “Mustang",
    "Color" : "red"
}
print("Color" in car) # Ture
```
To check if a value occurs in a dictionary, you need to use the `values()` function.
```python
"red" in car.values()
```

You can interate through a dictionary using a `for` loop. If you loop through a dictionary, it will return the `keys`
```python
for in in car:
    print(i)  # Brand,Model,Color
```

While **strings** are the most commonly used data type for keys, other immutable types can also serve as keys. Values can be of any data type. So, you can't use a list to be as a key in a dictionary.

The `update()` function can accept dictionaries with multiple items.If an item is new, it will be added to the original dictionary.
```python
car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}
car.update({"Color": "blue", "Year": 2018})

# Output: {"Brand": "Ford","Model": "Mustang","Color": "blue","Year" : 2018}
```



# List
Here is the generic syntax and structure of a list comprehension:
`<variable> = [<expression> for <item> in <iterable>]`
1. <variable>: the variable that will store the newly created list
2. <expresion>:  an expression performed on each item. If no specific action is needed, the item itself is used.
3. <item>: the current item being processed
4. <iterable>: any interable object, such as ranges, lists, strings, tuples and sets.

List comprehensions are useful shorthands for such operations. They offer a shorter and more readable way to create lists with various setting using just a single line of code. List comprehensions are created using square brackets[].
```python
nums = [x for x in range(1,51)]
```

You can apple any expression to each item in the list being created with a list comprehension.
```python
nums = [x**2 for x in range(10)]
```

You can incorporate a condition into a list comprehension, placed after the interable.
```python
group = [x for x in user if x[0] == "B"]
```


# lambda

Lambda expression perform a single operation and return a result. They are defined using the lambda keyword, followed by its arguments, a colon and the expression to perform. 

`lambda <argument> : <expression>`


Lambda expressions can take multiple arguments separated by commas.

`lambda <argument 1>, <argument 2> : expression`

```python
lambda width, height : width*height
```

```python
x = lambda price, count : price*count
print(x(10,2))

### output
20
```

You can provide arguments to lambda expressions on-the-fly by adding them in parentheses immediately after the lambda function. The lambda expression should be also enclosed in parentheses.

```python
res = (lambda x,y : x+y)  (2,3)
print(res)

## output
5
```


# map

The `map()` function applies a specified function to every element in an iterable, like lists or tuples. It produces a result that can be transformed into a list using the `list()` function for easy viewing or further use.


```python
# List of names in various cases
names = ["alice", "bob", "CHARLTE", "dEborah"]

# Function to capitalize each name
def capitalize(name):
    return name.capitalize()

# Using map() to apply the capitalization to each name
capitalized = map(capitalize, names)

# Converting map object to a list
capitalized = list(capitalized)

print(capitalized)


## output
["Alice", "Bob", "Chralte", "Deborah"]
```

The `map()` function takes two arguments, an iterable and a function. Its requires the first argument to be a function and the second argument to be an iterable.

If you have a Lambda function, it can also put into a `map()` function.

```python
numbers = [1,2,3]
doubled = list(map(lambda x : x*2), number)
print(doubled)

# output
[2,4,6]
```

# filter

The `filter` function, just like the `map()` function, takes in a function and an iterable as arguments. The key purpose of `filter()` is to **apply a condition specified in the provide function to each item in the iterable and return only those for which the function evaluates to True**.

```python
products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]

# Filters products with name length equal to 4
filter_prof = list(filter(lambda name : len(name)==4, product))

print(filter_prof)

# output
["Sofa", "Vase"]
```


# args and kwargs

When you calling a function, you need to use the same number of arguments that have been defined, in the same order.

If the number of arguments of your function is unknown and unpredictable, you can always use an iterable as an argument.

```python
def total(numbers):
    result = 0
    for i in numbers:
        result += i
    return result

nums = [1,2,3,4,5]
print(total(nums))

## output
15
```

`*args` allows you to provide any number of arguments without the need to create a list before calling the function each time. It receives arguments as a tuple, which can be used inside the function. You need to use the unpacking operator `*` before args. This operator informs Python that the argument is an iterable and should be unpacked to receive its values as individual arguments.

```python
def total(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(total(1,2,3,4,5))
print(total(1,2,3))

## output
15
6
```

Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer.

```python
def display(*words):
    for item in words:
        print(item)

display("paper", "pen", "pencil")

## output
paper
pen
pencil
```

**When defining a function with both regular arguments and *args, the regular arguments must come before *args in the function definition**.

```python
def show_items(category, *args):
    print("Category: " + category)
    for item in items:
        print(item)

show_items("Electronics", "Laptop", "Smartphone", "Tablet")

## output
Category: Electronics
Laptop
Smartphone
Tablet
```

Python also allows you to pass keyword arguments using `**kwargs`. In this case, `**kwargs` receives arguments in the form of a dictionary, consisting of `key:value` pairs.

```python
# **kwargs is a dictionary

def display_info(**kwarges):
    #kwargs.items() returns the key:value pairs
    for key, value in kwarges.items():
        print(key, ":", value)

display_info(name="Alice", age=30, city="New York")

#output
name:Alice
age:30
city:New York
```

In a function definition, the order of arguments is important. First, regular arguments are listed, following by `*args` for positional arguments, and finally `**kwargs` for keyword arguments.

`def <func> (<argument>, <*args>, <**kwargs>)`


# Function
A function in Python can accept another function as an argument, it calls higher-order function.

```python
def song_name(name):
    return "Song name:" + name

def info(name, func):
    print(func(name))

info("Hallelujah", song_name)

# output
Song name: Hallelujah
```

In Python, functions can ne nested. This means you can define a function inside another functions's body.
```python
# outer function
def outer_function():
    print("Hello from the outer function")

    # inner function
    def inner_function():
        print("Hello from inner function")
    
    inner_function()

outer_function()

# output
Hello from the outer function
Hello from the inner function

```

You can also return the result of the nested function directly from within the body of the parent function.
```python
def greet(name):
    print("Hey", name)

    def account():
        return "Your account is created"

    message = account()
    return message

print(greet("Bob"))

## output
Hey, Bob
Your account is created
```


# Decorators

Imagine you have a function that generates a message. Your goal is to create another function that takes this original function as an argument and converts the original message into uppercase, without altering the original function's code.

These functions are known as `decorators`. In the code below, the `uppercase()` function acts as a decorator, and the `wrapper()` function represents the modified (or decorated) version of the `greet()` function.

```python
def greet():
    return "Welcome"

# take a function as an argument
def uppercase(func):
    # wrapper function to keep the original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

greet_upper = uppercase(greet)
print(greet_upper())


## output
WELCOME

```

Decorators modify a function's behavior without altering its original code. A decorator function include:
1. A function that modifies the original function
2. A function as an argument
3. A function of the decorator


You can apply a decorator to a function using the @ sign. It improves the code readability and provides a clean separation between the function and its decoration.

When a function with a decorator is called, it automatically includes the behavior defined in the decorator.

```python
def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome"

# Using the decorated function
print(greet_upper())


## output
WELCOME
```

Decorators are a powerful feature, offering a concise, readable, and efficient way to enhance the functionality of existing functions.

You can apply the same decorator to several different functions:

```python
def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(result, ": stock status for", item)
        return result
    return wrapper

@stock_status_decorator
def restock_item(item):
    return "Restocked"

@stock_status_decorator
def sell_item(item):
    return "Sold"

print(restock_item("Laptop"))
print(sell_item("Smartphone"))


## output
Restocked: stock status for Laptop
Sold: stock status for Smartphone
```


# OOP

In programming, there is a paradigm that follows the same principle as blueprint and instances. It's called object-oriented programming(OOP), blueprints are referred to as classes, and the instances are known as objects.

In Python, you can define a class by using the class keyword followed by the class name and a colon. Like this:
```python
class Dog:
```

In the real world, everything has distinguishing characteristics: a dog has its breed, color, and name; a car had its brand, model, and color. In programming, classes and objects mirror this concept with attributes. Attributes are the properties that define an object's individuality within a class.

To add attributes to a class, you must define the `__init__` method. This method's first parameter in always `self`, which represents the instance if the class. Following self, you specify the attributes you wish to include. Then, inside the function, you assign values to the initialized object's attributes, setting their initial state.

After an object is created, you can access its attributes by using the dot. notation.

In addition to attributes, you can add custom behaviors to a class by defining functions within it. These functions, known as methods, should include the `self` parameter to interact with the class instance. You can call these methods using the dot . notation, similar to how you access attributes.

```python
class Car:
    # Initialize attributes
    def __init__(self, brand, color):
        # Assign values to attributes
        self.brand = brand
        self.color = color

    def honk(self):
        print('Beep beep')

# Create am object of the car class
my_car = Car('Audi', 'yellow')

print(my_car.brand)
print(my_car.color)
may_car.honk()

## output
Audi
yellow
Beep beep
```


The main difference between functions and methods is that functions are independent and can be called on their own, while methods are associated with a class and can be called only with its instance. This means that you can't call a method without having the instance of a class where that method is defined. Like this:

`print()` : this is a function
`my_car.honk()`: this is a method

There are many built-in method in Python, some of which you already are familiar with. For example, the `lower()`, `upper()` and `capitalize()` methods are commonly used in string objects.


# Inheritance

Inheritance is a key concept for situations where you have an existing class with defined attributes and behaviors. And you need a new class that not only shares these characteristics but also has its own unique ones. 

Inheritance allows the new class to 'inherit' properties from the existing class while adding or modifying specific features as needed.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print('Moving')


# Inheritance from Animal class
class Dog(Animal):
    #Specific behavior
    def bark(self):
        print('Woof!')

# Creating an instance
my_dog = Dog('Bob')

# Inherited attribute and behavior
print(my_dog.name)
my_dog.move()

# Specific behavior
my_dog.bark()
```

A class from which others are inherited is known as a superclass or parent class. Conversely, a class that inherits from another class is referred to as a subclass or child class.

The Dog class inherits from the Animal class. Identify the elements. Like this: **child class: Dog,   parent class: Animal**

What if we want to not only inherit attributes but also ass specific ones to a child class? In this case, we define an `__init__` method in the child class. Use `super().__init__()` to inherit attributes from the parent class, and then define any additional attributes as usual.

```python
# parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print('Moving')

# Child class
class Dog(Animal):
    def __init__(self, name, breed, age):
        # Initialize attributes of the superclass
        super().__init__(name)
        # Additional attributes specific to Dog
        self.breed = breed
        self.age = age

    def bark(self):
        print('Woof!')

my_dog = Dog('Jax', 'Bulldog', 5)
# inherited attribute
print(my_dog.name)

# Additional attributes
print(my_dog.breed)
print(my_dog.age)


## output
Jax
Bulldog
5
```

You can define methods with the same name in both parent and child classes, but they can perform different operations. This is known as **method overriding**. For instance, consider the Animal class with a sound method. The dog and cat child classes inherit the sound method from Animal but override it to suit their specific needs.

You can use the super()  function if you want to call a method from the parent class while overriding it.

This is useful when you want to add some functionality to the child class method without changing the original one.

Method overriding is a demonstration of another key concept in OOP - polymorphism. Polymorphism lets objects use methods in their own way, even if they share the same name.

In this example, even though each animal in the animals list may be of a different subclass, the code can call sound() on each without needing to know its specific type.

```python
# Parent class
class Animal:
    def __init__(slef, name):
        self.name = name

    def sound(self):
        print('Making s sound')

# Child class Dog
class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    # Overridden sound method for Dog
    def sound(self):
        print('Woof!')

# Child class Cat
class Cat(Animal):
    def __init__(self, breed, age):
        super().__init__(name)
        self.breed =breed
        self.age = age

    def sound(self):
        print('Meow!')


# Creating instances
my_dog = Dog('Jax', 'Bulldog', 5)
my_cat = Cat('Lily', 'Ragdoll', 2)


# Using overridden methods
my_dog.sound()
my_cat.sound()


## output
Woof!
Meow!
```

# Data hiding

Data hiding is a key idea in making code with objects(like in games or apps) safer and cleaner. It means keeping some parts of an object private so that only certain parts of your code can change them. This helps prevent mistakes and keeps your code easy to manage.

In Python, data hiding has two levels. The first involves prefixing an attribute with a **single underscore _**, signaling **it's meant for internal use and should be viewed as 'protected'**.

Attributes with a single underscore are accessible but considered protected by convention, signaling they're for internal use and should be accessed cautiously outside the class.

To access a protected attribute outside of the class, use the single underscore prefix, as that's part of the attribute's name.
```python
class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        # Making the odometer attribute 'protected'
        self._odometer = odometer

    def describe_car(self):
        print(self.year, self.model)

    def read_odometer(self):
        print('Odometer:', self._odometer, 'miles')

my_car = Car('Audi', 2020, 15000)

my_car.describe_car()
my_car.read_odometer()

# accessing the protected attribute
print(my_car._odometer)

```

**The next level of data hiding involves making an attribute private**. This is achieved by prefixing the attribute name with **two underscores(e.g., __attribute)**. In this case, unlike protected attributes, this is not just a convention - it limits its access outside the class through name mangling, enhancing data protection and encapsulation. This method is used for sensitive or internal data, strongly discouraging external access.

Accessing a private attribute with double underscores from outside the class cause an error, but it's accessible within class methods. This demonstrates encapsulation, protecting sensitive data from external access and ensuring it's only reachable via specific methods, aligning with object-oriented programming principles.

Accessing a private attribute directly from outside its class is generally discouraged in Python. However, Python employs name mangling for private attributes, which means you can access them using a specific naming convention from outside the class if necessary. 

```python
class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        # Making the odometer attribute 'private'
        self.__odometer = odometer

    def describe_car(self):
        print(self.year, self.model)

    def read_odometer(self):
        print('Odometer:', self.__odometer, 'miles')

my_car = Car('Audi', 2020, 15000)

# accessing the attribute within method
my_car.read_odometer()

# error
print(my_car.__odometer)

# accessing using name mangling
print(my_car._Car__odometer)

```

You can also designate methods as protected or private, following the same convention as with attributes. Protected methods are prefixed with a single underscore and can be accessed within the class and its subclasses. However, private methods, marked by a double underscore, cannot be directly accessed from outside the class.

```python
class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        # Making the odometer attribute 'private'
        self.__odometer = odometer

    def _describe_car(self):
        print(self.year, self.model)

    def __read_odometer(self):
        print('Odometer:', self.__odometer, 'miles')

my_car = Car('Audi', 2020, 15000)

# accessing protected method
my_car._describe_car()

# error when accessing a private method
my_car.__read_odometer
```