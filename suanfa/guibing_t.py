# 归并排序 分治算法
def merge(l1, l2):
    res = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    if i < len(l1):
        res.extend(l1[i:])
    if j < len(l2):
        res.extend(l2[j:])
    return res


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    s1 = nums[:mid]
    s2 = nums[mid:]
    l1 = merge_sort(s1)
    l2 = merge_sort(s2)
    return merge(l1, l2)


if __name__ == '__main__':
    nums = [14, 2, 34, 43, 21, 19]
    res = merge_sort(nums)
    print(res)
