# 数组移位
class Solution:
    def move(self, val, l): 
        l = l % len(val)
        val.reverse()
        left = val[:l]
        left.reverse() 
        right = val[l:]
        right.reverse() 
        val[:l] = left
        val[l:] = right
        return val

if __name__ == "__main__":
    s = [1,2,3,4,5]
    r = Solution().move(s, 7)
    print(r)
