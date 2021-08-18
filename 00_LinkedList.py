class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def print(self):
        curn = self.head
        string = ''
        while curn:
            string += str(curn.data)
            if curn.next:
                string += '->'
            curn = curn.next
        print(string)


if __name__=='__main__':
    sl = SingleLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.print()
