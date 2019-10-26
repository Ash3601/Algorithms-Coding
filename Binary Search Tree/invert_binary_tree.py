class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self

        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                # print('Value Found')
                return True
        # print('Value not found')
        return False

        # while True:
        #     if value > currentNode.value:
        #         if currentNode.right != None:
        #             currentNode = currentNode.right
        #         else:
        #             print('Not Found')
        #             break
        #     elif value < currentNode.value:
        #         if currentNode.left != None:
        #             currentNode = currentNode.left
        #         else:
        #             print('Not Found')
        #             break
        #     elif value == currentNode.value:
        #         print('Value found')
        #         break

    def remove(self, value, parentNode=None):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # ? Case 1: Node has two children nodes
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinVal()
                    currentNode.right.remove(currentNode.value, currentNode)
                # ? The cases left are the ones with the parent node and without the parent node
                # ? For e.g. the root node of the bst that do not have a parent node
                #! We're gonna do this case later
                # ? Finally to our case in which the parent node is None
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.right

                pass
        return self

    def getMinVal(self):
        return self


def _invertBst(tree):
    tree.left, tree.right = tree.right, tree.left
    return tree


def invertBst(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invertBst(tree.left)
        invertBst(tree.right)
    return tree


def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.value, end=' ')
        inorder(tree.right)


tree = BST(10).insert(5).insert(15).insert(26).insert(0).insert(3)
inorder(tree)
# print(tree.value)
# if tree.left is None:
#     print('None')
# else:
#     print(tree.left.value)


# if tree.right is None:
#     print('None')
# else:
#     print(tree.right.value)


print()

tree = invertBst(tree)
inorder(tree)

# print(tree.value)
# if tree.left is None:
#     print('None')
# else:
#     print(tree.left.value)


# if tree.right is None:
#     print('None')
# else:
#     print(tree.right.value)
