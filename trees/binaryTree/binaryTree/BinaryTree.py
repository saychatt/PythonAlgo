from trees.binaryTree.binaryTree.BTNode import BTNode


class BinaryTree:
    def __init__(self, value):
        self.root = BTNode(value)

    def lowestCommonAncestor(self, root, p, q):
        return self.lCAPreOrder(root, p, q, False, False)

    def lCAPreOrder(self, node, p, q, p_flag, q_flag):
        if node is None:
            return None
        if p_flag and q_flag:
            self.findLCA(p, q)
        if node.val == p.val:
            p_flag = True
        if node.val == q.val:
            q_flag = True
        self.lCAPreOrder(node.left, p, q, p_flag, q_flag)
        self.lCAPreOrder(node.right, p, q, p_flag, q_flag)

    def findLCA(self, p, q):
        ancestor_set = set()
        while p:
            ancestor_set.add(p.value)
            p = p.parent
        while q:
            if q.val in ancestor_set:
                return q
            q = q.parent