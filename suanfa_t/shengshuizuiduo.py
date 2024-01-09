# 盛水最多计算（双指针）
class Solution:
    def calc(self, nums):
        if len(nums) < 2:
            return 0
        r = 0
        left = 0
        right = len(nums)-1
        while left < right:
            r = max(min(nums[left], nums[right]) * (right - left), r)
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return r


if __name__ == "__main__":
    nums = [1,7,3,2,4,5,8,2,7]
    r = Solution().calc(nums)
    print(r)
