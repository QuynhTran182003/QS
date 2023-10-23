class Node:
    """Class represents the NODE (element) in the stack"""

    def __init__(self, value):
        """Initialization node with a value"""
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        """Initialization empty stack"""
        self.top = None
        self.length = 0

    def add(self, value):
        """Add an element to the end of the stack"""
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1

    def pop(self):
        """Get the first NODE (element) and delete it from the stack"""
        if self.top is None:
            # if the stack is empty, raise the exception
            raise IndexError("Stack is empty")
        # get value of the top node, assigned to popNode
        else:
            # assign the actual top node value to the next node's value
            popNode = self.top
            self.top = self.top.next
        self.length -= 1
        # in the end decrease the length of stack for 1 ndoe (element) and return the poped node
        return popNode

    def count(self):
        """Get the length of the stack"""
        return self.length

    def clear(self):
        """Clear the stack"""
        self.top = None
        self.length = 0

    def popAll(self):
        """Get all of the elements in the stack and delete them from the stack"""

        if self.top is None:
            # if the stack is empty, raise the exception
            raise IndexError("Stack is empty")

        popNodes = []
        # list popNodes for saving all elements (elementss value)
        while self.top is not None:
            popNode = self.top
            self.top = self.top.next
            popNodes.append(popNode.value)
        return popNodes

    def displayQueue(self):
        """The method is not required but to check if my program is working"""
        displayRes = ""
        currentNode = self.top

        while currentNode is not None:
            displayRes += str(currentNode.value) + " "
            currentNode = currentNode.next

        print(displayRes if displayRes != "" else "None")


# use MyStack
myStack = MyStack()
myStack.add("a")
myStack.add("d")
myStack.add("e")
myStack.add("b")
myStack.add("g")
myStack.add("e")


myStack.displayQueue()

print("after pop" + str(myStack.popAll()))
myStack.displayQueue()
