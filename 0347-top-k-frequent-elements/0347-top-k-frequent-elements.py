class Solution(object):
    import heapq
    def topKFrequent(self, nums, k):
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        heap = []
        for num , count in freq.items():
            heapq.heappush(heap,(count,num))

            if len(heap) > k:
                heapq.heappop(heap)
                
        result = []
        for count , num in heap:
            result.append(num)
        return result
