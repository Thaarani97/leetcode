#TC: O(log(x))
#SC: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        positive = x > 0
        x = abs(x)
        rev = 0

        while x != 0:
            pop = x % 10
            x //= 10
            if rev > 214748364: # 2**31 // 10 == (2**31 - 1) // 10 == 214748364
                return 0
            rev = rev * 10 + pop
            
        return rev if positive else -rev