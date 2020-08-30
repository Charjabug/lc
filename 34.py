#08.03
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==i:
                return i
        return -1

#69
class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x+1
        while l<r-1:
            m=(l+r)//2
            if m*m>x:
                r=m-1
            else:
                l=m
        if r*r<=x:
            return r
        return l

#278
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
            :type n: int
            :rtype: int
            """
        l=1
        r=n
        while l<r:
            m=(l+r)//2
            if isBadVersion(m):
                r=m
            else:
                l=m+1
        return l

#374
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n+1
        while True:
            m=(l+r)//2
            g=guess(m)
            if g==0:
                return m
            if g==1:
                l=m+1
            else:
                r=m


#34
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[]:
            return [-1,-1]
        length=len(nums)
        l,r=0,length
        while l<r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            else:
                r=m
        if l==length or nums[l]!=target:
            return [-1,-1]
        ans=[l]
        l,r=0,length-1
        ans2=0
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                ans2=m
            if nums[m]>target:
                r=m-1
            else:
                l=m+1
        ans.append(ans2)
        return ans

#658
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        c=len(arr)
        l,r=0,c
        while l<r:
            m=(l+r)//2
            if arr[m]<x:
                l=m+1
            else:
                r=m
        if l>=c:
            return arr[-k:]
        if l>0 and abs(arr[l-1]-x)<=abs(arr[l]-x):
            l-=1
        r=l
        while r-l+1<k:
            if l==0:
                r+=1
                continue
            if r==c-1:
                l-=1
                continue
            if x-arr[l-1]<=arr[r+1]-x:
                l-=1
            else:
                r+=1
        return arr[l:r+1]

#4
class Solution:
    def findK(self,k:int, nums1: List[int], nums2: List[int]) -> float:
        l=k//2
        if len(nums1)<len(nums2):
            x=nums1
            nums1=nums2
            nums2=x
        if k==1:
            if len(nums2)==0 or nums1[0]<nums2[0]:
                return nums1[0]
            return nums2[0]
        if len(nums2)<l or nums1[l-1]<nums2[l-1]:
            return self.findK(k-l,nums1[l:],nums2)
        else:
            return self.findK(k-l,nums1,nums2[l:])
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2=len(nums1),len(nums2)
        return (self.findK((l1+l2+1)//2,nums1,nums2)+self.findK((l1+l2+2)//2,nums1,nums2))/2


