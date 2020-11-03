class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return self.list == []

    def push(self, item):
        self.list.insert(0,item)

    def pop(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def size(self):
        return len(self.list)
s = Stack()
sk = input('Введите строку из скобок: ')
s.push(sk)

l1 = ["[","{","("]
l2 = ["]","}",")"]

def my_def():
    my_list = []
    for i in s.list[0]:
        if i in l1:
            my_list.append(i)
        elif i in l2:
            posicion = l2.index(i)
            if ((len(my_list) > 0) and
                (l1[posicion] == my_list[len(my_list)-1])):
                my_list.pop()
            else:
                return "Небалансированно"
    if len(my_list) == 0:
        return "Сбалансированно"
    else:
        return "Небалансированно"
print(my_def())

