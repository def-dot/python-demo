class Solution:
    def force_t(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        l = max(len(v1), len(v2))
        for i in range(l):
            temp1 = 0
            temp2 = 0
            if i < len(v1):
                temp1 = int(v1[i])
            if i < len(v2):
                temp2 = int(v2[i])
            if temp1 > temp2:
                return 1
            elif temp1 < temp2:
                return -1
        return 0

    def compare(self, version1: str, version2: str) -> int:
        n1 = len(version1)
        n2 = len(version2)
        i, j = 0, 0
        # 直到某个字符串结束
        while i < n1 or j < n2:
            num1 = 0
            # 从下一个点前截取数字
            while i < n1 and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1
            # 跳过点
            i += 1
            num2 = 0
            # 从下一个点前截取数字
            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1
            # 跳过点
            j += 1
            # 比较数字大小
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        # 版本号相同
        return 0


if __name__ == "__main__":
    v1 = "1.01.0.0"
    v2 = "1.1"
    # r = Solution().force_t(v1, v2)
    r = Solution().compare(v1, v2)
    print(r)
