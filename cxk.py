import chardet

# 读取文件的一部分内容用于检测编码
with open('f:\\csv.py', 'rb') as f:
    raw_data = f.read(1024)
    result = chardet.detect(raw_data)
    encoding = result['encoding']

try:
    # 使用检测到的编码打开文件进行读取
    with open('f:\\csv.py', 'r', encoding=encoding) as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("文件未找到。")
except UnicodeDecodeError:
    print("使用检测到的编码解码文件时出错。")