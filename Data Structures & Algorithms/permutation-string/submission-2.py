class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref = {}
        sub = {}
        # create default dict with 0
        for char in s1:
            ref[char] = 0
        for char in s2:
            sub[char] = 0
        #preprocess
        for char in s1:
            ref[char] += 1
        
        l = 0
        match = False
        for r in range(len(s2)):
            sub[s2[r]] +=1
            if (r >= len(s1)):
                sub[s2[l]] -= 1
                l += 1
            match = all(sub.get(k) == v for k, v in ref.items())
            print(sub, ref)
            if match:
                return True
        return False
            
            