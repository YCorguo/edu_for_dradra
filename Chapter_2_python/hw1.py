def gen_list1(n):
    """
        生成一个长度为n的列表，里面为1到n的立方。
    """
    a = []
    for i in range(n):
        i = i**3
        a.append(i)
    res = a
    return res

def gen_list2(n):
    """
        生成一个长度为5n的列表，要求其中不包含4的倍数，从小到大排列，两个元素之间间隔为1或2.
    """
    a = []
    k = 10*n
    for i in range(k): 
        if i % 4 != 0: 
            a.append(i)
        if len(a) == 5*n:
            break
    res = a
    return res

def ans_g1(n):
    return [i ** 3 for i in range(n)]

def ans_g2(n):
    res, i = [], 1
    while len(res) < 5 * n:
        if i % 4 != 0:
            res.append(i)
        i += 1
    return res


res1 = gen_list1(10)
res2 = gen_list2(100)

res3 = ans_g1(10)
res4 = ans_g2(100)

print(res1 == res3)
print(res2 == res4)
