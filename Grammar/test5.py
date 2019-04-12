# Fibonacci series


# First Step
a, b = 1, 1
while b < 15:
      print(a, end = " ")
      a, b = b, a + b
print(a)

# Second Step
var1 = 100
if var1:
      print("1 - if 表达式为True")
      print(var1)
var2 = 0
if var2:
      print("2 - if 表达式为True")
      print(var2)
print("Goodbye!")

# Third Step
"""
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
"""

# while
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

# for
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# range()
for i in range(5):
      print(i)
      for j in range(5, 9):
            print(j, end = "")
      print()
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
      print(i, a[i])

# break, continue
for letter in 'Runoob':     # 第一个实例
   if letter == 'b':
      break
   print ('当前字母为 :', letter)
var = 10                    # 第二个实例
while var > 0:              
   print ('当期变量值为 :', var)
   var = var -1
   if var == 5:
      break
print ("Good bye!")

# pass
# pass语句不做任何事情，单纯的占位置所用