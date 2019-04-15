#!/usr/bin/python



class Tree:

    class _Node:

        def __init__(self, element):
            self._element = element
            self._left = None
            self._right = None

    def is_root(self, node):
        raise NotImplementedError("must implement is_root")

    def parent(self, node):
        raise NotImplementedError("must implement parent")

    def depth(self, node):
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))

