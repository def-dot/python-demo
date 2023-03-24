# 动态规划 最大子序和
# https://leetcode.cn/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/

def dynamic_t(nums):
    # 动态规划
    sums = [0]
    for item in nums:
        latest_sum = sums[-1]
        if latest_sum > 0:
            sums.append(latest_sum + item)
        else:
            sums.append(item)
    sums.sort()
    return sums[-1]


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = dynamic_t(nums)
    print(max_sum)
