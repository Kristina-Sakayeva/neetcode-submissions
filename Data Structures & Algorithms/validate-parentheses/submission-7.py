class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keys = {'(': ')',
        '{':'}',
        '[':']'}
        for letter in s:
            if letter in keys:
                stack.append(letter)
            else:
                if not stack:
                    return False
                if keys[stack.pop()] != letter:
                    return False
        if stack:
            return False
        return True
        