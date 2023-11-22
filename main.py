#### LINKED LISTS ####

nyc_parks = ["Central", "Prospect", "Riverside", "Washington Square"]

# A list stores a collection of data, has a beginning and end, it is ordered

# What is a linked list?

# What is a node?

# How do we traverse a linked list?

# "utica" --> "franklin" --> "atlantic" --> "nevins"

class LinkedListNode:

    def __init__(self, data):
        # what is my data?
        self.data = data
        # what is the next node in the list?
        self.next = None

    def __repr__(self):
        return f"LinkedListNode(data={self.data})"
    
    def create_next(self, data):
        self.next = LinkedListNode(data)
    
utica = LinkedListNode("Utica")
utica.create_next("Franklin")