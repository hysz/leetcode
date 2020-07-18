class Solution:
    def reverse(self, x: int) -> int:
        # Answer stored in `y`
        y = 0

        # Should we negate?
        is_positive = True
        if x < 0:
            is_positive = False
            x *= -1
            
        # Find y
        while x > 0:
            y = y * 10 + (x % 10)
            x = int(x / 10)
        y = y if is_positive else -y

        # Handle overflow
        if not -pow(2,31) <= y <= pow(2,31) - 1:
            return 0

        # We done!
        return y


print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(0))
print(Solution().reverse(1))
print(Solution().reverse(120))
print(Solution().reverse(1534236469))