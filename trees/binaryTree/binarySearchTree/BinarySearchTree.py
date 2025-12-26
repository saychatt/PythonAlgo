from collections import deque


from trees.binaryTree.binarySearchTree.BSTNode import BSTNode


class BinarySearchTree(object):
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, root, value):
        if not root:
            return BSTNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        return root

    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root


    def remove(self, root, value):
        if not root:
            return None
        if value > root.value:
            root.right = self.remove(root.right, value)
        if value < root.value:
            root.left = self.remove(root.left, value)
        else: #if the value is equal
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else: #if both the child is present find the min from the right node and replace with root
                minNode = self.findMin(root.right)
                root.value = minNode.value
                root.right = self.remove(root.right, minNode.value)
        return root

    def search(self, root:BSTNode, value):
        if not root:
            return False
        if value == root.value:
            return True
        if value < root.value:
            return self.search(root.left, value)
        elif value > root.value:
            return self.search(root.right, value)

    def findKthSmallest(self, root, k):
        stack = []
        n = 0
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            n += 1
            if n == k:
                return current
            current = current.right

    def bfs(self, root):
        result = {}
        queue = deque()

        if root:
            queue.append(root)
        level = 0
        while len(queue) > 0:
            levelStart = True
            for i in range(len(queue)):
                curr = queue.popleft()
                # operation to put the key = level
                if levelStart:
                    result[level] = []
                    levelStart = False
                result[level].append(curr.value)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        return result

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        # If both values are less than root, LCA must be in left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both values are greater than root, LCA must be in right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If one value is less and other is greater, or one equals root,
        # then current node is LCA
        return root

    # Diameter of a binary tree:
    # https://neetcode.io/problems/binary-tree-diameter?list=neetcode150
    def diameterOfBinaryTree(self, root):
       result = 0

       def dfs(curr):
           if not curr:
               return 0
           left = dfs(curr.left)
           right = dfs(curr.right)
           nonlocal result
           result = max(result, left + right)
           return 1 + max(left, right)

       dfs(root)
       return result

    #serialize and de-serialize a tree
    #https://neetcode.io/problems/serialize-and-deserialize-binary-tree?list=neetcode150
    # def serialize(self, root) -> str:
        #res = []

        #return ",".join(res)

    #def deserialize(self, str) -> BSTNode:

