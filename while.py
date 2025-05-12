n=100
sum=0
conuter=1
while conuter <=n:
    sum=sum+conuter
    conuter += 1
print("1到100之和为：%d" % (sum))
print("1 到 %d 之和为: %d" % (n,sum))

import time
import sys


def progress_bar(current, total, bar_length=50):
    """
    显示进度条
    :param current: 当前进度
    :param total: 总进度
    :param bar_length: 进度条长度
    """
    percent = current / total
    arrow = '=' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    # 添加颜色（可选）
    color_code = 32  # 绿色
    if percent > 0.7:
        color_code = 33  # 黄色
    if percent > 0.9:
        color_code = 31  # 红色

    # 格式化输出
    sys.stdout.write(f"\r\033[{color_code}m进度: [{arrow + spaces}] {current:3d}/{total} ({percent:.0%})\033[0m")
    sys.stdout.flush()


# 使用示例
total = 100
for i in range(total + 1):
    progress_bar(i, total)
    time.sleep(0.05)

print("\n完成！")  # 完成后换行