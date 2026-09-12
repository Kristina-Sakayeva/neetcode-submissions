class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {
        }

        for word in strs:
            value = ''.join(sorted(word))
            
            if len(word) in groups:
                if value in groups[len(word)]:
                    groups[len(word)][value].append(word)
                
                else:
                    groups[len(word)][value] = [word]
            else:
                groups[len(word)] = {
                    value: [word]
                }
        full_list = []
        for string_len in groups.values():
            for group in string_len.values():

                full_list.append(group)

        return full_list