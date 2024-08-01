class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        blocked = defaultdict(set)
        # Iterate over all reserved sears, saving blocked pos
        for row, col in reservedSeats:
            if col in [2,3,4,5]:
                blocked[row].add('left')
            if col in [4,5,6,7]:
                blocked[row].add('middle')
            if col in [6,7,8,9]:
                blocked[row].add('right')
        
        # total will holf # of 4-p seats avail
        # initialize with 2 per row w/o blocked seats
        num_empty = n - len(blocked)
        total = 2 * num_empty

        # for each row w/ blocked sections, add avail seats
        for blocked_section in blocked.values():
            num_blocked = len(blocked_section)
            if num_blocked == 1: total += 1
            elif num_blocked == 2: total += 1
            # total += (3 - num_blocked)
        return total