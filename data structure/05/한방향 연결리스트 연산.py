class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        while (v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:
            # 앞에서부터 탐색
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        if self.size == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key

    def popBack(self):
        # 빈 리스트인 경우
        if self.size == 0:
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            # 리스트에 노드가 하나만 있는 경우
            if prev == None:
                self.head = None
            # 리스트에 두 개 이상의 노드가 있는 경우
            else:
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key

    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return v

    def remove(self, x):
        if self.size == 0 or x == None:
            return False
        elif x == self.head:
            self.popFront()
        else:
            prev, tail = None, self.head
            while tail.next != x.next:
                prev = tail
                tail = tail.next
            prev.next = tail.next
            del tail
            self.size -= 1
        return True

    # def remove(self, x):
    #     if self.size == 0 or x == None:
    #         return False
    #     elif x == self.head:
    #         self.popFront()
    #         return True
    #     else:
    #         prev, tail = None, self.head
    #         while tail.next != None:
    #             prev = tail
    #             tail = tail.next
    #             if tail == x:
    #                 prev.next = tail.next
    #                 del tail
    #                 self.size -= 1
    #                 return True
    #     return False

    def size(self):
        return self.size
