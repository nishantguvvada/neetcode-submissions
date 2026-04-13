class Solution:
    def reverse(self, x: int) -> int:
        reversed_digit = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            last_digit = x % 10
            reversed_digit = reversed_digit * 10 + last_digit
            x = x // 10

        result = reversed_digit * sign
        if result < -2**31 or result > 2**31-1:
            return 0
        else:
            return result