# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = [root]
        nested_list = []
        if not root:
            return nested_list
        while queue:
            nested_list.append([i.val for i in queue])
            temp = queue
            queue = []
            for cur in temp:
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return nested_list
        