class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        lst = []
        # for num in nums:
        #     lst += [str(num)]
            
        lst = [*map(str,nums)]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if str(lst[i]) + str(lst[j]) > str(lst[j]) + str(lst[i]):
                    continue
                else:
                    lst[i], lst[j] = lst[j], lst[i]
        res = ''.join(lst)

        return str(int(res))

        '''
        Using a custom comparator:
        lst.sort(key=lambda x:x[0]+x[-1],reverse=True)

        Stripping 0's from ans instead of casting twice
        ''.join(lst).lstrip('0') or '0'
        3 30 34 5 9
        "9"
        
        '''