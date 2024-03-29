#   [1.2] 循环

# ----------------- #

#   for 循环
fruits = ["apple", "banana", "cherry"]
for fruit in fruits: # 遍历列表
    print(fruit)
#   输出：
#   apple
#   banana
#   cherry

for char in "hello": # 遍历字符串
    print(char)
#   输出：
#   h
#   e
#   l
#   l
#   o

for i in range(5): # 遍历数字范围
    print(i)
#   输出：
#   0
#   1
#   2
#   3
#   4

# ----------------- #

#   while 循环
i = 1
while i <= 5:
    print(i)
    i += 1
print("i > 5，循环已结束")

#   输出：
#   1
#   2
#   3
#   4
#   5
#   i > 5，循环已结束

# ----------------- #

#   break 使用
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana": break
    print(fruit)
print('loop breaked')

# 输出
# apple
# loop breaked

# ----------------- #
