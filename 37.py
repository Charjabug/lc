#543
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans=0
        def dfs(i):
            nonlocal ans
            left=right=0
            if i.left is not None:
                left=dfs(i.left)
            if i.right is not None:
                right=dfs(i.right)
            ans=max(ans,left+1,right+1,left+right+1)
            return max(1,left+1,right+1)
        dfs(root)
        return ans-1

#605
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        a=flowerbed
        l=len(a)
        if a[0]==0 and (l==1 or a[1]==0):
            a[0]=1
            n-=1
        for i in range(1,l-1):
            if n==0:
                return True
            if a[i]==0 and a[i-1]==0 and a[i+1]==0:
                a[i]=1
                n-=1
        if n==0:
            return True
        if a[l-1]==0 and (l==1 or a[l-2]==0):
            a[l-1]=1
            n-=1
        return n<=0

#703
import heapq
class KthLargest:
    
    def ad(self,val):
        a,k=self.a,self.k
        if len(a)<k:
            heapq.heappush(a,val)
        elif val>a[0]:
            heapq.heappop(a)
            heapq.heappush(a,val)

def __init__(self, k: int, nums: List[int]):
    self.a=[]
    self.k=k
        for i in nums:
            self.ad(i)

def add(self, val: int) -> int:
    self.ad(val)
    return self.a[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#852
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        t=len(A)
        l,r=0,t
        while l<r:
            m=(l+r)//2
            if A[m]>A[m+1]:
                r=m
            else:
                l=m+1
        return l

#39
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        import copy
        s=0
        ans=[]
        c=[]
        a=candidates
        l=len(a)
        def dfs(i):
            nonlocal s
            if i==l:
                if s==target:
                    cc=copy.deepcopy(c)
                    ans.append(cc)
                return
            dfs(i+1)
            if s+a[i]<=target:
                s+=a[i]
                c.append(a[i])
                dfs(i)
                s-=a[i]
                c.pop()
        dfs(0)
        return ans

#208
class Trie:
    
    def __init__(self):
        """
            Initialize your data structure here.
            """
        self.t={}
    
    
    def insert(self, word: str) -> None:
        """
            Inserts a word into the trie.
            """
        t=self.t
        for c in word:
            if c not in t:
                t[c]={}
            t=t[c]
        t["ex"]=True

def search(self, word: str) -> bool:
    """
        Returns if the word is in the trie.
        """
            t=self.t
                for c in word:
                    if c not in t:
                        return False
                            t=t[c]
                                if "ex" not in t:
                                    return False
                                        return True

def startsWith(self, prefix: str) -> bool:
    """
        Returns if there is any word in the trie that starts with the given prefix.
        """
            t=self.t
                for c in prefix:
                    if c not in t:
                        return False
                            t=t[c]
                                return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#785
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        c=[0]*101
        e=graph
        ans=1
        def dfs(i):
            nonlocal ans
            if ans==0:
                return
            for j in e[i]:
                if c[j]==c[i]:
                    ans=0
                    return
                if c[j]==0:
                    c[j]=3-c[i]
                    dfs(j)
        for i in range(101):
            if len(e)>=i+1 and c[i]==0:
                c[i]=1
                dfs(i)
        return ans


#25
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l=0
        i=head
        while i:
            i=i.next
            l+=1
        l=l//k
        last1=ListNode()
        ret=last1
        i=head
        for x in range(l):
            for y in range(k):
                j=i.next
                if y!=0:
                    i.next=last
                else:
                    last2=i
                last=i
                if y==k-1:
                    last1.next=i
                    last1=last2
                i=j
        last1.next=i
        return ret.next

