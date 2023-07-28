class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def bfs(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        print(node.data, end=' ')

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def dfs(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while len(stack) != 0:
        node = stack.pop()
        print(node.data, end=' ')

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

# Example usage
if __name__ == '__main__':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("BFS: ", end='')
    bfs(root)

    print("\nDFS: ", end='')
    dfs(root)