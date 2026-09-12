class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # counter = {}
        # highest = 0
        # for i in s:
        #     if i in counter:
        #         counter = {i: 1}
        #     else:
        #         counter[i] = 1
        #         if sum(counter.values()) > highest:
        #             highest = sum(counter.values())
        # return highest
        counter = []
        highest = 0
        for i in s:
            if i in counter:
                counter = counter[counter.index(i)+1:]
            counter.append(i)

            if len(counter) > highest:
                    highest = len(counter)
        return highest
        