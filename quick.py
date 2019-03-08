#快速排序
#原始数据
#value = [91,60,20,120,149,48,100,50,75,70]

def quick(value):
    #递归退出条件
    if len(value) < 2:
        return value
    #设置关键数据
    A = value[0]
    #找出所有比A大的数据
    big = [x for x in value if x > A]
    #找出比A小的数据
    small = [x for x in value if x < A]
    #拼接数据排序结果
    return quick(small) + equal + quick(big)
    