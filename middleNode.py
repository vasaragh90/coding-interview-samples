class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def middleNode(self):
        slowNode = self.head
        fastNode = self.head
        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return slowNode

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insertAtEnd(3)
    linked_list.insertAtEnd(4)
    linked_list.insertAtEnd(5)
    
    middle = linked_list.middleNode()
    if middle:
        print(f'Middle Node Value: {middle.value}')
    else:
        print('The list is empty')
