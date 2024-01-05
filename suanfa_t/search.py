# 二分查找
class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        m = len(nums) // 2
        if nums[m] > target:
            return self.search(nums[:m], target)
        elif nums[m] < target:
            return self.search(nums[m:], target)
        else:
            return m
        
    def search2(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


if __name__ == '__main__':
    nums = [-1, 3, 9 ,11]
    r = Solution().search2(nums, 9)
    print(r)
