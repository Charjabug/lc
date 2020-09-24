#226
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root

#404
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        s=0
        def dfs(i,l):
            if not i:
                return
            if not i.left and not i.right and l==1:
                nonlocal s
                s+=i.val
                return
            dfs(i.left,1)
            dfs(i.right,0)
        dfs(root,0)
        return s

#538
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        s=0
        def dfs(i):
            if not i:
                return
            nonlocal s
            dfs(i.right)
            s+=i.val
            i.val=s
            dfs(i.left)
        dfs(root)
        return root

#617
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(i,j):
            if not i and not j:
                return
            if i and j:
                i.val+=j.val
                i.left=dfs(i.left,j.left)
                i.right=dfs(i.right,j.right)
                return i
            elif i and not j:
                return i
            elif j and not i:
                return j
        t1=dfs(t1,t2)
        return t1

#637
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans=[]
        s=[]
        def dfs(i,d):
            if not i:
                return
            if len(ans)<d:
                ans.append(i.val)
                s.append(1)
            else:
                ans[d-1]+=i.val
                s[d-1]+=1
            dfs(i.left,d+1)
            dfs(i.right,d+1)
        dfs(root,1)
        ans=[ans[i]/s[i] for i in range(len(s))]
        return ans


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

#144
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        s=[root]
        ans=[]
        while s!=[]:
            i=s.pop()
            if i is None:
                continue
            ans.append(i.val)
            s.append(i.right)
            s.append(i.left)
        return ans

#145
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        s=[[root,0]]
        ans=[]
        while s!=[]:
            i=s.pop()
            if i[0] is None:
                continue
            if i[1]==1:
                ans.append(i[0].val)
                continue
            s.append([i[0],1])
            s.append([i[0].right,0])
            s.append([i[0].left,0])
        return ans

#987
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        s=[]
        def dfs(i,x,y):
            if not i:
                return
            s.append((i.val,x,y))
            dfs(i.left,x-1,y-1)
            dfs(i.right,x+1,y-1)
        dfs(root,0,0)
        s=sorted(s,key=lambda x:(x[1],-x[2],x[0]))
        ans=[]
        l=len(s)
        for i in range(l):
            if i==0 or s[i-1][1]!=s[i][1]:
                ans.append([s[i][0]])
            else:
                ans[-1].append(s[i][0])
        return ans

#968
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans=0
        def dfs(i):
            if not i:
                return
            i.c=0
            if not i.left and not i.right:
                return
            dfs(i.left)
            dfs(i.right)
            nonlocal ans
            if i.left and i.left.c==0 or i.right and i.right.c==0:
                ans+=1
                i.c=2
            elif i.left and i.left.c==2 or i.right and i.right.c==2:
                i.c=1
        dfs(root)
        if root.c==0:
            ans+=1
        return ans

