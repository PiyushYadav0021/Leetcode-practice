class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        result = 0
        stack = [(root, 0)]

        while stack:
            node, total = stack.pop()

            total = (total << 1) | node.val
            if node.left is None and node.right is None:
                result += total
            else:
                if node.right:
                    stack.append((node.right, total))

                if node.left:
                    stack.append((node.left, total))

        return result
