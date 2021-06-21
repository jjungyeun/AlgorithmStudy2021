import sys


class TreeNode:
    def __init__(self, number, parent):
        self.number = number
        self.parent = parent
        self.left = None
        self.right = None
        self.sequence = 0
        self.level = 0


cnt = 1
def dfs(node, depth):
    global treeLevelRange, maxLevel, cnt
    node.level = depth
    s, e = treeLevelRange[depth]
    if s == -1:
        s = node.number
    e = node.number
    maxLevel = max(maxLevel, depth)
    treeLevelRange[depth] = (s, e)

    if node.left != None:
        dfs(node.left, depth + 1)

    node.sequence = cnt
    cnt += 1

    if node.right != None:
        dfs(node.right, depth + 1)


def getTreeWidth(level):
    global tree, treeLevelRange
    start, end = treeLevelRange[level]
    return tree[end].sequence - tree[start].sequence + 1


if __name__ == '__main__':
    N = int(input())

    tree = [TreeNode(0, None)] * (N+1)
    treeLevelRange = [(-1, -1)] * (N+1)
    maxLevel = 1

    for _ in range(N):
        p, c1, c2 = map(int, sys.stdin.readline().split())
        if tree[p].number == 0:
            tree[p] = TreeNode(p, None)

        if c1 != -1:
            if tree[c1].number == 0:
                leftChild = TreeNode(c1, tree[p])
                tree[p].left = leftChild
                tree[c1] = leftChild
            else:
                tree[p].left = tree[c1]
                tree[c1].parent = tree[p]
        if c2 != -1:
            if tree[c2].number == 0:
                rightChild = TreeNode(c2, tree[p])
                tree[p].right = rightChild
                tree[c2] = rightChild
            else:
                tree[p].right = tree[c2]
                tree[c2].parent = tree[p]

    for i in range(1, N+1):
        if tree[i].parent == None:
            dfs(tree[i], 1)

    maxIdx = 1
    maximum = 1
    for i in range(1, maxLevel + 1):
        width = getTreeWidth(i)
        if width > maximum:
            maxIdx = i
            maximum = width

    print('%d %d' % (maxIdx, maximum))