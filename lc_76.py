import collections     
class Solution:

    def minWindow(self, s, t):
        if not (s and t): return ''
        c=collections.Counter(t)
        npos,l,best=len(c),0,(0,len(s))
        found=False
        for r in range(len(s)):
            if s[r] not in c: continue
            c[s[r]]-=1
            if c[s[r]]: continue
            npos-=1
            if npos: continue
            found=True
            while 0==npos:
                if s[l] in c:
                    c[s[l]]+=1
                    if c[s[l]]==1: npos+=1
                l+=1
            if r-l+1<best[1]-best[0]: best=(l-1,r)                
        return s[best[0]:best[1]+1] if found else ''


if __name__ == "__main__":
    obj = Solution()
    s = "wewewewewew"
    t = "wewewew"
    print(obj.minWindow(s, t))