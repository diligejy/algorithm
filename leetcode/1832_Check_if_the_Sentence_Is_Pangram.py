class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphaList = [chr(c) for c in range(ord('a'), ord('z')+1)]
        return len(list(set(sentence))) == len(alphaList)
