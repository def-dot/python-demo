import re

def is_valid_domain(domain):
    # 定义域名正则表达式
    regex = r'^(http://|https://)?(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$'
    return re.match(regex, domain) is not None


r = is_valid_domain("www.baidu.com")
print(r)