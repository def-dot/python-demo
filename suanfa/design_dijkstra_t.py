"""
无向有权图 有向有权图 邻接矩阵 最短路径（贪心算法）
打印出路径 距离
"""


class Solution:
    def __init__(self, nums, src, dst):
        self.nums = nums
        self.src = src
        self.dst = dst
        self.open = {src: 0}
        self.close = {}
        self.parent = {}

    def optimize(self):
        while True:
            min_k = min(self.open, key=lambda x: self.open[x])
            if min_k == self.dst:
                child = min_k
                path = [child]
                while True:
                    p = self.parent.get(child)
                    if not p:
                        break
                    path.append(p)
                    child = p
                return self.open[min_k], path[::-1]

            self.close[min_k] = self.open[min_k]
            del self.open[min_k]

            nexts = self.nums.get(min_k)
            for k in nexts:
                if k in self.close:
                    continue

                distance = nexts[k] + self.close[min_k]
                if k not in self.open or self.open[k] > distance:
                    self.open[k] = distance
                    self.parent[k] = min_k


if __name__ == "__main__":
    nums = {
        "A": {"B": 6, "C": 3},
        "B": {"A": 6, "C": 2, "D": 5},
        "C": {"A": 3, "B": 2, "D": 3, "E": 4},
        "D": {"B": 5, "C": 3, "E": 2, "F": 3},
        "E": {"C": 4, "D": 2, "F": 5},
        "F": {"D": 3, "E": 5}
    }
    # 求从A出发，到B、C、D的最短路径, [0, 2, 5, 4]
    r = Solution(nums, 'A', 'D').optimize()
    print(r)
