class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {
        }

        for word in strs:
            value = ''.join(sorted(word))
            
            if value in groups:
                groups[value].append(word)
            else:
                groups[value] = [word]
        return list(groups.values())