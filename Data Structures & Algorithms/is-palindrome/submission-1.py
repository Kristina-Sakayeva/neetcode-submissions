class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = list(s)
        opposite_index = len(s) - 1

        for index, letter in enumerate(s):
            if not letter.isalnum():
                continue

            opposite = s[opposite_index]
            while not opposite.isalnum():
                opposite_index -= 1
                opposite = s[opposite_index]

            if letter.lower() != opposite.lower():
                return False
            
            opposite_index -= 1
        return True
        