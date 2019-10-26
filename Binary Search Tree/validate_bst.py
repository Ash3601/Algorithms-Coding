def validateBst(tree):
    return validateBstHelper(tree, float('-inf'), float('inf'))


def validateBstHelper(tree, minVal, maxVal):

    if tree is None:
        return True

    if tree.value < minVal or tree.value >= maxVal:
        return False

    isValid_leftSubTree = validateBstHelper(tree.left, minVal, tree.value)
    isValid_rightSubTree = validateBstHelper(tree.right, tree.value, maxVal)
    return isValid_leftSubTree and isValid_rightSubTree
