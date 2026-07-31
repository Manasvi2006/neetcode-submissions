class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackPairing = {'}':'{', ']':'[',')':'('}
        for p in s:
            if p in "[({":
                stack.append(p)
            elif stack and stack[-1] == stackPairing[p]:
                stack.pop()
            else:
                stack.append(p)

        return len(stack) == 0
        