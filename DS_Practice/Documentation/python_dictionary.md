### Python Dictionary

Python dictionary is used to store key value pairs.

you can define dictionary in curly bracket or by calling dict object and can assign key values to it

```python
>>>items = dict() # or you can define like items = {}
items = {
    'name': 'milk powder',
    'qty':1,
    'price': 200.0,
    'description': 'some descriptions',
    'related_items': [
        #... add all related items
    ]
}
```
Dictionaries doesnt allow duplicate keys which means if you add duplicate key then the last duplicate value will be present in the dictionary
```python
items = {
    'name': 'milk powder',
    'qty':1,
    'price': 200.0,
    'price': 400.0,
    'description': 'some descriptions',
    'related_items': [
        #... add all related items
    ]
}
```
so the output of above dictionary will be
```python
>>> items
{'name': 'milk powder', 
 'qty': 1, 
 'price': 400.0, 
 'description': 'some descriptions', 
 'related_items': []
 }
```

As you can see the duplicate key price value is updated with the last duplicate value.

Access Dictionary items:
you can access dictionary items with the square bracket and key name. For example, if you want to access name of out items then you can do it by following
```python
>>> items['name']
'milk powder'
```

Dictinary are Changeable:
Dictionary are changeble which means you can change value dictionary. For example, Suppose you want to change the name of items to some other name then you can do it by following
```python
>>> items['name'] = 'Sugar pack of 1 KG'
>>> items
{'name': 'Sugar pack of 1 KG', 'qty': 1, 'price': 400.0, 'description': 'some descriptions', 'related_items': []}
```

Calculate length of dictionary:
you can use calculate length of dictionary by using len function
```python
>>> print(len(items))
5
```
Sort dictionary by key:
```python
>>> items = dict(sorted(items.items()))
>>> items
{'description': 'some descriptions', 'name': 'milk powder', 'price': 400.0, 'qty': 1, 'related_items': []}

```

Sort dictionary by values:
here few things to note
1. If dictionary value is numeric then you can simply write the follwong code. It will sort dictionary items by ascending order by value
```python
>>> items = dict(sorted(items.items(), key=lambda x:x[1]))
```
if you want to sort descending order by value
```python
>>> items = dict(sorted(items.items(), key=lambda x:x[1], reverse=True))
```
2. If dictionary is string then you have to write additional comprator, if you just write with lambda function then you will get some error as shown
```python
>>> items = dict(sorted(items.items(), key=lambda x:x[1]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'float' and 'str'
```

Please note: dictionary value must be of same type if you want to sort it.

Now take an exple you want to sort followung dictionary
```python
user_items_mapping={
    'abc':4,
    'xyz':44,
    'pqr':33
}
```
```python
>>> dict(sorted(user_items_mapping.items(), key=lambda x:x[1]))
{'abc': 4, 'pqr': 33, 'xyz': 44}
```
If you wwant to sort in descending order then add reverse=True
```python
>>> dict(sorted(user_items_mapping.items(), key=lambda x:x[1], reverse=True))
{'xyz': 44, 'pqr': 33, 'abc': 4}
```

Now solve one Leetcode question to understand the whole dictionary concept
!(1636. Sort Array by Increasing Frequency)[https://i.imgur.com/yUlFzcg.png]

```python
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        items = {}
        
        # Count frequency of elements
        for ele in nums:
            if ele in items:
                items[ele] += 1
            else:
                items[ele] = 1
        
        # Sort elements in decending by key
        items = dict(sorted(items.items(), reverse=True)) # sort by a
        # Now sort elements in ascending order by frequency which means value
        items = dict(sorted(items.items(), key=lambda x: x[1]))

        # Now add final dictionary to result array and return
        res = []
        for key in items:
            res += [key]*items[key]
        return res
```
