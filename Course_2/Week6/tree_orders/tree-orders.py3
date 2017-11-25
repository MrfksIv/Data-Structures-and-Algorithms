# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:

    def read(self):
        self.nodes_list = []
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.has_been_added = [False for i in range(self.n)]
    
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        """In-order tree traversal."""
        current_id = 0
        stack = []

        while True:
            if current_id != -1:
                stack.append(current_id)
                current_id = self.left[current_id]
            elif stack:
                current_id = stack.pop()
                yield self.key[current_id]
                current_id = self.right[current_id]
            else:
                break


    def preOrder(self):
        """Pre-order tree traversal."""
        current_id = 0
        stack = []

        while True:
            if current_id != -1:
                yield self.key[current_id]
                stack.append(current_id)
                current_id = self.left[current_id]
            elif stack:
                current_id = stack.pop()
                current_id = self.right[current_id]
            else:
                break

    def postOrder(self):
        """Post-order tree traversal."""
        # Create two stacks and push root's index to the first one.
        stack1 = [0]
        stack2 = []

        while stack1:
            current_id = stack1.pop()
            stack2.append(self.key[current_id])

            left_id = self.left[current_id]
            right_id = self.right[current_id]
            if left_id != -1:
                stack1.append(left_id)
            if right_id != -1:
                stack1.append(right_id)

        while stack2:
            yield stack2.pop()

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
