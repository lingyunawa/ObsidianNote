#   [1.1] 基础函数

# ----------------- #

#   1. 输出函数
print("Hello, World!")  # 输出括号内的内容到控制台

# ----------------- #

#    2. 输入函数
name = input("Enter your name: ")  # 接受用户输入名字
print("Hello, " + name)  # 输出 Hello, 加上你输入的名字

# ----------------- #

#    3. 长度函数
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # 获取列表的长度

# ----------------- #


# 4. 范围函数
numbers = range(1, 5)
for num in numbers:
    print(num)  # 生成范围内的整数序列

# ----------------- #


#    5. 类型函数
x = 5
print(type(x))  # 获取对象的类型

# ----------------- #

#    6. 整数函数
num_str = "10"
num_int = int(num_str)
print(num_int)  # 将字符串转换为整数

# ----------------- #

# 7. 字符串函数
num = 10
num_str = str(num)
print(type(num_str))  # 将对象转换为字符串

# ----------------- #

#    8. 列表函数
numbers_tuple = (1, 2, 3)
numbers_list = list(numbers_tuple)
print(numbers_list)  # 将元组转换为列表

# ----------------- #

#   9. 最大值函数
numbers = [3, 6, 1, 9, 4]
max_num = max(numbers)
print(max_num)  # 返回列表中的最大值

# ----------------- #

#   10. 最小值函数
numbers = [3, 6, 1, 9, 4]
min_num = min(numbers)
print(min_num)  # 返回列表中的最小值
