#!/usr/bin/python


class LinkedStack:
    # LIFO - stack implementation using single linked list


    class _Node:
        __slots__ = '_elememt', '_next' # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise 'Stack is empty'
        self._size -= 1
        val = self._head._element
        self._head = self._head._next
        return val

    def top(self):
        """ Return element from top of stack, but don't deletes it
        """

        if self.is_empty():
            raise 'stack is empty'
        return self._head._element

    def __str__(self):
        cur = self._head
        while cur:
            print "%d -> " %cur._element , 
            cur = cur._next
#        print "\n"
        # __str__ expect return type else will raise TypeError
        return ""


class ArrayStack(object):

    _ARRAY_SZ = 10

    def __init__(self):
        self._arrayStack = [0] * ArrayStack._ARRAY_SZ
        self._index = -1

    def push(self, e):
        if self._index == ArrayStack._ARRAY_SZ:
            print 'Array Stack is full'
        self._index += 1
        self._arrayStack[self._index] = e

    def pop(self):
        if self._index == -1:
            raise "Array stack is empty"
        e = self._arrayStack[self._index]
        self._index -= 1
        return e

    def __str__(self):
        if self._index == -1:
            print 'Array stack is empty'
        i = 0
        while i < self._index:
            print "%d->" %self._arrayStack[i], 
            i += 1
        return ""
            

if __name__ == '__main__':
    stack = LinkedStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    str(stack)
    print "poped : %d " %stack.pop()
    print "poped : %d " %stack.top()
    str(stack)

    print "\n\nArrayStack"

    arrStack = ArrayStack()
    arrStack.push(100)
    arrStack.push(200)
    arrStack.push(300)
    arrStack.push(400)
    arrStack.push(300)
    str(arrStack)
    print "poped : %d " %arrStack.pop()
    print "poped : %d " %arrStack.pop()
    str(arrStack)
