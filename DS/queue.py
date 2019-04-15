#!/usr/bin/python

class LinkedQueue:
    # FIFO - 

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element  = element
            self._next  = next


    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise "Queue is empty"
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise "Queue is empty"
        val = self._head._element
        self._size -= 1
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
        return val

    def enqueue(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            self._head = newnode
#            print "IF in enqueue - %d\n" %e
        else:
            self._tail._next = newnode
#            print "ELSE in enqueue - %d\n" %e
        self._tail = newnode
        self._size += 1

    def __str__(self):
        cur = self._head
        print "Queue: ",
        while cur :
            print "%d -> " % cur._element,
            cur = cur._next
        print "\n"
        return ""


class ArrayQueue(object):

    _QUEUE_SZ = 10

    def __init__(self):
        self._queueData = [-1] * ArrayQueue._QUEUE_SZ
        self._head = 0
        self._tail = 0

    def __str__(self):
        i = self._head
        while i < self._tail:
            print "%d -> " %self._queueData[i] ,
            i += 1
        print "\n"
        return ""

    def enqueue(self, e):
        if self._tail == ArrayQueue._QUEUE_SZ:
            raise "Queue is full"
        self._queueData[self._tail] = e
        self._tail += 1

    def dequeue(self):
        if self._tail == 0:
            raise "Queue is empty"
        if self._head == ArrayQueue._QUEUE_SZ:
            self._head = 0
        val = self._queueData[self._head]
        self._queueData[self._head] = -1
        self._head += 1
        return val


if __name__ == '__main__':
    lq = LinkedQueue()
    lq.enqueue(10)
    lq.enqueue(30)
    lq.enqueue(20)
    lq.enqueue(70)
    lq.enqueue(80)
    str(lq)
    print "dequeue: %d\n" % lq.dequeue()
    print "dequeue: %d\n" % lq.dequeue()


    print "Array based:"
    aq = ArrayQueue()
    aq.enqueue(100)
    aq.enqueue(200)
    aq.enqueue(300)
    str(aq)
    print "\ndequeue: %d\n" % aq.dequeue()
    str(aq)
    aq.enqueue(400)
    aq.enqueue(500)
    str(aq)

