#914
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if a<b:
                a,b=b,a
            if a%b==0:
                return b
            return gcd(a%b,b)
        ans=-1
        cnt=[0]*10003
        for i in deck:
            cnt[i]+=1
        for i in range(10001):
            if cnt[i]>=1:
                if ans==-1:
                    ans=cnt[i]
                ans=gcd(cnt[i],ans)
        if ans<2:
            return False
        return True

#1128
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(i*(i-1)//2 for i in list(Counter(",".join(str(sorted(dominoes[i]))) for i in range(len(dominoes))).values()))

#846
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand=sorted(hand)
        counter=Counter(hand)
        p=list(counter.keys())
        c=list(counter.values())
        l=len(p)
        h=0
        s=sum(c)
        if s%W!=0:
            return False
        while s>0:
            if h+W-1>=l:
                return False
            mm=10001
            for i in range(h,h+W):
                if c[i]<=0 or p[i]!=p[h]+i-h:
                    return False
                if c[i]<mm:
                    mm=c[i]
            for i in range(h,h+W):
                c[i]-=mm
            s-=W*mm
            for i in range(h,l):
                if c[i]>0:
                    h=i
                    break
        return True

#870
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A=sorted(A)
        l=len(A)
        a=[-1]*l
        c=[-1]*l
        for i in range(l):
            B[i]=[B[i],i]
        B=sorted(B,key=lambda x:x[0])
        y=0
        for i in range(l):
            while y<l:
                if A[y]>B[i][0]:
                    a[i]=A[y]
                    A[y]=-1
                    break
                else:
                    y+=1
        for i in range(l):
            if a[i]>-1:
                c[B[i][1]]=a[i]
        a=c
        y=0
        for i in range(l):
            while a[i]==-1 and y<l:
                if A[y]>-1:
                    a[i]=A[y]
                    A[y]=-1
                else:
                    y+=1
    return a

#948
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        l=len(tokens)
        t=sorted(tokens)
        eat=l
        use=-1
        power=P
        point=0
        ans=0
        while use<eat-1:
            ok=0
            while use<eat-1 and power>=t[use+1]:
                use+=1
                power-=t[use]
                point+=1
                ok=1
            if point>ans:
                ans=point
            if use<eat-1 and point>0:
                eat-=1
                power+=t[eat]
                point-=1
                ok=1
            if ok==0:
                break
        return ans

#950
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        l=len(deck)
        a=[i for i in range(l)]
        nex=[i+1 for i in range(l)]
        s=l
        o=[]
        h=0
        t=l-1
        while s>0:
            o.append(h)
            s-=1
            if s==0:
                break
            h=nex[h]
            nex[t]=h
            t=h
            h=nex[h]
        print(o)
        p=ans=[0]*l
        deck=sorted(deck)
        for i in range(l):
            p[o[i]]=i
        for i in range(l):
            ans[i]=deck[p[i]]
        return ans

#1007
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a=[0]*7
        b=[0]*7
        ans=23333
        for i in range(len(A)):
            for j in range(1,7):
                if A[i]!=j and B[i]==j:
                    a[j]+=1
                if A[i]==j and B[i]!=j:
                    b[j]+=1
                if A[i]!=j and B[i]!=j:
                    b[j]=-23333
                    a[j]=-23333
        for i in range(1,7):
            if a[i]>=0 and a[i]<ans:
                ans=a[i]
            if b[i]>=0 and b[i]<ans:
                ans=b[i]
        if ans>20000:
            ans=-1
        
        return ans

#1423
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s=0
        l=len(cardPoints)
        k=l-k
        for i in range(k):
            s+=cardPoints[i]
        su=sum(cardPoints)
        ans=maxans=su-s
        for i in range(1,l-k+1):
            s-=cardPoints[i-1]
            s+=cardPoints[i-1+k]
            ans=su-s
            if ans>maxans:
                maxans=ans
        return maxans

