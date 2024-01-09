# 贪心算法，主持人调度
class Solution:
    def min_host(self, nums):
        start = []
        end = []
        for t in nums:
            start.append(t[0])
            end.append(t[1])
        start.sort()
        end.sort()
        print(start)
        print(end)
        r = 0
        j = 0
        for i in range(len(nums)):
            if start[i] < end[j]:
                r += 1
            else:
                j += 1
        return r


if __name__ == "__main__":
    plans = [[1,6],[2,4],[4,5]]
    r = Solution().min_host(plans)
    print(r)
