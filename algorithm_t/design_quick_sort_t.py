"""
快速排序 分治算法
"""
from typing import List


class Solution:
    def force_t(self, nums: List[int], start: int, end: int) -> List[int]:
        if start >= end:
            return
        pivot = nums[start]
        l = start
        r = end

        while l < r:
            while nums[r] > pivot and l < r:
                r -= 1

            nums[l] = nums[r]

            while nums[l] < pivot and l < r:
                l += 1

            nums[r] = nums[l]

        nums[l] = pivot
        self.force_t(nums, start, l)
        self.force_t(nums, l+1, end)
        return nums


if __name__ == '__main__':
    nums = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    r = Solution().force_t(nums, 0, len(nums)-1)
    print(r)
