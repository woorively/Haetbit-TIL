'''
Infix to postfix
'''
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


def infix_to_postfix(infix):
    # 연산자를 담을 스택
    opstack = Stack()

    # 후위표기 결과를 담을 리스트
    outstack = []
    token_list = infix.split()


    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)

        elif token == ')':
            # 스택에서 모두 다 꺼낼 때까지
            while not opstack.isEmpty():
                # 하나씩 꺼내서
                a = opstack.pop()
                # 만약 왼쪽 괄호라면 break,
                if a == '(':
                    break
                # 아니라면 outstack에 append
                else:
                    outstack.append(a)

        elif token in '+-/*^':
            # 연산자가 담긴 스택에 다른 연산자가 들어 있다면,
            while not opstack.isEmpty():
                # 일단 탑을 저장해서
                a = opstack.top()

                # 탑이 token보다 우선 순위가 높거나 같다면,
                # pop한 뒤 append
                if prec[token] <= prec[a]:
                    outstack.append(opstack.pop())
                # 아니라면, 반복문 종료 후 스택에 push
                else:
                    break
            opstack.push(token)

        # operand일 때
        # 그냥 리스트에 append
        else:
            outstack.append(token)


    # opstack에 남은 모든 연산자를 pop 후
    # outstack에 append
    while not opstack.isEmpty():
        outstack.append(opstack.pop())

    return " ".join(outstack)

infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)
