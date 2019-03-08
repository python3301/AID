import re

pattern = r'(ab)cd(?P<pig>)ef'

regex = re.compile(pattern)

#获取match对象
obj = regex.search("abcdefgh",pos=0,endpos=6)

###### match 属性变量 ######
print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)
print("****************")
########match属性方法###########
print(obj.span())#起止位置
print(obj.start())#起始位置
print(obj.end())#结束位置

print(obj.groupdict())#获取捕获组字典，组名为键，对应内容为值
print(obj.groups())#获取子组对应内容

print("******************")
print(obj.group())
print(obj.group(1))#获取第一个子组内容
print(obj.group(2))#获取对应捕获组内容