#offer39
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

#offer58I
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')[::-1]
        ans=""
        ok=0
        for i in s:
            if i=="":
                continue
            if ok==0:
                ok=1
                ans+=i
            else:
                ans+=" "+i
        return ans

#1114
class Foo:
    def __init__(self):
        self.a=0
        self.b=0
    
    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.a=1
    
    
    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while(self.a==0):
            time.sleep(0.0001)
        if self.a==1:
            printSecond()
        self.b=1
    
    
    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while(self.b==0):
            time.sleep(0.0001)
        if self.b==1:
            printThird()

#94
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s=[[root,0]]
        ans=[]
        while s!=[]:
            i=s.pop()
            if i[0] is None:
                continue
            if i[1]==1:
                ans.append(i[0].val)
                continue
            s.append([i[0].right,0])
            s.append([i[0],1])
            s.append([i[0].left,0])
        return ans

#133
"""
    # Definition for a Node.
    class Node:
    def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []
    """

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        d={}
        def dfs1(node):
            i=Node(val=node.val)
            d[i.val]=i
            for j in node.neighbors:
                if j.val not in d:
                    dfs1(j)
        dfs1(node)
        def dfs2(node):
            i=d[node.val]
            for j in node.neighbors:
                k=d[j.val]
                i.neighbors.append(k)
                if d[j.val].neighbors==[]:
                    dfs2(j)
        dfs2(node)
        return d[node.val]

#343
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        ans=1
        while n>=5:
            n-=3
            ans*=3
        ans*=n
        return ans

#765
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        l=len(row)
        ans=0
        for i in range(l):
            if row[i^1]==row[i]^1:
                continue
            nxt=row.index(row[i]^1)
            row[i^1],row[nxt]=row[nxt],row[i^1]
            ans+=1
        return ans
