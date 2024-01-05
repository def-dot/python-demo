# 数组中找出两数之和等于值的两个数
class Solution:
    def find_two_num(self, arr, target) -> None:
        i = 0
        while arr:
            i += 1
            t = arr.pop(0)
            if target - t in arr:
                n_i = arr.index(target-t)
                return i, n_i+i+1
        return -1
    
    def find_two_num_hash(self, arr, target) -> None:
        d = dict()
        for i in range(len(arr)):
            t = target - arr[i]
            if t not in d:
                d[arr[i]] = i
            else:
                return d[t]+1, i+1
        return None


if __name__ == "__main__":
    arr = [3,2,4]
    r = Solution().find_two_num_hash(arr, 5)
    print(r)
