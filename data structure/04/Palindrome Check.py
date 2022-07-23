class Deque:
    def __init__(self, s):
        self.items = list(s)

    def append(self, c):
        self.items.append(c)

    def appendleft(self, c):
        self.temp = self.items
        self.items = list(c) + self.temp

    def pop(self):
        return self.items.pop()

    def popleft(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def right(self):
        return self.items[-1]

    def left(self):
        return self.items[0]


def check_palindrome(word):
    dq = Deque(word)

    while len(dq) > 1:
        # 맨 앞과 뒤를 꺼내서 다르다면 False
        if dq.popleft() != dq.pop():
            return False

    return True

word = input()
print(check_palindrome(word))
