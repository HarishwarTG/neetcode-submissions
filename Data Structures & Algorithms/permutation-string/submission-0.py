class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        
        if n > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(n):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        if count1 == count2:
            return True
        
        for i in range(n, len(s2)):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - n]) - ord('a')] -= 1

            if count1 == count2:
                return True

        return False 
        
