def get_dict():
    """返回一个字典，对于1-60得'D',61-70得'C',71-80得'B',81-90得'A',91-100得'S'。"""
    res = {}
    for i in range(1, 101):
        if i <= 60: res[str(i)] = 'D'
        elif i <= 70: res[str(i)] = 'C'
        elif i <= 80: res[str(i)] = 'B'
        elif i <= 90: res[str(i)] = 'A'
        else: res[str(i)] = 'S'
    return res    
