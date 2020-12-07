
""" 使用time.time()计算函数执行时间 """

import time

def exec_time(count):
    start = time.time()
    i = 0
    while i < count:
        i += 1
    end = time.time()
    exec = end - start
    print(f"count = {count}, This function performed for {exec} seconds")

exec_time(200)  # 如果执行时间太短 结果显示为0.0
exec_time(200000)   # 需要提高数据量才能看到结果



