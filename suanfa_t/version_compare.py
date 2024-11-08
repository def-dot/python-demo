# 版本比较
# 方法一：双指针
# 方法二：分割比较

class Solution:
    def compare(self, v1, v2):
        # 分割比较
        v1 = v1.split('.')
        v2 = v2.split('.')
        i = 0
        for i in range(max(len(v1), len(v2))):
            t1 = int(v1[i]) if i < len(v1) else 0
            t2 = int(v2[i]) if i < len(v2) else 0
            if t1 > t2:
                return 1
            elif t1 < t2:
                return -1
        return 0


if __name__ == "__main__":
    v1 = "1.0"
    v2 = "1.0.0"
    r = Solution().compare(v1, v2)
    print(r)
