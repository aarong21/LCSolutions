class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        import heapq
        num = len(score)
        counter = 1
        heap = []
        answer = [None] * num
        for i in range(num):
            heapq.heappush(heap, (-1*score[i], i))
        heapq.heapify(heap)

        print(heap)
        for _ in range(num):
            term = heapq.heappop(heap)
            Score = term[0] * -1
            ind = term[1]
            if counter == 1:
                answer[ind] = "Gold Medal"
            elif counter == 2:
                answer[ind] = "Silver Medal"
            elif counter == 3:
                answer[ind] = "Bronze Medal"
            else:
                answer[ind] = str(counter)
            counter += 1
        return answer
