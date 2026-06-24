# Write a function to find the maximum depth/height of a tree (Post-order DFS).
# Write a function to search for a value in a Binary Search Tree.
# Write a level-order traversal using a queue.
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.node = None

    def add(self,new_value):
        if self.node is None:
            self.node = Node(new_value)
        else:
            self._add(self.node,new_value)
    def _add(self,current_node,new_value):
        if current_node.val >= new_value:
            if current_node.left is None:
                current_node.left = Node(new_value)
            else:
                self._add(current_node.left,new_value)
        else:
            if current_node.right is None:
                current_node.right = Node(new_value)
            else:
                self._add(current_node.right,new_value)
    def _min(self,current_node):
        if current_node.left is None:
            return current_node.val
        return self._min(current_node.left)
    def _rm(self,current_node,value):
        if current_node is None:
            print("Value not found in the tree")
            return None
        if current_node.val == value:
            if current_node.left is None and current_node.right is None:
                current_node = None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                replace_node = self._min(current_node.right)
                current_node.val = replace_node
                current_node.right = self._rm(current_node.right,replace_node)
        # if current value is larger than remove value move left
        elif current_node.val > value:
            current_node.left = self._rm(current_node.left,value)
        # if current value is smaller than remove value move right
        elif current_node.val < value:
            
            current_node.right = self._rm(current_node.right,value)
        return current_node

# for adding the new node we have find the lowest postion

new_tree = Tree()
new_tree.add(5)
new_tree.add(3)
new_tree.add(7)
new_tree.add(2)
new_tree.add(4)

print(new_tree.node.val) # 5
print(new_tree.node.left.val) # 3
print(new_tree.node.right.val) # 7
print(new_tree.node.left.left.val) # 2
print(new_tree.node.left.right.val) # 4
print('pre order traversal')
def pre_order_traversal(node):
    if node is None:
        return None
    print(node.val)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
pre_order_traversal(new_tree.node)
print('in order traversal')
def in_order_traversal(node):
    if node is None:
        return None
    in_order_traversal(node.left)
    print(node.val)
    in_order_traversal(node.right)
in_order_traversal(new_tree.node)
print('post order traversal')
def post_order_traversal(node):
    if node is None:
        return None
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.val)
post_order_traversal(new_tree.node)
print('node removal')
new_tree._rm(new_tree.node,3)
print(new_tree.node.val) # 5
print(new_tree.node.left.val) # 3
print(new_tree.node.right.val) # 7
print(new_tree.node.left.left.val) # 2
#print(new_tree.node.left.right.val)