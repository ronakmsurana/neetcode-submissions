import heapq



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = [i for i in nums[:k]]
        heapq.heapify_max(heap)
        to_del = {}
        if k==len(nums):
            return [heap[0]]
        for i in range(k,len(nums)):
            first = nums[i-k]
            cmax = heap[0]
            if cmax == first:
                heapq.heappop_max(heap)
            else: 
                while to_del.get(heap[0],0) > 0:
                    to_del[heapq.heappop_max(heap)] -=1
                cmax = heap[0]
                to_del[first] = to_del.setdefault(first,0) + 1
            ans.append(cmax)
            heapq.heappush_max(heap,nums[i])
        while to_del.get(heap[0],0) > 0:
            to_del[heapq.heappop_max(heap)] -= 1
        ans.append(heap[0])
        return ans
            
