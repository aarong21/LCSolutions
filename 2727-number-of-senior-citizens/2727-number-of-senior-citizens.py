class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # idx 11,12
        num = 0
        for i in range(len(details)):
            year = int(str(details[i][11])+str(details[i][12]))
            print(year)
            if year > 60:
                num += 1
        return num