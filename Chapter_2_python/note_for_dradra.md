# python

## list

### 初始化
```python
a = [] # []
a = [1, 2, 3] # [1, 2, 3]
a = list(range(3)) # [0, 1, 2]
a = [i for i in range(3)] # [0, 1, 2]
a = [i for i in range(20)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
a = [i for i in range(0, 20, 2)] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
a = [i for i in range(0, 20)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
a = [i for i in range(20) if i % 2 == 0] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### 基础操作
```python
a = list(range(5))
print(len(a)) # 5
print(type(a)) # '<class list>'
print(type(a) == 'list') # True
a.remove(2)
print(a) # [0, 1, 3, 4]
a.append(3)
print(a) # [0, 1, 3, 4, 3]

#list.remove
a.remove(3)
print(a) # [0, 1, 4, 3]
a.append(1)
a.append(1)
print(a) # [0, 1, 4, 3, 1, 1]
while 1 in a:
    a.remove(1)
print(a) # [0, 4, 3]

#list.insert
a.insert(0, 2)
print(a) # [2, 0, 4, 3]
a.insert(3, 2)
print(a) # [2, 0, 4, 2, 3]

#copy
b = a
print(b) # [2, 0, 4, 2, 3]
b.append(2)
print(b) # [2, 0, 4, 2, 3, 2]
print(a) # [2, 0, 4, 2, 3, 2]
c = a[:]
c.remove(2)
print(c) # [0, 4, 2, 3, 2]
print(a) # [2, 0, 4, 2, 3, 2]
