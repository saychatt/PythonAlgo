class BTNode:
    def __init__(self, value=0, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value

    def getLeftChild(self):
        return self.left
    def setLeftChild(self, left):
        self.left = left

    def getRightChild(self):
        return self.right
    def setRightChild(self, right):
        self.right = right

    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent
