#1021
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        s=0
        l=len(S)
        ans=""
        for i in range(l):
            if S[i]=='(':
                s+=1
                if s==1:
                    continue
            elif S[i]==')':
                s-=1
                if s==0:
                    continue
            ans+=S[i]
        return ans

#1441
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l=len(target)
        a=1
        ans=[]
        for i in range(l):
            while target[i]>a:
                ans.extend(['Push','Pop'])
                a+=1
            ans.append('Push')
            a+=1
        return ans

#456
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s,s1,su=[],None,None
        for i in nums[::-1]:
            if su is not None and s1 is not None and s1>i:
                return True
            while len(s)>0 and i>s[-1]:
                s1=s.pop()
            s.append(i)
            if s1 is not None and (su is None or i>su):
                su=i
        return False

#636
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        a=[]
        l=len(logs)
        for i in range(l):
            sp=logs[i].split(":")
            if sp[1]=="start":
                a.append([int(sp[2]),"s",int(sp[0])])
            else:
                a.append([int(sp[2])+1,"e",int(sp[0])])
        a=sorted(a,key=lambda s:s[0])
        s=[]
        ans=[0]*n
        last=None
        for i in range(l):
            if a[i][1]=="s":
                if last is not None and len(s)>0:
                    ans[s[-1][1]]+=a[i][0]-last
                last=a[i][0]
                s.append([a[i][0],a[i][2]])
            else:
                x=s.pop()
                ans[x[1]]+=a[i][0]-last
                last=a[i][0]
        return ans

#735
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        l=len(asteroids)
        for i in range(l):
            while ans!=[] and ans[-1]>0 and asteroids[i]<0 and ans[-1]<-asteroids[i]:
                ans.pop()
            if ans!=[] and ans[-1]>0 and asteroids[i]<0:
                if ans[-1]>-asteroids[i]:
                    continue
                if ans[-1]==-asteroids[i]:
                    ans.pop()
                    continue
        
            else:
                ans.append(asteroids[i])

    return ans

#880
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        l=len(S)
        a=[0]*l
        target=0
        for i in range(l):
            if S[i].isdigit():
                a[i]=a[i-1]*int(S[i])
            else:
                a[i]=a[i-1]+1
            if a[i]>=K:
                target=i
                break
        for i in range(target,-1,-1):
            if not S[i].isdigit():
                if a[i]==K:
                    return S[i]
                continue
            K=K%a[i-1]
            if K==0:
                K=a[i-1]


#85
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        a=matrix
        ans=0
        if len(a)==0 or len(a[0])==0:
            return 0
        n=len(a)
        m=len(a[0])
        d=[0]*m
        left=[0]*m
        for i in range(n):
            for j in range(m):
                if a[i][j]=="1":
                    d[j]+=1
                else:
                    d[j]=0
            s=[]
            for j in range(m):
                while s!=[] and d[j]<=s[-1][0]:
                    s.pop()
                if s==[]:
                    left[j]=0
                else:
                    left[j]=s[-1][1]+1
                s.append([d[j],j])
            s=[]
            for j in range(m-1,-1,-1):
                while s!=[] and d[j]<=s[-1][0]:
                    s.pop()
                if s==[]:
                    right=m-1
                else:
                    right=s[-1][1]-1
                ans=max(ans,d[j]*(right-left[j]+1))
                s.append([d[j],j])
        
    return ans

#726
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        a=formula
        l=len(formula)
        s=[{}]
        i=0
        def down():
            d=s[-1]
            s.pop()
            for k,v in d.items():
                if k in s[-1]:
                    s[-1][k]+=v
                else:
                    s[-1][k]=v
        def ev(i):
            num=0
            while i<l and a[i].isdigit():
                num=num*10+int(a[i])
                i+=1
            return num
        while i<l:
            if a[i]=='(':
                s.append({})
            elif a[i]==')':
                num=ev(i+1)
                if num!=0:
                    d=s[-1]
                    nd={}
                    for k,v in d.items():
                        nd[k]=v*num
                    s[-1]=nd
                    while i+1<l and a[i+1].isdigit():
                        i+=1
                down()
            else:
                s.append({})
                if i+1<l and a[i+1].islower():
                    e=a[i:i+2]
                    i+=2
                else:
                    e=a[i]
                    i+=1
                num=ev(i)
                if num!=0:
                    while i+1<l and a[i+1].isdigit():
                        i+=1
                else:
                    num=1
                    i-=1
                s[-1][e]=num
                down()
            i+=1
        d=s[-1]
        ans=[]
        for k,v in d.items():
            if v>1:
                v=str(v)
            else:
                v=""
            ans.append([k,v])
        ans=sorted(ans,key=lambda x:x[0])
        ret=""
        for i in ans:
            ret+=i[0]+i[1]
        return ret

