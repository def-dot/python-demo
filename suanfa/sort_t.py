# 排序算法常用的有十种

def maopao_t(nums):
    # 冒泡
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j + 1]:
                t = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = t
    return nums


def dac_t(nums):
    # 分治
    # nums = [6, 9, 1, 4]
    def merge_two(nums1, nums2):
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i < len(nums1):
            res.extend(nums1[i:])
        if j < len(nums2):
            res.extend(nums2[j:])
        return res

    def split_nums(nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        left = split_nums(left)
        right = split_nums(right)
        res = merge_two(left, right)
        print(f"split_nums nums {nums} left {left} right {right} res {res}")
        return res

    res = split_nums(nums)
    return res


def quick_t(nums):
    # 快速排序
    # refer:https://blog.csdn.net/qq_40941722/article/details/94396010
    pass


if __name__ == "__main__":
    nums = [6, 1, 3, 4, 9]
    r = dac_t(nums)
    # r = maopao_t(nums)
    for i in r:
        print(i)

