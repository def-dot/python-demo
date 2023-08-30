"""
找零钱 贪心算法
"""


class Solution:
    def __init__(self):
        self.coins = [10, 5, 1]

    def force_t(self, amount: int) -> int:
        r = []
        coin = self.coins.pop(0)
        while True:
            if amount >= coin:
                r.append(coin)
                amount -= coin
                if amount == 0:
                    print(f'success {r}')
                    break
            else:
                if self.coins:
                    coin = self.coins.pop(0)
                else:
                    print(f'fail {r}')
                    break

    def optimize_t(self, amount: int) -> int:
        r = []
        for coin in self.coins:
            while amount >= coin:
                amount -= coin
                r.append(coin)
            if amount == 0:
                print(f'success {r}')
                break
        if amount > 0:
            print(f'fail {r}')


if __name__ == '__main__':
    # r = Solution().force_t(42)
    r = Solution().optimize_t(42)
