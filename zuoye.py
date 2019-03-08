import re
f = open('文档')
data = f.read()
#大写字母开头单词
pattern1 = r'\b[A-Z]\S*'
#数字
pattern2 = r'-?\d+\.?/?\d*%?'
#日期格式替换
pattern3 = r'\d{4}-\d{1,2}-\d{1,2}'

for i in regex.finditer(data):
    print(i.group())
