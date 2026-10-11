class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for i in range(len(temperatures))]

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_index, prev_temp = stack.pop()
                output[prev_index] = index - prev_index
            stack.append((index, temp))
        
        return output
        