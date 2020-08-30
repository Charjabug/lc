#14
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=len(strs)
        ans=0
        if l==0:
            return ""
        ml=len(strs[0])
        for i in range(l):
            ml=min(ml,len(strs[i]))
        for i in range(ml):
            ok=1
            for j in range(l):
                if strs[j][ans]!=strs[0][ans]:
                    ok=0
                    break
            if ok==1:
                ans+=1
        return strs[0][:ans]

#155
class MinStack:
    
    def __init__(self):
        """
            initialize your data structure here.
            """
        self.s=[]
        self.ms=[]
    
    def push(self, x: int) -> None:
        self.s.append(x)
        if self.ms==[] or self.ms[-1][0]>=x:
            self.ms.append([x,len(self.s)-1])

def pop(self) -> None:
    self.s.pop()
    if self.ms!=[] and self.ms[-1][1]==len(self.s):
        self.ms.pop()
    
    def top(self) -> int:
        return self.s[-1]
    
    def getMin(self) -> int:
        return self.ms[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last=None
        now=head
        while now:
            nxt=now.next
            now.next=last
            last=now
            now=nxt
        return last

#146
from collections import deque
class LRUCache:
    
    def __init__(self, capacity: int):
        self.d={}
        self.data=[0]*capacity
        self.usage=[0]*capacity
        self.q=deque()
        self.cnt=0
        self.keys=[0]*capacity
        for i in range(capacity):
            self.cnt+=1
            self.usage[i]=self.cnt
            self.q.append((i,self.cnt))
            self.keys[i]=-self.cnt
            self.d[-self.cnt]=i
    def get(self, key: int) -> int:
        if key in self.d:
            self.cnt+=1
            self.usage[self.d[key]]=self.cnt
            self.q.append((self.d[key],self.cnt))
            return self.data[self.d[key]]
        else:
            return -1

def put(self, key: int, value: int) -> None:
    
    d,data,usage,q,keys=self.d,self.data,self.usage,self.q,self.keys
        if key in d:
            i=d[key]
            data[i]=value
            self.cnt+=1
            usage[i]=self.cnt
            q.append((i,self.cnt))
            return
    while usage[q[0][0]]!=q[0][1]:
        q.popleft()
        i=q.popleft()[0]
        del(d[keys[i]])
        d[key]=i
        data[i]=value
        self.cnt+=1
        usage[i]=self.cnt
        q.append((i,self.cnt))
        keys[i]=key


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#199
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans=[]
        def dfs(i,d):
            if not i:
                return
            if len(ans)<d+1:
                ans.append(i.val)
            else:
                ans[d]=i.val
            dfs(i.left,d+1)
            dfs(i.right,d+1)
        dfs(root,0)
        return ans

#491
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        l=len(nums)
        for i in range(l):
            nans=set()
            for j in ans:
                s=j.split(".")
                if nums[i]>=int(s[-1]):
                    s.append(str(nums[i]))
                    nans.add(".".join(s))
            nans.add(str(nums[i]))
            ans=ans.union(nans)
        ret=[]
        for i in ans:
            s=i.split(".")
            if len(s)>1:
                ret.append(s)
        return ret

#714
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l=len(prices)
        d0,d1,nd0,nd1=0,0,0,0
        if l==0:
            return 0
        d1=-fee-prices[0]
        for i in range(1,l):
            nd0=max(d0,d1+prices[i])
            nd1=max(d1,d0-prices[i]-fee)
            d0,d1=nd0,nd1
        return d0

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
