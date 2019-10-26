# # Do not edit the class below except for
# # the insert, contains, and remove methods.
# # Feel free to add new properties and methods
# # to the class.


# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         currentNode = self

#         while True:
#             if value < currentNode.value:
#                 if currentNode.left is None:
#                     currentNode.left = BST(value)
#                     break
#                 else:
#                     currentNode = currentNode.left
#             else:
#                 if currentNode.right is None:
#                     currentNode.right = BST(value)
#                     break
#                 else:
#                     currentNode = currentNode.right
#         return self

#     def contains(self, value):
#         currentNode = self

#         while currentNode is not None:
#             if value < currentNode.value:
#                 currentNode = currentNode.left
#             elif value > currentNode.value:
#                 currentNode = currentNode.right
#             else:
#                 # print('Value Found')
#                 return True
#         # print('Value not found')
#         return False

#         # while True:
#         #     if value > currentNode.value:
#         #         if currentNode.right != None:
#         #             currentNode = currentNode.right
#         #         else:
#         #             print('Not Found')
#         #             break
#         #     elif value < currentNode.value:
#         #         if currentNode.left != None:
#         #             currentNode = currentNode.left
#         #         else:
#         #             print('Not Found')
#         #             break
#         #     elif value == currentNode.value:
#         #         print('Value found')
#         #         break

#     def remove(self, value, parentNode=None):
#         currentNode = self

#         while currentNode is not None:
#             if value < currentNode.value:
#                 parentNode = currentNode
#                 currentNode = currentNode.left
#             elif value > currentNode.value:
#                 parentNode = currentNode
#                 currentNode = currentNode.right
#             else:
#                 # ? Case 1: Node has two children nodes
#                 if currentNode.left is not None and currentNode.right is not None:
#                     currentNode.value = currentNode.right.getMinVal()
#                     currentNode.right.remove(currentNode.value, currentNode)
#                 # ? The cases left are the ones with the parent node and without the parent node
#                 # ? For e.g. the root node of the bst that do not have a parent node
#                 #! We're gonna do this case later
#                 # ? Finally to our case in which the parent node is None
#                 elif parentNode is None:
#                     if currentNode.left is not None:
#                         currentNode.value = currentNode.left.value
#                         currentNode.right = currentNode.left.right
#                         currentNode.left = currentNode.left.left
#                     elif currentNode.right is not None:
#                         currentNode.value = currentNode.right.value
#                         currentNode.left = currentNode.right.left
#                         currentNode.right = currentNode.right.right
#                     else:
#                         currentNode.value = None
#                 elif parentNode.left == currentNode:
#                     parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
#                 elif parentNode.right == currentNode:
#                     parentNode.right = currentNode.right if currentNode.right is not None else currentNode.right

#                 pass
#         return self

#     def getMinVal(self):
#         return self


# test1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
# print(test1.right.value)
# test1.contains(5)

# test1.contains(50)


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
		currentNode = self  # save the current node

		while True:
			# we need to check where we need to put the node
			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
					currentNode = currentNode.left
			else:  # value > currentNode.value:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
        return self

    def contains(self, value):
		currentNode = self
		
		while currentNode is not None:
			if value > currentNode.value:
				currentNode = currentNode.right
			elif value < currentNode.value:
				currentNode = currentNode.left
			else:
				return True
		return False
	
	def getMinVal(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		return currentNode.value	

    def remove(self, value, parentNode = None):
		# The most important method of the bst
		# Case 1:
		# In this case we have both the left and right childs
		# The solution is to replace the parent node with the smallest value node 
		# of the right sub tree
		currentNode = self
		
		# First of all lets search for the node to be removed
		while currentNode is not None:
			if value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
			elif value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			else:
				if currentNode.left is not None and currentNode.right is not None:
					currentNode.value = currentNode.right.getMinVal()
					# Now we replaced the value for the node to be deleted 
					# But now we have to delete the other node too
					currentNode.right.remove(currentNode.value, currentNode)
				# The case where we do not have the parent node
				# The case for the root node
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else: # if the root node does not have both the elements in it 
						currentNode.value = None
				# That is how we dealt with the case
				# Now for the easier sub cases in which we have only 1 Node present on the parent node
				# This case works since we already took care for the case when we have both childs for 
				# the parent node
				elif parentNode.left == currentNode: 
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
				break
		return self
