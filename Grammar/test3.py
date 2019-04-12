import requests
from bs4 import BeautifulSoup
from io import BytesIO

# r = requests.get('https://api.github.com/events')
#
# r_post = requests.post('http://httpbin.org/post', data = {'key':'value'})
# r_opt = requests.options('http://httpbin.org/get')
# # print(r_opt.url)
# print(r.encoding)
# r_jso = r.json()
# print(r_jso)

# Type
class A:
    pass

class B(A):
    pass

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))
print("isinstance(A(), A): ", isinstance(A(), A))
print("type(A()) == A: ", type(A) == A)
print("isinstance(B(), A): ", isinstance(B(), A))
print("type(B()) == A: ", type(B()) == A)

# String
word = "Python"
print("word: ", word)
print("word[0]: ", word[0])
print("word[-2]: ", word[-2])
print("word[0: 5]: ", word[0: 5])
print("word[0: 5: 2]: ", word[0: 5: 2])

# List
list1 = ['abcd', 786, 2.23, "Runnoob", 70.2]
print(list1)
print(list1 * 2)
print(list1[0: 3: 2])
list1[0: 3] = []
print(list1[0: 4])
print()

# Tuple
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
print()

# Set
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素
print()

# Dictionary
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob',
            'code': 1,
            'site': 'www.runoob.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
