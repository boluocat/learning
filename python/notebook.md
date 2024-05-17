
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

