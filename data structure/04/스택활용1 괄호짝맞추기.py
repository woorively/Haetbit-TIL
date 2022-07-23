class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()


# pseudo code
def parChecker(parSeq):
    s = Stack()
    for symbol in parSeq:
        if symbol == '(':
            s.push(symbol)

        # symbol = ')'
        else:
            # 스택이 비어 있는지 검사, 비어 있다면 false
            if not s.stack:
                return False
            else:
                # () 짝 맞추기
                s.pop()

    # 스택이 비어 있지 않다면 false
    if s.stack:
        return False
    return True


parSeq = input()
print(parChecker(parSeq))
