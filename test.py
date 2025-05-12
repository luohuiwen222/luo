import re
pattern = re.compile(r'''
    ^(?P<username>\w+)  # 用户名
    :(?P<password>\S+)  # 密码
    @(?P<domain>\w+\.\w+)  # 域名
$''', re.VERBOSE)

m = pattern.match("john:pass123@example.com")
if m:
    print(m.groupdict())  # 输出: {'username': 'john', 'password': 'pass123', 'domain': 'example.com'}

