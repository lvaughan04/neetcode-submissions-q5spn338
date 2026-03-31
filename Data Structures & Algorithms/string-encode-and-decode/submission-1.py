class Solution:

    def encode(self, strs: List[str]) -> str:
        line = ""
        for word in strs:
            length = len(word)
            line += str(length) + "#" + word
        return line

    def decode(self, s: str) -> List[str]:
        line = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            right += 1
            word = s[right:right + length]
            left = right + length
            line.append(word)
        return line