# 两个有序数组合并
class Solution:
    def merge(self, arr1, arr2):
        r = []
        p1 = 0
        p2 = 0
        while arr1 and arr2 and p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] < arr2[p2]:
                r.append(arr1[p1])
                p1 += 1
            else:
                r.append(arr2[p2])
                p2 += 1
        if p1 < len(arr1):
            r.extend(arr1[p1:])
        if p2 < len(arr2):
            r.extend(arr2[p2:])
        return r
    
    def merge2(self , A, m, B, n):
        # write code here
        r = []
        p1 = 0
        p2 = 0
        while A and B and p1 < len(A) and p2 < len(B):
            if A[p1] < B[p2]:
                r.append(A[p1])
                p1 += 1
            else:
                r.append(B[p2])
                p2 += 1
        if p1 < len(A):
            r.extend(A[p1:])
        if p2 < len(B):
            r.extend(B[p2:])
        return r


if __name__ == "__main__":
    arr1 = []
    arr2 = [1]
    r = Solution().merge2(arr1, 0, arr2, 1)
    print(r)
