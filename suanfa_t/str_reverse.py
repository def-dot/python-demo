# 字符串大小写互换并反转
class Solution:
    def trans(self , s: str) -> str:
        r = ""
        for c in s:
            if c.isupper():
                r += c.lower()
            elif c.islower():
                r += c.upper()
            else:
                r += c
        r = r.split(' ')[::-1]
        return ' '.join(r)
    

if __name__ == "__main__":
    s = "Hello World !"
    r = Solution().trans(s)
    print(r)
