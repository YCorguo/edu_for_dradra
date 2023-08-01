## python
### 遍历字典
```python
d = {
    'a' : 'bb',
    'b' : 'cc',
}
for key, value in d.items():
    print(key, value)
# d.keys()
# d.values()
```

### [Python标准库](http://pymotw.com)

### 编码风格
#### 类：驼峰命名法

### 读取文件
  1. 使用with
  2. ```read()```：读取全文作为字符串。
  3. ```readline()```：读取一行作为字符串。
  4. ```readlines()```：读取全文作为字符串列表。

### 异常处理
#### 异常
  1. ZeroDivisionError
  2. FileNotFoundError
  3. ValueError
#### 处理
  ```
  try:
      xxx
  except FileNotFoundError:
      pass
  except ZeroDivisionError:
      pass
  else:
      pass
  ```

### 数据存储
#### json
  1. json.dump(my_str, f)
  2. a = json.load(f)


