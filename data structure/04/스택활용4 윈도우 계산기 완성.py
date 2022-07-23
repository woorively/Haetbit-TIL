from tkinter import Tk, Label, Button, Entry, StringVar
from functools import partial

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

        elif token == ' ':
            continue

        # 만약 피연산자이면,
        # token을 실수로 스택에 저장
        else:
            s.push(float(token))

    return s.pop()


def do_something():
    value = compute_postfix(infix_to_postfix(expr.get()))
    total.set("{0:.4f}".format(value))
    return

root = Tk()
root.title("My Calculator")
expr = StringVar()
title_label = Label(root, text="My Calcualtor").grid(row=0, columnspan=2)
input_exam = Label(root, text="Space between terms: ( 3 + 2 ) * 8").grid(row=1, columnspan=2)
exp_entry = Entry(root, textvariable=expr).grid(row=2, column=0)
total_label = Label(root, text="TOTAL").grid(row=3, column=0)
total = StringVar()
total.set('0')
value_label = Label(root, textvariable=total, width=20).grid(row=3, column=1)
equal_btn = Button(root, text=' = ', width=20, command=do_something).grid(row=2, column=1)
root.mainloop()
root.destroy()
