import re

# regex = re.compile(r'\w+',flags=re.A)#re.A 使用ascii字符 所以不会显示 北京
# regex = re.compile(r'[a-z]+',flags=re.I) 忽略大小写
# regex = re.compile(r'.+',flags=re.DOTALL) 可以匹配换行
# regex = re.compile(r'^北京',flags=re.M) #可以匹配每一行的开头结尾位置
# .............................flags=re.X 为正则注释

s ='''Welcome to
北京
'''
l = regex.findall(s)
print(l)