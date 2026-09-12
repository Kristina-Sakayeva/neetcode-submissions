class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
            
        for num, count in counts.items():
            freq[count].append(num)
        
        top_k = []
        for i in freq[len(freq) - 1::-1]:
            for n in i:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k


        