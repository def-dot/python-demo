# https://leetcode.cn/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
# 给定字符串数组，求公共前缀


def prefix_t(strs):
    res = []
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if len(strs[j]) <= i:
                return ''.join(res)
            if strs[j][i] != c:
                return ''.join(res)
        res.append(c)
    return ''.join(res)


if __name__ == '__main__':
    strs = ["ab", "a"]
    res = prefix_t(strs)
    print(res)
