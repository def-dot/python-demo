# 合并有序数组
# https://leetcode.cn/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/

def merge_t(nums1, nums2):
    # 时间复杂度 o(logn)
    nums1.extend(nums2)
    nums1.sort()
    return nums1


def double_point_t(nums1, nums2):
    # 双指针
    res = []
    i = 0
    j = 0
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


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 5, 6]
    # res = merge_t(nums1, nums2)
    res = double_point_t(nums1, nums2)
    print(res)
