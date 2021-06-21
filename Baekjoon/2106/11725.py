import sys


def get_parents():
    global parent_of_node, link_of_node

    stack = [1]
    parent_of_node[1] = 1

    # node 1부터 자식들을 찾아서 parent_of_node에 등록하고 stack에 추가
    while stack:
        parent = stack.pop()

        for child in link_of_node[parent]:
            if parent_of_node[child]:
                continue
            parent_of_node[child] = parent
            stack.append(child)


if __name__ == '__main__':
    N = int(input())
    parent_of_node = [0 for _ in range(N+1)]
    link_of_node = [[] for _ in range(N+1)]

    for _ in range(N-1):
        node1, node2 = map(int, sys.stdin.readline().split())
        link_of_node[node1].append(node2)
        link_of_node[node2].append(node1)

    get_parents()

    for parent in parent_of_node[2:]:
        print(parent)