#   [1.3.2] 高级运算

# ----------------- #

#   与（AND）运算
#   使用 bool() 时代表输出逻辑运算值

print(bool(0 and 0))
# 输出：false

print(bool(1 and 1))
# 输出：true

print(bool([] and ['1']))
# 输出：false

print(bool((1) and ['1']))
# 输出：true

print(0 and 9)
# 输出：0

print(('34') and [])
# 输出：[]

# ----------------- #

#   或（OR）运算
#   使用 bool() 时代表输出逻辑运算值

print(bool(0 or 0))
# 输出：false

print(bool(1 or 1))
# 输出：true

print(bool([] or ['1']))
# 输出：true

print(bool((1) or ['1']))
# 输出：true

print(0 or 9)
# 输出：9

print(('34') or [])
# 输出：'34'

# ----------------- #

#   非（NOT）运算
#   只会输出布尔值

print(not True)
# 输出：False

print(not False)
# 输出：True

print(not 0)
# 输出：True

print(not 10)
# 输出：False

print(not [])
# 输出：True

print(not [1, 2, 3])
# 输出：False