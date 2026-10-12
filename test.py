import time

line = "Thu Mar 19 15:16:25 2026 0 192.168.2.67 6 test.txt b - o u test1@192.168.2.159 ftp 1 test1@192.168.2.159 c"
parts = line.strip().split()

# 1. 提取前 5 个字段并拼接
time_str = " ".join(parts[:5])

# 2. 定义格式化字符串
# %a: 星期, %b: 月份简写, %d: 日期, %H:%M:%S: 时间, %Y: 年份
time_format = "%a %b %d %H:%M:%S %Y"

# 3. 转换为时间元组 (Time Tuple)
time_struct = time.strptime(time_str, time_format)

# 4. 转换为时间戳 (Timestamp)
timestamp = int(time.mktime(time_struct))

print(f"原始字符串: {time_str}")
print(f"Unix 时间戳: {timestamp}")