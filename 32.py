#687
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans=0
        def calc(root):
            if not root:
                return 0
            left=right=ret=length=0
            if root.left:
                left=calc(root.left)
                if root.left.val==root.val:
                    ret=left+1
                    length=ret
            if root.right:
                right=calc(root.right)
                if root.right.val==root.val:
                    ret=max(ret,right+1)
                    length+=right+1
            nonlocal ans
            ans=max(ans,length)
            return ret
        
        calc(root)
        return ans

#938
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        s=0
        def dfs(i):
            if not i:
                return
            if i.val<L:
                dfs(i.right)
                return
            if i.val>R:
                dfs(i.left)
                return
            nonlocal s
            s+=i.val
            dfs(i.left)
            dfs(i.right)
        dfs(root)
        return s


#1137
class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c=1,0,0
        for i in range(n):
            a,b,c=b,c,a+b+c
        return c

#779
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1: return 0
        if K%2==1:
            return self.kthGrammar(N-1,(K+1)//2)
        else:
            return 1-self.kthGrammar(N-1,(K+1)//2)

#794
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def judge(a):
            for i in range(3):
                if a[i][0]!=' ' and a[i][0]==a[i][1] and a[i][0]==a[i][2]: return True
                if a[0][i]!=' ' and a[0][i]==a[1][i] and a[0][i]==a[2][i]: return True
                if a[0][0]!=' ' and a[0][0]==a[1][1] and a[0][0]==a[2][2]: return True
                if a[0][2]!=' ' and a[0][2]==a[1][1] and a[0][2]==a[2][0]: return True
                for i in range(3):
                    for j in range(3):
                        if a[i][j]==' ': return False
                return True
        def xia(a,hand):
            if a==board: return True
            if judge(a): return False
            for i in range(3):
                for j in range(3):
                    if a[i][j]==' ' and ((board[i][j]=='X' and hand==0)or(board[i][j]=='O' and hand==1)):
                        a[i]=a[i][:j]+board[i][j]+a[i][j+1:]
                        if xia(a,1-hand): return True
                        a[i]=a[i][:j]+' '+a[i][j+1:]
            return False
        a=["   ","   ","   "]
        return xia(a,0)

#894
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N%2==0:
            return []
        ans=[[] for i in range(N+1)]
        ans[1]=[TreeNode()]
        for i in range(3,N+1,2):
            for j in range(1,N-1,2):
                k=i-j-1
                print(j,k)
                for l in ans[j]:
                    for m in ans[k]:
                        ans[i].append(TreeNode(left=l,right=m))
        return ans[N]

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

