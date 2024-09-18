class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # convert to string list
        lst = [*map(str,nums)]
        # compare current number to rest of numbers after
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                # if str of curr + next > next + curr
                # its in right order, else swap
                if lst[i]+lst[j] > lst[j]+lst[i]:
                    continue
                else:
                    lst[i], lst[j] = lst[j], lst[i]
        # put altogether into a string
        res = ''.join(lst)

        return str(int(res))