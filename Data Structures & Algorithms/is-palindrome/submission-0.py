class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum()).lower()

        for index, letter in enumerate(list(clean)):
            if letter != clean[len(clean) - 1 - index]:
                return False
        return True
        