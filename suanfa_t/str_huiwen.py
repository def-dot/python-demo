# 回文字符串检测
class Solution:
    def check(self, val):
        left = 0
        right = len(val) - 1
        while left < right:
            if val[left] != val[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    s = "hellollehs"
    r = Solution().check(s)
    print(r)
