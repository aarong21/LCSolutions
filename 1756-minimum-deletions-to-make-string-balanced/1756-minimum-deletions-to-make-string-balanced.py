class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count_right = [0]*n

        for i in range(n-2, -1, -1):
            a_count_right[i] = a_count_right[i+1]
            if s[i+1] == 'a':
                a_count_right[i] += 1

        b_count_left = 0
        res = float('inf')

        for i,c in enumerate(s):
            res = min(res, b_count_left + a_count_right[i])
            if c == 'b':
                b_count_left += 1
        return res