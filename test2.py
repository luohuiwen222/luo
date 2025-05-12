import time

print (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
import os

# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)

# 列出目录下的文件
files = os.listdir(current_dir)
print("目录下的文件:", files)

from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()

# 计算 10 天后的时间
future_time = now + timedelta(days=-10)
print("10 天后的时间:", future_time)


import re

pattern = "(ab)+"
text = "ababab"

match = re.search(pattern, text)
if match:
    print("匹配成功:", match.group())

    import re

    pattern = r"hello"
    text = "a hello world"

    match = re.match(pattern, text)
    if match:
        print("匹配成功:", match.group())
    else:
        print("匹配失败")

        import re

        pattern = r"\d{3}-\d{3}-\d{4}"
        text = "My phone number is 123-456-7890."

        match = re.search(pattern, text)
        if match:
            print("找到的电话号码:", match.group())

            import sys

            print("脚本名称:", sys.argv[0])
            print("参数列表:", sys.argv[1:])
