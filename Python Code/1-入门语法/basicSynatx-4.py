#   [1.4] 导入库
#   1.基本导入

import time # 导入 time 库
print(time.time()) # 使用 time 库内的函数

#   2. 指定导入
from time import strftime # 指定从 time 库中导入 strftime 函数
print(strftime("%X")) # 使用函数

#   3. 相对导入
from basicSynatx4.test import run # 从 basicSynatx 文件夹中的 test.py 导入 run 函数
run() # 使用函数