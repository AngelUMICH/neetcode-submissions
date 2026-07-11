class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        for char in s:
            chars[char] = 0
        res = 0
        l = 0

        for r in range(len(s)):
            chars[s[r]] += 1
            maxf_key = max(chars, key=chars.get)
            maxf = chars[maxf_key]
            winsize = r-l+1
            if (winsize-maxf <= k):
                res = max(res, winsize)
            else:
                chars[s[l]] -= 1
                l += 1

        return res
