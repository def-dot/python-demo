# 贪心算法，主持人调度
from typing import List
import functools
from queue import PriorityQueue

class Solution:
    def min_host(self, nums):
        start = []
        end = []
        for t in nums:
            start.append(t[0])
            end.append(t[1])
        start.sort()
        end.sort()
        r = 0
        j = 0
        for i in range(len(nums)):
            if start[i] < end[j]:
                r += 1
            else:
                j += 1
        return r
    
    def min_host2(self, nums):
        sorted_nums = sorted(nums, key=lambda x: (x[0], x[1]))
        # [[1, 6], [2, 4], [4, 5]]
        q = PriorityQueue()
        q.put(-1)
        for t in sorted_nums:
            v = q.get()
            if v > t[0]:
                # 开始时间小于结束时间
                q.put(v)
            q.put(t[1])
        return q.qsize()
    

if __name__ == "__main__":
    plans = [[4,5],[1,6],[2,4]]
    r = Solution().min_host2(plans)
    print(r)
