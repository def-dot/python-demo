# 符号匹配
class Solution:
    def match(self, val):
        self.s = []
        for c in val:
            if c in ['{', '[', '(']:
                self.s.append(c)
            elif c == '}' and (not self.s or self.s.pop() != '{'):
                return False
            elif c == ']' and (not self.s or self.s.pop() != '['):
                return False
            elif c == ')' and (not self.s or self.s.pop() != '('):
                return False
        if self.s:
            return False
        return True


if __name__ == "__main__":
    val = "()"
    r = Solution().match(val)
    print(r)