#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
    
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

    def IsBinarySearchTree(self):
        # Implement correct algorithm here
        if self.n > 1:
          ordered_tree = list(self.inOrder())
        #   print(ordered_tree)
          for i in range(0, self.n-1):
              if ordered_tree[i + 1] < ordered_tree[i] :
                    return False       
              if ordered_tree[i + 1] == ordered_tree[i]:
                   if self.key[self.left[self.key.index(ordered_tree[i + 1])]] == ordered_tree[i + 1] and self.left[self.key.index(ordered_tree[i + 1])] != -1:
                    return False
        return True

def read(self):
        self.nodes_list = []
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
    
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
def main():
      
  tree = TreeOrders()
  tree.read()

  if tree.IsBinarySearchTree():
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
