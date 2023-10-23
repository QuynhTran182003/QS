# Vytvořte vlastní třídu, která repezentuje datovou strukturu fronta ale uvnitř své prvky ukládá
# jako obousměrný spojový seznam. # Třída musí mít následující funkcionality:

# Přidání jednoho prvek na konec fronty metodou add()
# Získání prvku ze začátku fronty, včetně jeho odebrání, metodou pop()
# Získání počtu prvků metodou count()
# Vyprázdnění celé fronty metodou clear()
# Získání všech prvků metodou popAll() jako tuple nebo list, včetně vyprázdění fronty.
# Nezapomeňte vyřešit chybové stavy, například volání pop() nad prázdnou frontou..

class Node:
    """Class represents the NODE (element) in the queue"""

    def __init__(self, value):
        """Initialization node with a value"""
        self.value = value
        self.next = None
        self.prev = None

class MyQueue:
    """Class represents my queue"""

    def __init__(self):
        """Initialization empty queue"""
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value):
        """Add an element to the end of the queue"""
        newNode = Node(value)
        # first create a new node with the value arg. for adding to the queue
        if self.head is None:
            # if queue doesnt have head (queue is empty), set new node as tail and head of the queue
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def pop(self):
        """Get the first NODE (element) and delete it from the queue"""
        if self.head is None:
            # if the queue is empty, raise the exception
            raise IndexError("Queue is empty")
        popNode = self.head
        # get value of the head node, assigned to popNode

        if self.head == self.tail:
            # if the queue has 1 node, eg. head = tail, then set all = None
            self.head = None
            self.tail = None
        else:
            # assign the actual head node value to the next node's value
            self.head = self.head.next

        self.length -= 1
        # in the end decrease the length of queue for 1 ndoe (element) and return the poped node
        return popNode

    def count(self):
        """Get the length of the queue"""
        return self.length

    def clear(self):
        """Clear the queue"""
        self.head = None
        self.tail = None
        self.length = 0

    def popAll(self):
        """Get all of the elements in the queue and delete them from the queue"""

        if self.head is None:
            # if the queue is empty, raise the exception
            raise IndexError("Queue is empty")

        popNodes = []
        # list popNodes for saving all elements (elementss value)
        while self.head is not None:
            popNode = self.head
            self.head = self.head.next
            popNodes.append(popNode.value)
        return popNodes


    def displayQueue(self):
        """The method is not required but to check if my program is working"""
        displayRes = ""
        currentNode = self.head

        while currentNode is not None:
            displayRes += str(currentNode.value) + " "
            currentNode = currentNode.next
        print(displayRes if displayRes != "" else "None")


"""Use myQueue"""
myQueue = MyQueue()
myQueue.add("a")
myQueue.add("b")
myQueue.add("c")
myQueue.add("d")
myQueue.add("e")

print(myQueue.count())
myQueue.displayQueue()
print("after pop" + str(myQueue.popAll()))
myQueue.displayQueue()