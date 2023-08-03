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
```

### 底层逻辑
#### 创建
  实现空列表的创建
  ```
  def CreateList(): -> list
      return []

  # a = CreateList()
  # a = []
  ```

#### 判空
  ```
  def ListEmpty(a : list): -> bool
      if len(a) == 0: return False
      return True
  ```

#### 插入
  实现在i位置的插入
  ```
  def IndexInsert(a : list, id : int, elem : int): -> bool
      if id < 0 or id > len(a): return False
      a.append(0)
      for i in range(len(a) - 1, id, -1):
          a[i] = a[i - 1]
      a[id] = elem
      # a = a[:id] + [elem] + a[id:]
      return True

  # IndexInsert(a, 3, 7)
  # a.insert(3, 7)
  ```
  实现第一个某元素前的插入
  ```
  def ElementInsert(a : list, elem : int, x : int): -> bool
      i = 0

      while i < len(a) and a[i] != elem:
          i += 1
      if i == len(a):
          return False
      return IndexInsert(a, i, x)
  # ElementInsert(a, 3, 7)
  ```

#### 修改
  ```
  def ModifyList(a : list, id : int, x : int): -> bool
      if id < 0 or id > len(a): return False
      a[id] = x
      return True
  def ModifyElemInList(a : list, elem : int, x : int): -> bool
      if id < 0 or id > len(a) : return False
      for i in range(len(a)):
          if a[i] == elem:
              a[i] = x
              return True
      return False
  ```

#### 查找
  ```
  def FindSecondElem(a : list, elem : int): -> int
      cnt = 0
      for i in range(len(a)):
          if a[i] == elem:
              cnt += 1
              if cnt == 2: return i
      return -1
  ```

#### 删除
  ```
  def DeleteSecondElem(a : list, elem : int): -> bool
      i = 0
      t = 0
      k = -1
      while i < len(a): 
          if a[i] == elem:
              t += 1
              if t == 2:
                  k = i
          i += 1
      if k == -1: return False
      for i in range(k, len(a)):
          a[i] = a[i + 1]
      a.pop()
      return True
  def DeleteSecondElem2(a : list, elem : int): -> bool
      id = FindSecondElem(a, elem)
      if id == -1: return False
      # a = a[:id] + a[id+1:]
      while id < len(a) - 1:
          a[id] = a[id + 1]
          id += 1
      a.pop()
      return True
  ```


















