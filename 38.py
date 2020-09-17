#160
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1=0
        l2=0
        i=headA
        while i is not None:
            l1+=1
            i=i.next
        i=headB
        while i is not None:
            l2+=1
            i=i.next
        i=headA
        j=headB
        if l1>l2:
            for k in range(l1-l2):
                i=i.next
        else:
            for k in range(l2-l1):
                j=j.next
        while i is not None:
            if i==j:
                return i
            i=i.next
            j=j.next
        return None

#237
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
            :type node: ListNode
            :rtype: void Do not return anything, modify node in-place instead.
            """
        node.val=node.next.val
        node.next=node.next.next



#292
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4==0:
            return False
        return True

#54
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        a=matrix
        n=len(a)
        if n==0:
            return []
        m=len(a[0])
        if m==0:
            return []
        i,j=0,-1
        s=m*n
        while s:
            while j+1<m and a[i][j+1] is not None:
                j+=1
                ans.append(a[i][j])
                a[i][j]=None
                s-=1
            while s and i+1<n and a[i+1][j] is not None:
                i+=1
                ans.append(a[i][j])
                a[i][j]=None
                s-=1
            while s and j-1>=0 and a[i][j-1] is not None:
                j-=1
                ans.append(a[i][j])
                a[i][j]=None
                s-=1
            while s and i-1>=0 and a[i-1][j] is not None:
                i-=1
                ans.append(a[i][j])
                a[i][j]=None
                s-=1
        return ans

#77
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        import copy
        s=[]
        ans=[]
        def dfs(i):
            if len(s)==k:
                x=copy.deepcopy(s)
                ans.append(x)
                return
            if i>n:
                return
            s.append(i)
            dfs(i+1)
            s.pop()
            dfs(i+1)
        dfs(1)
        return ans

#82
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ret=ListNode(next=head)
        i=ret
        while i:
            if i.next and i.next.next and i.next.val==i.next.next.val:
                while i.next and i.next.next and i.next.val==i.next.next.val:
                    i.next.next=i.next.next.next
                i.next=i.next.next
            else:
                i=i.next
        return ret.next

#142
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        a,b=head,head
        ok=None
        while a and a.next:
            a=a.next.next
            b=b.next
            if a==b:
                ok=1
                break
        if not ok:
            return ok
        a,b=head,b
        while a and b:
            if a==b:
                return a
            a=a.next
            b=b.next

