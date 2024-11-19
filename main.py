'''
Користувач вводить з клавіатури набір чисел. Отримані числа необхідно зберегти в список (тип списку потрібно вибрати
залежно від поставленого нижче завдання). Після чого потрібно показати меню, у якому запропонувати користувачеві набір
пунктів:
1. Додати нове число в список (якщо таке число існує в списку, потрібно вивести повідомлення користувачеві про це,
без додавання числа).
2. Видалити всі входження числа зі списку (користувач вводить із клавіатури число для видалення).
3. Показати вміст списку (залежно від вибору користувача список потрібно показати з початку або з кінця).
4. Перевірити чи є значення в списку.
5. Замінити значення у списку (користувач визначає замінити тільки перше входження чи всі входження).
Залежно від вибору користувача виконується дія, після чого меню відображається знову'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class List_bidirectional(Node):
    def __init__(self):
        self.head = None
        self.tail = None

    def isvalinlist(self, value):
        if self.head.data == value:
            return True
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.data == value:
                return True
        return False

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        if self.isvalinlist(data):
            print(f"The value {data} has already in list. You can't add one more.")
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last
        self.tail = new_node
        #self.tail.prev = last

    def display_top(self):
        # print(self.head.data)
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_tail(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    def del_nodes(self, value):
        #searching value is in first node
        if self.head.data == value:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            del tmp
            return value
        #search value
        current = self.head
        while current.next:
            if current.next.data == value:
                tmp = current.next
                current.next = current.next.next
                if tmp.next is None:
                    self.tail = self.tail.prev
                else:
                    tmp.next.prev = current
                del tmp
            current = current.next
        return value

    def reverse(self, oldvalue, newvalue):
        if self.head.data == oldvalue:
            self.head.data = newvalue
            return oldvalue
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.next.data == oldvalue:
                temp.next.data = newvalue
                return oldvalue

    def reverseall(self, oldvalue, newvalue):
        #if self.head.data == oldvalue:
        #    self.head.data = newvalue
        temp = self.head
        while temp:
            print(temp.data)
            if temp.data == oldvalue:
                temp.data = newvalue
            temp = temp.next

dll=List_bidirectional()

while True:
    sw = int(input("1 - add, 2 - del, 3 - print, 4 - is value in list? 5- reverse, 0 - exit: "))
    if sw == 1:
        num = int(input("Enter the num for adding: "))
        dll.append(num)
    elif sw == 2:
        num = int(input("Enter the num for deleting: "))
        #sw1 = input(f"Do you want to delete all value = {num}? (y/n)")
        dll.del_nodes(num)
    elif sw == 3:
        sw1 = int(input(f"Do you want to print from first to last - 1 or last to first - 2?"))
        if sw1 == 2:
            dll.display_tail()
        else:
            dll.display_top()
    elif sw == 4:
        num = int(input("Enter the num for finding: "))
        if dll.isvalinlist(num):
            print(f"{num} is in List.")
        else:
            print(f"{num} isn't in List.")
    elif sw == 5:
        old = int(input("Enter the num for reversing: "))
        new = int(input("Enter the new value: "))
        sw1 = int(input(f"Do you want to reverse all value - 1 or only first value - 2?"))
        if sw1 == 1:
            dll.reverseall(old, new)
        else:
            dll.reverse(old, new)

    elif sw == 0:
        break
