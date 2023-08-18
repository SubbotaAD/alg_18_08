class Node:
    def __init__(self, value, next):
        self.value: int = value
        self.next: Node = next


string = [1, 2, 3, 4, 5]

node = Node(string[0], None)
head_pointer = node
for el in string[1:]:
    node.next = Node(el, None)
    node = node.next


def solve(prev: Node, cur: Node, head_pointer: Node):
    if cur.next is None:
        cur.next = prev
        head_pointer = cur
    else:
        next = cur.next
        cur.next = prev
        head_pointer = solve(cur, next, head_pointer)

    return head_pointer


prev_head = head_pointer
head_pointer = solve(head_pointer, head_pointer.next, head_pointer)
prev_head.next = None

el = head_pointer
while el is not None:
    print(el.value)
    el = el.next
