#!/usr/bin/python -tu

#import os

class ExpressionTree(object):

    class _Node(object):
        def __init__(self, value):
            self._value = value
            self._right = None
            self._left = None

    def __init__(self):
        self.postfixStack = []
        self.prefixStack = []
        self.infixStack = []

    def is_operator(self, value):
        if value == '+' or value == '-' or value == '*' or value == '/' or value == '^':
            return True
        else:
            return False

    def inOrderTraversal(self, tree):
        if tree is not None:
            self.inOrderTraversal(tree._right)
            print tree._value ,
            self.inOrderTraversal(tree._left)

    def preOrderTraversal(self, tree):
        if tree is not None:
            print tree._value ,
            self.preOrderTraversal(tree._right)
            self.preOrderTraversal(tree._left)

    def postOrderTraversal(self, tree):
        if tree is not None:
            self.postOrderTraversal(tree._right)
            self.postOrderTraversal(tree._left)
            print tree._value ,

    def constructPostFixTree(self, postfixtree):
        for ch in postfixtree:
            if not self.is_operator(ch):
                self.postfixStack.append(self._Node(ch))
            else:
                # operator
                t = self._Node(ch)
                leftValue = self.postfixStack.pop()
                rightValue = self.postfixStack.pop()
                t._left = leftValue
                t._right = rightValue
                self.postfixStack.append(t)
        root = self.postfixStack.pop()
        return root


if __name__ == '__main__':
    postFixExp = "ab+ef*g*-"
    expObj = ExpressionTree()
    root = expObj.constructPostFixTree(postFixExp)
    print "infix exp: " ,
    expObj.inOrderTraversal(root)
    print "\nprefix exp: " ,
    expObj.preOrderTraversal(root)
    print "\npostfix exp: " ,
    expObj.postOrderTraversal(root)
