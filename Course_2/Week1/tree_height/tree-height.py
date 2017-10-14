# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def go_down(arr, root):
        if len(arr[root]) == 0:
                return 1
        else:   
                heights = [0 for elem in arr[root]]
                # print('heights: {}'.format(heights))
                for (i,elem) in enumerate(arr[root]):
                        heights[i] = 1 + go_down(arr, elem)
        return max(heights)

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

       

        def compute_height(self):
                # Replace this code with a faster implementation
                arr = [[] for i in range(self.n)]
                root = None
                height = 0

                for i in range(self.n):
                        node = i
                        parent = self.parent[i]
                        if parent == -1:
                                root = i
                                height += 1
                        else:
                                arr[parent].append(node)

                # for root_children in arr[root]:
                return go_down(arr, root)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
