# 冒泡排序算法

def maopao(nums):
    l = len(nums)
    for i in range(l):
        for j in range(l-i-1):
            if nums[j] > nums[j+1]:
                tmp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = tmp


if __name__ == '__main__':
    nums = [2, 5, 3, 8, 6]
    maopao(nums)
    print(nums)
