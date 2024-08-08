class Solution:
    def backtrack(self, n, left, right, out, res):
        # base case where left and right brace count = n
        if left >= n and right >= n:
            # join arr elements without separators
            outStr = "".join(out)
            res.append(outStr)
        # add left brace
        if left < n:
            out.append("(")
            self.backtrack(n, left+1, right, out, res)
            out.pop()
        # if right < left, add a right
        if right < left:
            out.append(")")
            self.backtrack(n, left, right+1, out, res)
            out.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        out = []
        self.backtrack(n, 0, 0, out, res)
        return res
        