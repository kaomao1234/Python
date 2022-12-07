

class Node:
    def __init__(self, child=None):
        self.parent = None
        self.child = child
        if(self.child is not None):
            self.child.parent = self
            self.show()
    def show(self):
        print(self)
        if(self.child is not None):
            self.child.show()

    def create_state(self):
        return _NodeState(self)


class _NodeState:
    def __init__(self, object: Node):
        self.object = object
        self.init_state()
        self.build(self)

    def init_state(self):
        print(f"{self.object}: {self} call init_state")

    def build(self, context: Node):
        print(f"{self.object}: {self} call build")

    def set_state(self, state):
        state()
        self.build(self.object)


node = Node(
    child=Node(
        child=Node()
    )
)
print(node)
