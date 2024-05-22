# Task One -

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'<Node|{self.value}>'
    



# Task Two - 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def get_food(self, get_value):
        node_check = self.head
        while node_check:
            if node_check.value == get_value:
                return node_check
            node_check = node_check.next
        return None


    def deletion(self, remove_value):
        if self.head is None:
            print('Nothing in this list!')
            return
        if self.head.value == remove_value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == remove_value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        print(f'{remove_value} is not here.')

    def traversal(self):
        print('Linked elements:')
        print('head\n | \n V')
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print(None)





# Task Three - 

planets = SinglyLinkedList()

planets.push('Mercury')
planets.push('Venus')
planets.push('Earth')
planets.push('Mars')
planets.push('Jupiter')
planets.push('Saturn')
planets.push('Uranus')
planets.push('Neptune')

planets.deletion('Mars')

planets.traversal()