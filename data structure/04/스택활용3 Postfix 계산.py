class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def compute_postfix(postfix):
    s = Stack()

    for token in postfix:
        # 만약 연산자이면
        # 피연산자2, 피연산자1 순서대로 꺼내 계산한 뒤 push
        if token in '+-/*^':
            num2 = s.pop()
            num1 = s.pop()

            if token == '+':
                s.push(num1 + num2)
            elif token == '-':
                s.push(num1 - num2)
            elif token == '*':
                s.push(num1 * num2)
            elif token == '/':
                s.push(num1 / num2)
            else:
                s.push(num1 ^ num2)

        # 만약 피연산자이면,
        # token을 실수로 스택에 저장
        else:
            s.push(float(token))

    return s.pop()


postfix = input().split()
print(f'{compute_postfix(postfix):.4f}')
