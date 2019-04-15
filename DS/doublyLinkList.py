#!/usr/bin/python


class DoublyLinkedBase(object):

    class _Node(object):
        """ Non public class for book keeping work
        """

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        # Sentinels (Guards) of lists
        self._header = self._Node(0, None, None)
        self._tailer = self._Node(0, None, None)
        self._size = 0

        self._header._next = self._tailer
        self._tailer._prev = self._header

    def __len__(self):
        return self._size

    def is_empty():
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newnode = self._Node(e, predecessor, successor)
        predecessor._next = newnode
        newnode._next = successor
        successor._prev = newnode
        self._size += 1
        reurn newnode

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successort._prev = predecessor
        self._size -= 1


class LinkedDeque(DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise "LinkedDeque is empty"
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise "LinkedDeque is empty"
        return self._tail._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._tailer._prev, self._tailer)

    def delete_first(self):
        if self.is_empty():
            raise "LinkedDeque is empty"
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise "LinkedDeque is empty"
        self._delete_node(self._tailer._prev)
