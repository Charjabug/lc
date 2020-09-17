#96
class Solution:
    def numTrees(self, n: int) -> int:
        ans=[0]*20
        ans[0]=1
        ans[1]=1
        ans[2]=2
        for i in range(3,20):
            for j in range(i):
                ans[i]+=ans[j]*ans[i-1-j]
        return ans[n]

#221
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        a=matrix
        n=len(a)
        if n==0:
            return 0
        m=len(a[0])
        if m==0:
            return 0
        ans=0
        for i in range(n):
            for j in range(m):
                if a[i][j]=='1':
                    if i==0 or j==0:
                        a[i][j]=1
                    else:
                        a[i][j]=min(a[i-1][j-1],a[i][j-1],a[i-1][j])+1
                    ans=max(ans,a[i][j]**2)
                else:
                    a[i][j]=0
        return ans

#357
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans=[0]*9
        ans[0]=1
        ans[1]=9
        for i in range(2,n+1):
            ans[i]=ans[i-1]*(11-i)
        for i in range(1,n+1):
            ans[i]=ans[i-1]+ans[i]
        return ans[n]

#413
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        a=A
        l=len(a)
        ans=[0]*l
        s=0
        for i in range(2,l):
            if a[i-1]<<1==a[i]+a[i-2]:
                ans[i]=ans[i-1]+1
                s+=ans[i]
        return s

#516
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l=len(s)
        ans=0
        b=s[::-1]
        a=s
        for i in range(l):
            f=[0]*l
            for j in range(l):
                if a[i]==b[j]:
                    if i==0 or j==0:
                        f[j]=1
                    else:
                        f[j]=f2[j-1]+1
                else:
                    if i-1>=0:
                        f[j]=f2[j]
                    if j-1>=0:
                        f[j]=max(f[j],f[j-1])
                        if i-1>=0:
                            f[j]=max(f[j],f2[j-1])
            f2=f
        return f[l-1]

#673
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        a=nums
        l=len(a)
        ansl=0
        ansc=0
        c=[1]*(l+1)
        f=[1]*(l+1)
        for i in range(l):
            for j in range(i):
                if a[i]>a[j]:
                    if c[j]+1>c[i]:
                        c[i]=c[j]+1
                        f[i]=f[j]
                    elif c[j]+1==c[i]:
                        f[i]+=f[j]
        for i in range(l):
            if c[i]>ansl:
                ansl=c[i]
                ansc=f[i]
            elif c[i]==ansl:
                ansc+=f[i]
        return ansc

#698
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        a=nums
        total=sum(a)
        if total//k*k!=total:
            return False
        t=total//k
        l=len(a)
        a=sorted(a)
        s=[0]*k
        ans=0
        def dfs(c):
            nonlocal ans
            if ans==1:
                return
            if len(c)==0:
                ans=1
                return
            for j in range(k):
                if j>0 and s[j]==s[j-1]:
                    continue
                if c[-1]+s[j]<=t:
                    s[j]+=c[-1]
                    dfs(c[:-1])
                    s[j]-=c[-1]
        dfs(a)
        return ans

