import random
import sys
import os

try:
    import keyboard
except ModuleNotFoundError:
    os.system("pip install keyboard")

import keyboard

class VLineStack:
    def __init__(self, fruits, size):
        self.maximum = size
        self.values = random.choices(fruits, k=size)
    
    def __getitem__(self, key):
        return self.to_list()[key]
    
    def __len__(self):
        return self.maximum
    
    def pop(self):
        return self.values.pop()

    def to_list(self):
        return self.values + [None for _ in range(self.maximum - len(self.values))]

def get_fruits(level):
    fruits = "🍇🍑🍒🍓🥝🍉🍈🍊🍋🍌🍍🥭🥥🍎🍏🍐"
    result = []
    while len(result) != level:
        if (fruit := random.choice(fruits)) not in result:
            result.append(fruit)
    return result


fruits = get_fruits(3)

vlines = [VLineStack(fruits, 10) for _ in range(10)]

os.system('cls')



class Stack:
    def __init__(self, size):
        self.maximum = size
        self.values = []
    
    def get_values(self):
        return self.values

    def push(self, element):
        self.values.append(element)
    
    def __getitem__(self, key):
        return self.to_list()[key]

    def to_list(self):
        return self.values + [None for _ in range(self.maximum - len(self.values))]

    def bomb(self):
        if len(self.values) < 3:
            return
        size = 1
        element = self.values[-1]
        for i in range(len(self.values)-2, -1, -1):
            if element == self.values[i]:
                size += 1
            else:
                break
        if size < 3:
            return
        for _ in range(size):
            self.values.pop()
        show_cursor()

stack = Stack(10)


def show():
    sys.stdout.write("Fruits Crain\n\n")
    sys.stdout.write("┏━━━━━━━━━━━━━━━━━━━━━┓")
    sys.stdout.write("┏━━━┓\n")
    result = ["┃"+"".join(["%s" % (vlines[i][j] if vlines[i][j] is not None else "  ") for i in range(len(vlines))])+" ┃┃"+"%s" %
              (stack[j] if stack[j] is not None else "  ")+" ┃\n" for j in range(len(vlines[0])-1, -1, -1)]
    sys.stdout.write("".join(result))
    sys.stdout.write("┗━━━━━━━━━━━━━━━━━━━━━┛┗━━━┛\n")


cursor_index = 0


def show_cursor():
    os.system("cls")
    show()
    print(("%"+str(2*cursor_index+3)+"s") % "↑")


def dec_cursor_index():
    global cursor_index
    cursor_index -= 1
    cursor_index %= len(vlines)
    show_cursor()


def inc_cursor_index():
    global cursor_index
    cursor_index += 1
    cursor_index %= len(vlines)
    show_cursor()

def pop():
    global cursor_index
    stack.push(vlines[cursor_index].pop())
    show_cursor()

keyboard.add_hotkey('left', dec_cursor_index)
keyboard.add_hotkey('right', inc_cursor_index)
keyboard.add_hotkey('space', pop)
keyboard.add_hotkey('return', stack.bomb)

while True:
    pass
