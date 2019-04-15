#!/usr/bin/python

class CircularList(object):
    _LIST_MAX = 5

    class _Node(object):
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            newnode._next = newnode
        else:
            newnode._next = self._tail._next
            self._tail.next = newnode 

        self._tail = newnode
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise "Circular Queue is empty"
        oldnode = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = oldnode._next
        self._size -= 1
        return oldnode._element
            

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

    def __str__(self):
        if self.is_empty():
            print "Circular Queue is empty"
        else:
            cur = self._tail
            for _ in xrange(1, self._size):
                print "%d -> " % cur._element , 
                cur = cur._next
            print "\n"
        return ""

if __name__ == '__main__':
    cl = CircularList() 
    str(cl)
    cl.enqueue(100)
    cl.enqueue(200)
    cl.enqueue(300)
    cl.enqueue(400)
    cl.enqueue(500)
    str(cl)
    print "dequeue : %d \n" % cl.dequeue()
    cl.enqueue(300)
    cl.enqueue(400)
    cl.enqueue(500)
    str(cl)
