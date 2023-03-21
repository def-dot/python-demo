# 合并两个有序数组
# refer: https://leetcode.cn/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/


def append_and_sort_t(nums1, nums2):
    # 追加，排序
    nums1.extend(nums2)
    nums1.sort()


def double_point_t(nums1, nums2):
    # 双指针
    sorted = []
    p1, p2 = 0, 0
    while p1 < len(nums1) or p2 < len(nums2):
        if p1 == len(nums1):
            sorted.append(nums2[p2])
            p2 += 1
        elif p2 == len(nums2):
            sorted.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            sorted.append(nums1[p1])
            p1 += 1
        else:
            sorted.append(nums2[p2])
            p2 += 1
    return sorted


if __name__ == '__main__':
    nums1 = [2, 3, 9]
    nums2 = [3, 4, 10]
    # append_and_sort_t(nums1, nums2)
    res = double_point_t(nums1, nums2)
    print(res)
