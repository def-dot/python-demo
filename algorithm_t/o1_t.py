# https://leetcode.cn/problems/insert-delete-getrandom-o1/solution/o1-shi-jian-cha-ru-shan-chu-he-huo-qu-su-rlz2/
# O(1)时间复杂度，插入、删除、随机获取、取最小元素。


class C:
    def __init__(self):
        self.nums = []
        self.ht = {}

    def insert(self, val):
        if val not in self.ht:
            self.ht[val] = len(self.nums)
            self.nums.append(val)

    def delete(self, val):
        index = self.ht.get(val)
        del self.ht[val]
        self.nums.pop(index)

    def get_random(self):
        import random
        return random.choice(self.nums)


if __name__ == '__main__':
    nums = [3, 5, 9, 7]
    c = C()
    for item in nums:
        c.insert(item)

    print(c.get_random())

    c.delete(3)

