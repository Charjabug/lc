#1403
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s=sum(nums)
        x=0
        for i in range(len(nums)):
            x+=nums[i]
            if x>s-x:
                return nums[:i+1]


#1491
class Solution:
    def average(self, salary: List[int]) -> float:
        l=len(salary)
        a=sorted(salary)
        s=0
        p=0
        for i in range(1,l-1):
            s+=a[i]
            p+=1
        return s/p

#1502
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a=sorted(arr)
        l=len(a)
        if l<3:
            return True
        c=a[1]-a[0]
        for i in range(2,l):
            if a[i]-a[i-1]!=c:
                return False
        return True


#75
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
            Do not return anything, modify nums in-place instead.
            """
        a=[0]*3
        for i in nums:
            a[i]+=1
        for i in range(len(nums)):
            for j in range(3):
                if a[j]>0:
                    nums[i]=j
                    a[j]-=1
                    break
        return nums



#274
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        a=sorted(citations,reverse=True)
        h=0
        for i in a:
            if i>=h+1:
                h+=1
        return h




#324
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
            Do not return anything, modify nums in-place instead.
            """
        a=sorted(nums)
        l=len(a)
        for i in range(l):
            
            if i%2==0:
                nums[i]=a[(l+1)//2-i//2-1]
            else:
                nums[i]=a[l-i//2-1]
    return nums


#524
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans=None
        n=len(d)
        a=[0]*n
        l=[]
        for i in range(n):
            l.append(len(d[i]))
        for i in range(len(s)):
            for j in range(n):
                if a[j]<l[j] and s[i]==d[j][a[j]]:
                    a[j]+=1
        for i in range(n):
            if a[i]==l[i] and (ans is None or l[i]>=l[ans]):
                if ans is None or l[i]>l[ans] or d[i]<d[ans]:
                    ans=i
        if ans is None:
            return ""
        return d[ans]
