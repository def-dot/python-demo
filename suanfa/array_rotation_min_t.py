class Solution:
    def force_t(self, nums: list[int]) -> int:
        res = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                res = nums[i+1]
                break
        if res is None:
            res = nums[0]
        return res

    def optimize_t(self, nums: list[int]) -> int:
        print(nums)
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        if nums[mid] > nums[len(nums)-1]:
            return self.optimize_t(nums[(mid+1):])
        elif nums[mid] < nums[len(nums)-1]:
            return self.optimize_t(nums[:(mid+1)])
        else:
            if len(nums) == 2:
                return nums[0] if nums[0] < nums[1] else nums[1]
            return self.optimize_t(nums[:len(nums)-1])


if __name__ == "__main__":
    nums = [1, 0, 1, 1, 1]
    # [1, 0, 1, 1, 1]
    # [1, 0, 1, 1]
    # [1, 0, 1]
    # [1, 0]
    """
    1. 7//2=3 a[3]=7 -> 7>3 -> [7,1,2,3]
    2. 4//2=2 a[2]=2 -> 2<3 -> [7,1]
    3. 2//2=1 a[1]=1 -> 
    """
    r = Solution().optimize_t(nums)
    print(r)
