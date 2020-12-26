class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(i,j):
            x1,y1=divmod(i,6)
            x2,y2=divmod(j,6)
            return abs(x1-x2)+abs(y1-y2)

        inf=float("inf")
        dp=[0]*26
        for i in range(2,len(word)+1):
            new=[inf]*26
            cur=ord(word[i-1])-65
            pre=ord(word[i-2])-65
            for j in range(26):
                # 选择上一个手指
                new[j]=min(new[j], dp[j]+dist(pre,cur))
                # 选择另一个手指
                new[pre]=min(new[pre], dp[j]+dist(j,cur))
            dp=new
        return min(dp)

