class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if temp.value == value:
                return False
            elif value < temp.value:
                if temp.left is None:
                    temp.left = node
                    node.parent = temp
                    return True
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = node
                    node.parent = temp
                    return True
                temp = temp.right

    def __contains__(self, item):
        temp = self.root
        while True:
            if temp is None:
                return False
            if item == temp.value:
                return True
            elif item < temp.value:
                temp = temp.left
            elif item > temp.value:
                temp = temp.right

    # we assume x to be Non-NIL
    @staticmethod
    def subtree_first(x: Node):
        temp = x
        while temp.left:
            temp = temp.left
        return temp

    # we assume x to be Non-NIL
    @staticmethod
    def subtree_last(x: Node):
        temp = x
        while temp.right:
            temp = temp.right
        return temp

    # we assume x to be Non-NIL
    def successor(self, x: Node):
        if x.right:
            return self.subtree_first(x.right)
        while True:
            if x.parent is None:
                return None
            if x.parent.left == x:
                return x.parent
            x = x.parent

    # we assume x to be Non-NIL
    def subtree_insert_after(self, x: Node, value):
        new = Node(value)
        if x.right is None:
            x.right = new
            new.parent = x
            return True
        successor = self.successor(x)
        successor.left = new
        new.parent = successor
        return True

    # we assume x to be Non-NIL
    def predecessor(self, x: Node):
        if x.left:
            return self.subtree_last(x.left).value
        while True:
            if x.parent is None:
                return None
            if x.parent.right == x:
                return x.parent.value
            x = x.parent

    # we assume x to be Non-NIL
    def subtree_insert_before(self, x: Node, value):
        new = Node(value)
        if x.left is None:
            x.left = new
            new.parent = x
            return True
        predecessor = self.predecessor(x)
        predecessor.right = new
        new.parent = predecessor
        return True

    def subtree_delete(self, x: Node):
        pass

    # we assume x to be Non-NIL
    def traverse(self, x: Node):
        if x:
            self.traverse(x.left)
            print(x.value, end=" ")
            self.traverse(x.right)
