# Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок.
# Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий,
# и пары скобок правильно вложены друг в друга. Сбалансированными последовательности будут следующие скобки:
# (((([{}]))))
# [([])((([[[]]])))]{()}
# {{[()]}}
# Несбалансированными последовательности:
# }{}
# {{[(])]}}
# [[{())}]


class Stack:
    def __init__(self, stack):
        self.stack = stack

    def isEmpty(self):
        if len(self.stack) != 0:
            return True
        else:
            return False

    def push(self,new_element):
        self.stack = self.stack + new_element

    def pop(self):
        self.stack = self.stack[:-1]
        return self.stack[-1]

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def check_balanse(Stack):
    if Stack.isEmpty() == False or (Stack.size() % 2) != 0:
        return "Небалансированно"
    else:

        return 'Сбалансированно'


new = Stack('(((([{}]))))')
print(check_balanse(new))

