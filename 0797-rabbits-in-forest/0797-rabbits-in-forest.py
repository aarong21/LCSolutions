class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # rabbs = set(answers)
        # return max(len(answers), len(rabbs) + sum(rabbs))

        count = Counter()
        res = 0
        for i in answers:
            if count[i] % (i + 1) == 0:
                res += i + 1
            count[i] += 1
        return res