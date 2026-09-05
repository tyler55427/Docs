# 字典（map）
# 排序不重要
import pprint


mycat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
print(mycat['size'])

# 打印对应建、值、键值对
for i in mycat.keys():
    print(i,end=' ')
print()
for i in mycat.values():
    print(i,end=' ')
print()
# 返回的是元组
for i in mycat.items():
    print(i,end=' ')
print()

print('fat' in mycat.values())
# 根据key返回value, 没有可以自定义返回值
print(mycat.get('color'))
print(mycat.get('color',0))
# 设置默认值（如果原本有key，则不改变值）
mycat.setdefault('age','15')
print(mycat)
# 美观输出，排序
pprint.pprint(mycat)

