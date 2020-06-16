#58
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        if len(s)==0:
            return 0
        return len(s[-1])

#415
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1=len(num1)
        len2=len(num2)
        if len1<len2:
            len1,len2=len2,len1
            num1,num2=num2,num1
        num2='0'*(len1-len2)+num2
        res=""
        plus=0
        for i in range(len1-1,-1,-1):
            s=int(num1[i])+int(num2[i])+plus
            if s>=10:
                s-=10
                plus=1
            else:
                plus=0
            res+=str(s)
        if plus==1:
            res+='1'
        return res[::-1]

#521
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        len1=len(a)
        len2=len(b)
        if len1>len2:
            return len1
        if len2>len1:
            return len2
        if a==b:
            return -1
        return len1

#709
class Solution:
    def toLowerCase(self, str: str) -> str:
        l=len(str)
        str=list(str)
        for i in range(l):
            o=ord(str[i])
            if o>=65 and o<=90:
                str[i]=chr(o+32)
        
    return "".join(str)

#917
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l=len(S)
        s=list(S)
        log=[]
        for i in range(l):
            if ord(s[i])>=65 and ord(s[i])<=90 or ord(s[i])>=97 and ord(s[i])<=122:
                log.append(s[i])
        cnt=1
        for i in range(l):
            if ord(s[i])>=65 and ord(s[i])<=90 or ord(s[i])>=97 and ord(s[i])<=122:
                s[i]=log[-cnt]
                cnt+=1
        return "".join(s)

#468
class Solution:
    def checkint(self,n:str):
        for i in n:
            if ord(i)<48 or ord(i)>57:
                return False
        if len(n)<1 or len(n)>3:
            return False
        if len(n)>1 and n[0]=='0':
            return False
        return True
    
    def check4(self,n: str) -> bool:
        if self.checkint(n)==False:
            return False
        n=int(n)
        if n>=0 and n<=255:
            return True
        return False
    def validIPAddress(self, IP: str) -> str:
        s=IP.split('.')
        if len(s)>0:
            if len(s)==4 and self.check4(s[0]) and self.check4(s[1]) and self.check4(s[2]) and self.check4(s[3]):
                return "IPv4"
        s=IP.split(':')
        if len(s)>0:
            if len(s)==8:
                for i in s:
                    if len(i)<=0 or len(i)>4:
                        return "Neither"
                    l=len(i)
                    for j in range(l):
                        if not(ord(i[j])>=48 and ord(i[j])<=57) and not(ord(i[j])>=65 and ord(i[j])<=70) and not(ord(i[j])>=97 and ord(i[j])<=102):
                            return "Neither"
                return "IPv6"
        return "Neither"

#1233
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder=sorted(folder)
        ret=[folder[0]]
        father=folder[0]
        flen=len(father)
        for i in range(1,len(folder)):
            l=len(folder[i])
            if flen>l or (flen==l and father!=folder[i]) or (not (folder[i]==father+folder[i][flen:] and folder[i][flen]=='/')):
                ret.append(folder[i])
                father=folder[i]
                flen=len(father)
        return ret

