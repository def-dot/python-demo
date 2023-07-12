
count = 0
class Solution:
    def force_t(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
        return count

    def optimize_t(self, nums: list[int]) -> int:
        global count
        mod = 1000000007
        def merge(nums1, nums2):
            global count
            res = []
            i = 0
            j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] > nums2[j]:
                    count += len(nums1) - i
                    count = count % mod
                    res.append(nums2[j])
                    j += 1
                else:
                    res.append(nums1[i])
                    i += 1
            res += nums1[i:]
            res += nums2[j:]
            return res

        def divide(nums):
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left = nums[:mid]
            rl = divide(left)
            right = nums[mid:]
            rr = divide(right)
            print(f"rl rr {rl} {rr}")
            return merge(rl, rr)

        r = divide(nums)
        print(f"r {r}")
        return count


if __name__ == "__main__":
    nums = [627126, 415347, 850134, 371085, 279048, 705820, 453064, 944751, 92317, 58592, 167988, 284065, 992573, 78043, 190215, 104546, 607528, 391775, 701214, 849731, 231053, 603058, 975374, 199773, 479544, 143961, 206797, 325662, 90035, 69615, 429916, 717161, 484962, 796403, 604598, 280362, 502223, 57662, 741466, 594540, 632606, 909454, 394957, 625180, 503849, 585172, 729726, 627729, 976947, 947293, 477461, 724352, 66703, 452835, 440478, 62599, 596797, 163627, 388261, 203184, 233243, 334529, 436697, 234557, 647284, 41295, 514920, 665859, 615310, 256386, 776752, 247916, 682192, 171709, 389448, 186041, 273234, 635527, 813771, 766533, 582820, 807584, 490886, 649523, 260419, 447716, 228474, 373568, 611343, 616735, 576752, 844586, 467616, 529801, 595496, 631253, 571097, 110416, 297112, 186407, 883154, 73864, 950675, 81698, 245574, 340124, 267739, 35160, 975651, 597862, 801693, 74823, 921798, 292579, 240698, 182218, 256647, 469172, 72138, 867991, 602259, 165243, 228929, 69875, 695044, 824425, 701128]
    print(len(nums))
    # nums = [1, 2, 3, 4, 5, 6, 7, 0]
    """
    [1, 2, 3, 4]  [5, 6, 7, 0]
    [1,2] [3,4] [5,6] [7,0]
    [1] [2] [3] [4] [5] [6] [7] [0]
    ===>
    [1,2] [3,4] [5,6] [0,7] +1=1
    [1,2,3,4] [0,5,6,7] +2=3
    [0,1,2,3,4,5,6,7] +4=7
    """
    r = Solution().optimize_t(nums)
    print(r)