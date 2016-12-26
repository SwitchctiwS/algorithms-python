def depth_first_search(root, node):
    stack = [root]

    while len(stack) is not 0:
        current = stack.pop()

        if current == node:
            return current

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return None
