"""
dijkstra 主要使用了贪心算法
"""
from typing import List

class Solution:
    def optimize(self, nums: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    nums = [
        [0, 2, -1, 6],
        [2, 0, 3, 2],
        [-1, 3, 0, 2],
        [6, 2, 2, 0],
    ]
    # 求从A出发，到B、C、D的最短路径, [0, 2, 5, 4]
    r = Solution().optimize(nums)
    print(r)
