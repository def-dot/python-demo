# 多数元素
# https://leetcode.cn/problems/majority-element/solution/duo-shu-yuan-su-by-leetcode-solution/

def hahs_t(nums):
    ht = {}
    for item in nums:
        if item not in ht:
            ht[item] = 0
        ht[item] += 1
    max_num = max(ht, key=lambda k: ht[k])
    return max_num


if __name__ == '__main__':
    nums = [3, 2, 3]
    max_sum = hahs_t(nums)
    print(max_sum)
