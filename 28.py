#392
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1=len(s)
        l2=len(t)
        if l1==0:
            return True
        a=0
        for i in range(l2):
            if t[i]==s[a]:
                a+=1
            if a==l1:
                return True
        return False

#746
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        p1=p2=0
        for i in range(l):
            p1,p2=min(p1,p2)+cost[i],p1
        return min(p1,p2)

#1025
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N%2==0

#1025
class Solution:
    def divisorGame(self, N: int) -> bool:
        a=[0]*1001
        a[1]=0
        a[2]=1
        a[3]=0
        for i in range(4,N+1):
            for j in range(1,i):
                if i%j==0 and a[i-j]==0:
                    a[i]=1
        return a[N]

#1139
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        import copy
        ans=0
        h=copy.deepcopy(grid)
        s=copy.deepcopy(grid)
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans=max(ans,1)
                    if j==0:
                        h[i][j]=1
                    if i==0:
                        s[i][j]=1
                    if j>0:
                        h[i][j]=h[i][j-1]+1
                    if i>0:
                        s[i][j]=s[i-1][j]+1
                for k in range(1,min(i,j)+1):
                    if h[i][j]>=k+1 and s[i][j]>=k+1:
                        if h[i-k][j]>=k+1 and s[i][j-k]>=k+1:
                            ans=max(ans,k+1)
                    else:
                        break
        return ans*ans

#740
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums=sorted(nums)
        nums=Counter(nums)
        a=list(nums.keys())
        b=list(nums.values())
        print(a)
        l=len(a)
        p1=p2=0
        for i in range(l):
            if i>0 and a[i]-a[i-1]==1:
                p1,p2=p2+a[i]*b[i],max(p1,p2)
            else:
                p1,p2=max(p1,p2)+a[i]*b[i],max(p1,p2)
        return max(p1,p2)

#523
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k<0:
            k=-k
        l=len(nums)
        if l<2:
            return False
        for i in range(1,l):
            if nums[i]==nums[i-1] and nums[i]==0:
                return True
        if k==0:
            return False
        for i in range(1,l):
            nums[i]=nums[i]%k
        for i in range(1,l):
            if (nums[i]+nums[i-1])%k==0:
                return True
        b=[]
        for i in range(l):
            if nums[i]!=0:
                b.append(nums[i])
        nums=b
        l=len(nums)
        s=0
        d={}
        for i in range(l):
            s=(s+nums[i])%k
            if s in d:
                d[s]=d[s]+1
            else:
                d[s]=1
if s%k==0:
    return True
        s=0
        for i in range(l):
            s=(s+nums[i])%k
            if d[s]==1:
                del(d[s])
            else:
                d[s]-=1
            if s in d:
                return True
    return False

#1320
class Solution:
    def minimumDistance(self, word: str) -> int:
        l=len(word)
        while l>2 and word[0]==word[1]:
            word=word[1:]
            l-=1
        if l<=2:
            return 0
        s={}
        for i in range(26):
            s[chr(i+65)]=i
        d=[[10 for i in range(27)]for j in range(27)]
        f=[[0 for i in range(6)]for j in range(6)]
        for i in range(6):
            f[i][0]=i*6
            for j in range(1,6):
                f[i][j]=f[i][0]+j
        for i in range(6):
            for j in range(6):
                for i2 in range(6):
                    for j2 in range(6):
                        if f[i][j]<26 and f[i2][j2]<26:
                            d[f[i][j]][f[i2][j2]]=abs(i-i2)+abs(j-j2)
        for i in range(26):
            d[i][26]=2900
            d[26][i]=0
        n=[]
        for i in range(l):
            n.append(s[word[i]])
        a=[[2800 for i in range(27)]for j in range(27)]
        a[26][26]=0
        for i in range(l):
            b=[[2800 for i in range(27)]for j in range(27)]
            for j in range(27):
                for k in range(27):
                    b[n[i]][j]=min(a[k][j]+d[k][n[i]],b[n[i]][j])
                    b[j][n[i]]=min(a[j][k]+d[k][n[i]],b[j][n[i]])
            a=b
        ans=2900
        for i in range(27):
            for j in range(27):
                if a[i][j]<ans:
                    ans=a[i][j]
        return ans
