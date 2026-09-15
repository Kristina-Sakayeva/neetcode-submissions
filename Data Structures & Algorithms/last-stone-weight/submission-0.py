class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        while len(stones) > 1:
            stones = sorted(stones)
            heavy_1 = stones.pop()
            heavy_2 = stones.pop()

            if heavy_1 == heavy_2:
                continue
            elif heavy_1 > heavy_2:
                stones.append(heavy_1-heavy_2)
                continue
            elif heavy_1 < heavy_2:
                stones.append(heavy_2-heavy_1)
                continue
        if stones:
            return stones[0]
        return 0