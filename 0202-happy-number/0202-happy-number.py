class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumSquares(n)
            if n == 1:
                return True
        return False

    def sumSquares(self, n: int) -> int:
        summ = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            summ += digit
            n = n // 10
        return summ