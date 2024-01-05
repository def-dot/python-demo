# 字符串数组公共前缀
class Solution:
    def find_common(self , s) -> str:
        if not s:
            return ""
        for i in range(len(s[0])):
            for j in range(1, len(s)):
                if len(s[j]) <=i or s[j][i] != s[0][i]:
                    return s[0][:i]
        return s[0]


if __name__ == "__main__":
    s = [
        'Hello world',
        'Hey how are you',
        'Here we are'
    ]
    r = Solution().find_common(s)
    print(r)
