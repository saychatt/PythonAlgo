class BSTNode(object):
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getLeftChild(self):
        return self.left

    def setRightChild(self, left):
        return self.right
