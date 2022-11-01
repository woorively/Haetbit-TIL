# 나머지 코드
def splice(self, a, b, x):
    if a == None or b == None or x == None:
        return
    ap = a.prev
    bn = b.next

    ap.next = bn
    bn.next = ap

    xn = x.next
    xn.prev = b
    b.next = xn
    a.prev = x
    x.next = a


def moveAfter(self, a, x):
    self.splice(a, a, x)


def moveBefore(self, a, x):
    self.splice(a, a, x.prev)


def insertAfter(self, x, key):
    self.moveAfter(Node(key), x)


def insertBefore(self, x, key):
    self.moveBefore(Node(key), x)


def pushFront(self, key):
    self.insertAfter(self.head, key)


def pushBack(self, key):
    self.insertBefore(self.head, key)


def deleteNode(self, x):
    if x == None or x == self.head:
        return
    x.prev.next, x.next.prev = x.next, x.prev


def popFront(self):
    if self.isEmpty():
        return
    key = self.head.next.key
    self.deleteNode(self.head.next)
    return key


def popBack(self):
    if self.isEmpty():
        return
    key = self.head.prev.key
    self.deleteNode(self.head.prev)
    return key


def search(self, key):
    v = self.head
    while v.next != self.head:
        v = v.next
        if v.key == key:
            return v
    return


def first(self):
    if self.isEmpty():
        return
    return self.head.next


def last(self):
    if self.isEmpty():
        return
    return self.head.prev


def isEmpty(self):
    if self.head.next == None:
        return True
    return False


