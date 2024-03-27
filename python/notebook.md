
# unpack
```python
years = (2022,2021.2020,2019)
lastest, *rest = years
```

# set
Sets are unordered and don't support indexing or slicing. If you run these code, you will get an error:
```python
guest = {"Mery","Anna","Jonathan"}
print(guests)
print(guests[0])  #error
```

The `clear()` function doesn't accept an argument and removes all the items from a set.
```python
student = {"Addy","Nex","Jone"}
student.clear()
```

The `union()` function is called on a set and accepts another set as an argument.
```python
set1 = {1,2,3,4}
set2 = {2,4,5}
set1.union(set2)  # {1,2,3,4,5}
```


