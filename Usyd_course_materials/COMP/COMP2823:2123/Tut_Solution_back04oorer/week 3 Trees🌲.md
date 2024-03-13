### `Pre-order Traversal`
```Python
def PRE_ORDER_TRAVERSAL(root):
	vist(root)
	for child in root.children():
		PRE_ORDER_TRAVERSAL(child)
	return
```

### `In-order Traversal`

```Python
def IN_ORDER_TRAVERSAL(root):
	if root == None:
		return None
	
	if root.left() is not None:
		return IN_ORDER_TRAVERSAL(root.left())
	
	visit(root)
	
	if root.right() is not None:
		return IN_ORDER_TRAVERSAL(root.right())
	
```


### `Post-order Traversal
```Python
def POST_ORDER_TRAVERSAL(root):
	for child in root.children():
		POST_ORDER_TRAVERSAL(child)
	visit(root)
	return
```
### Q5

Design an algorithm that given a `binary tree T` and a node u, returns the  
node that would be visited after u in a  `pre-order` traversal. Your algorithm should  
not compute the full traversal and then search for u in that traversal.  

```Python
def Find_Next(Node):
	if Node.left() is not None:
		return Node.left()
  
	if Node.right() is not None:
		return Node.right()

	return helper(Node.parent())

def helper(Node):
	if Node == None:
		return None

	if Node.right() is not None:
		return Node.right()
	else:
		return helper(Node.parent())
```

The algorithm may take up to O(n) time to find the next node.

### Q6

Design an algorithm that given a `binary tree T` and a node u, returns the  
node that would be visited after u in an  
`in-order traversal`. Your algorithm should  
not compute the full traversal and then search for u in that traversal.  

```Python
def Find_Left_most(Node):
	if Node.left() is not None:
		return Find_Left_most(Node.left())
	return Node

def Find_Next(Node):
	if Node.right() is not None:
		return Find_Left_most(Node.right())
	return Find_Next(Node.parent())

Find_Next(Node)
```

### Q7
Design an algorithm that given a `binary tree` T and a node u, returns the node that would be visited after u in a <mark style="background: #FFF3A3A6;">post-order traversal</mark>. Your algorithm <mark style="background: #FFF3A3A6;">should not</mark> compute the full traversal and then search for u in that traversal.

```Python
def Find_Next(Node):
	if Node.parent() is None:
		return None
	
	if Node.parent().left() == Node:
		# current Node is left one
		if Node.parent.right():
			return Post_order_traversal(Node.parent.right())
		else:
			return Node.parent()
	else:
		# current Node is right one, and there is no subtree
		return Node.parent()
```

<mark style="background: #FF5582A6;">Hint</mark> Node u is the most recently visited node (in the traversal method given in the problem).


### Q8
The balance factor of a node in a binary tree is the absolute difference in height between its left and right subtrees (if the left/right subtree is empty we consider its height to be -1). Design an algorithm for computing the balance factor of every node in the tree in O(n) time.

Hint: Same idea with <mark style="background: #FF5582A6;">calculate height</mark> of every node in a tree.

Here is a function that calculate height of every node:
```Python
def Find_Height(Node):
	if Node.left():
		left_H = Find_Height(Node.left())
	else:
		left_H = -1 # there is no left subtree, mark as -1
		
	if Node.right():
		right_H = Find_Height(Node.right())
	else:
		right_H = -1 # there is no right subtree, mark as -1
	
	return Max(left_H,right_H) + 1

```

Since the function above has calculated the height of left/right subtrees.We can simply add a new line to calculate the factor.


```Python
def Calculate_factor(Node):
	if Node.left():
		left_H = Calculate_factor(Node.left())
	else:
		left_H = -1 # there is no left subtree, mark as -1
		
	if Node.right():
		right_H = Calculate_factor(Node.right())
	else:
		right_H = -1 # there is no right subtree, mark as -1
	
	print(abs(left_H - right_H))
	
	return Max(left_H,right_H) + 1
```



### Q9
Describe an algorithm for performing an <mark style="background: #FF5582A6;">Euler tour traversal</mark> of a binary tree that runs in linear time and __does not__ use a stack or recursion.

<mark style="background: #FF5582A6;">Euler tour traversal</mark>: Generic traversal of a binary tree. Includes as special cases the preorder, postorder and in-order traversals.

<mark style="background: #FF5582A6;">Hint</mark>: The next node we want to visit is determined by the current node and how we visit the current node (Left, Bottom, Right).


```Python
def Find_next(c, w): 
	# c -> current node , w -> how we visit the current node
	if w == "L" and c.left():
		return c.left(),"L"
	if w == "L" and not c.left():
		return c,"B"
	if w == "B" and c.right():
		return c.right(),"L"
	if w == "B" and not c.right():
		return c,"R"
	if w == "R" and c == root:
		return "end"
	if w == "R" and c == c.parent().left():
		return c.parent(),"B"
	if w == "R" and c == c.parent().right():
		return c.parent(),"R"

		
	
```
### Q11
Design a linear time algorithm that given a sorted sequence of n values, builds a binary search tree T holding these values such that the height of T is ⌊log2 n⌋. For simplicity, you can assume that n = 2^k − 1 for some positive integer k.

```Python
def ILoveVb(i,j,Node):
	if i == j:
		if Array[j] < Node.value():
			Node.left().setvalue(Array[j])
		else:
			Node.right().setvalue(Array[j])
		return
	
	
	if Array[j] < Node.value():
		Node.left().setvalue(Array[(i+j)/2])
		stack.push(i,(i+j)/2 -1,Node.left())
		stack.push((i+j)/2+1,j,Node.left())

	if Array[i] > Node.value():
		Node.right().setvalue(Array[(i+j)/2])
		stack.push(i,(i+j)/2 -1,Node.right())
		stack.push((i+j)/2+1,j,Node.right())
	return

i = 0
j = len(Array) - 1
Tree.root.value = Array[(i+j)/2]
stack.push(i,(i+j)/2-1,root)
stack.push((i+j)/2-1,j,root)

while stack.isNotEmpty():
	i,j,Node = stack.pop()
	ILoveVb(i,j,Node)
``` 

#### runnable version(Python)
```Python
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_value(self, value):
        self.value = value

    def set_left(self, node):
        self.left_child = node

    def set_right(self, node):
        self.right_child = node

def ILoveVb(i, j, node):
    if i == j:
        if Array[j] < node.value:
            node.set_left(Node(Array[j]))
        else:
            node.set_right(Node(Array[j]))
        return

    if Array[j] < node.value:
        mid = (i + j) // 2
        node.set_left(Node(Array[mid]))
        stack.append((i, mid - 1, node.left_child))
        stack.append((mid + 1, j, node.left_child))

    if Array[i] > node.value:
        mid = (i + j) // 2
        node.set_right(Node(Array[mid]))
        stack.append((i, mid - 1, node.right_child))
        stack.append((mid + 1, j, node.right_child))
    return

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right_child, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left_child, level + 1)

# Example array to create BST from
Array = [1, 6, 8, 14, 20, 21, 28]
i = 0
j = len(Array) - 1
root = Node(Array[(i + j) // 2])

stack = []
stack.append((i, (i + j) // 2 - 1, root))
stack.append(((i + j) // 2 + 1, j, root))

while stack:
    i, j, node = stack.pop()
    ILoveVb(i, j, node)

# Now print the tree
print_tree(root)

```
### Q12
Design an external memory data structure for maintaining a list that supports index-based insertions and deletions in O(n/B) transfers.

I know is <mark style="background: #FF5582A6;">B tree</mark>, but how to implement it?