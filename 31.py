#169
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=q=0
        for i in nums:
            if q==0:
                ans=i
                q=1
            elif ans==i:
                q+=1
            else:
                q-=1
        return ans

#461
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d=1
        ans=0
        for i in range(32):
            ans+=x//d%2!=y//d%2
            d*=2
            if x//d==0 and y//d==0: break
        return ans

#187
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l=len(s)
        if l<=10:
            return []
        en_dic={"A":0,"T":1,"C":2,"G":3}
        de_dic=["A","T","C","G"]
        def encode(c):
            a=0
            for i in range(10):
                a=a*4+en_dic[c[i]]
            return a
        def decode(a):
            c=""
            for i in range(10):
                c=de_dic[a%4]+c
                a=a//4
            return c
        
        a=encode(s[:10])
        b=1
        for i in range(9):
            b*=4
        d={a:1}
        for i in range(10,l):
            a=a%b*4+en_dic[s[i]]
            if a in d:
                d[a]=2
            else:
                d[a]=1
        ans=[]
        for i in d:
            if d[i]==2:
                ans.append(decode(i))
        return ans

#201
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==n:
            return m
        x=2147483648//2
        mm,nn=m,n
        while x>0:
            if m//x!=n//x:
                break
            m,n=m%x,n%x
            x>>=1
        ans=mm&nn&~(x-1)
        return ans

#1297
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l=len(s)
        d={}
        for i in range(l-minSize+1):
            c=s[i:i+minSize]
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        ans=0
        for k,v in d.items():
            if v>ans:
                lt=[0]*26
                for i in range(len(k)):
                    zm=ord(k[i])-97
                    lt[zm]+=1
                cnt=0
                for i in range(26):
                    if lt[i]>0:
                        cnt+=1
                if cnt<=maxLetters:
                    ans=v
        return ans


#1442
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans=0
        l=len(arr)
        for i in range(l):
            s=arr[i]
            for j in range(i+1,l):
                s=s^arr[j]
                if s==0:
                    ans+=j-i
        return ans

#1255
import copy
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if words==[]:
            return 0
        tl=copy.deepcopy(letters)
        s=0
        for i in words[0]:
            if i not in letters:
                return self.maxScoreWords(words[1:],tl,score)
            s+=score[ord(i)-97]
            letters.pop(letters.index(i))
        return max(s+self.maxScoreWords(words[1:],letters,score),self.maxScoreWords(words[1:],tl,score))

