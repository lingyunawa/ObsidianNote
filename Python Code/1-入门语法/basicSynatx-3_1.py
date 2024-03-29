#   [1.3.1] 数学运算

# ----------------- #

#   加运算
print(1 + 1)
# 输出：2

print(1.1 + 1.1)
# 输出：2.2

print("1" + "1")
# 输出：11

print([1, 2] + [3, 4])
# 输出：[1, 2, 3, 4]

print((1, 2) + (3, 4))
# 输出：(1, 2, 3, 4)

# 注：这里这段代码必定报错，所以加了个 try-except 保护代码不会直接中断
try:
    print(1 + "1")
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
except TypeError as ex:
    print(f"执行 print(1 + \"1\") 的时候发生 TypeError：{ex}")

print(True + True)
# 输出：2

# ----------------- #

#   减运算
print(3 - 2)
# 输出：1

print(1.1 - 1.1)
# 输出：0.0

# ----------------- #

#   乘运算
print(1 * 2)
# 输出：2

print(3.3 * 1.6)
# 输出：5.28

print("Hello" * 3)
# 输出：HelloHelloHello

print([12, 7] * 5)
# 输出：[12, 7, 12, 7, 12, 7, 12, 7, 12, 7]

print((9, 12) * 0)
# 输出：()

# 注：这里这段代码必定报错，所以加了个 try-except 保护代码不会直接中断
try:
    print("7" * 1.1)
    # TypeError: can't multiply sequence by non-int of type 'float'
except TypeError as ex:
    print(f"执行 print(\"7\" * 1.1) 的时候发生 TypeError：{ex}")

# ----------------- #

#   除运算

print(4 / 2)
# 输出：2

print(3.2 / 1.9)
# 输出：1.6842105263157896

print(7 // 3.2)
# 输出：2.0

# 注：这里这段代码必定报错，所以加了个 try-except 保护代码不会直接中断
try:
    print(13 / 0)
    # ZeroDivisionError: division by zero
except ZeroDivisionError as ex:
    print(f"执行 print(13 / 0) 的时候发生 ZeroDivisionError：{ex}")

# ----------------- #

#   运算赋值缩写

a = 7; b = 6 # 这里用分号分隔两句语句，短一点
a += b
print(a)
# 输出：13

a = 7; b = 6 # 这里用分号分隔两句语句，短一点
a = a + b
print(a)
# 输出：13
