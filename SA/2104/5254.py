class Node:
    def __init__(self):
        self.index = -1
        self.pEdge = None
        self.cEdges = []

    def setIndex(self, num):
        self.index = num

    def setParent(self, edge):
        self.pEdge = edge

    def setChild(self, edge):
        self.cEdges.append(edge)
        if edge.getSource() is None:
            edge.setSource(self)


    def getParentNode(self):
        parentEdge = self.pEdge
        if parentEdge is None:
            return None
        return parentEdge.getSource()

    def getChildNodes(self):
        childEdges = self.cEdges
        cNodes = []
        for e in childEdges:
            cNodes.append(e.getDestination())
        return cNodes

    def isLeaf(self):
        if len(self.cEdges) == 0:
            return True
        return False

    def getCommonPrefix(self, word):
        pEdgePrefix = self.pEdge.getPrefix()
        i = 0
        while i < len(word) and i < len(pEdgePrefix) and word[i] == pEdgePrefix[i]:
            i += 1
        return word[:i]


class Edge:
    def __init__(self, sNode, dNode, prefix):
        self.source = sNode
        self.destination = dNode
        self.commonPrefix = prefix

    def getPrefix(self):
        return self.commonPrefix

    def getSource(self):
        return self.source

    def getDestination(self):
        return self.destination

    def setCommonPrefix(self, p):
        self.commonPrefix = p

    def setSource(self, n):
        self.source = n

    def setDestination(self, n):
        self.destination = n


class SuffixTree:
    def __init__(self):
        self.head = Node()

    def addSuffix(self, suffix):
        here = self.head
        hereSuffix = suffix
        commonPrefix = None
        while not here.isLeaf():
            cNodes = here.getChildNodes()
            commonPrefix = None
            for cNode in cNodes:
                # prefix 겹치는 node 있으면 밑으로 타고 내려가기
                commonPrefix = cNode.getCommonPrefix(hereSuffix)
                if len(commonPrefix) != 0:
                    here = cNode
                    hereSuffix = hereSuffix[len(commonPrefix):]
                    break
            # prefix 겹치는 node 없으면 끝
            if commonPrefix is None or commonPrefix == '':
                break

        # here 아래에 그냥 추가
        if commonPrefix is None or commonPrefix == '':
            newNode = Node()
            newEdge = Edge(here, newNode, hereSuffix)
            newNode.setParent(newEdge)
            here.setChild(newEdge)
        # 중간 노드 생성해서 추가
        else:
            parentEdge = here.pEdge
            originSuffix = parentEdge.getPrefix()

            prefix1 = originSuffix[len(commonPrefix):]
            prefix2 = hereSuffix

            midNode, newNode = Node(), Node()
            Edge1 = Edge(midNode, here, prefix1)
            Edge2 = Edge(midNode, newNode, prefix2)

            parentEdge.setCommonPrefix(commonPrefix)
            parentEdge.setDestination(midNode)

            midNode.setParent(parentEdge)
            midNode.setChild(Edge1)
            midNode.setChild(Edge2)

            here.setParent(Edge1)
            newNode.setParent(Edge2)

        # self.printTree()

    def printTree(self):
        print("----")
        print("print Tree:")

        def dfs(here, cnt):
            # print(here.getParentNode())
            if not here.isLeaf():
                for e in here.cEdges:
                    print(cnt, e.getPrefix())
                    dfs(e.getDestination(), cnt+1)

        dfs(self.head, 1)
        print("----")

    def sortTree(self):
        q = [self.head]
        while q:
            here = q.pop(0)
            if not here.isLeaf():
                sortedChildren = sorted(here.cEdges, key=lambda x: x.getPrefix())
                here.cEdges = sortedChildren
                q += here.getChildNodes()

    def getNthPrefix(self, N):
        global cnt, answer
        cnt = 0
        answer = ''

        def dfs(here, prefix):
            global cnt, answer
            # print("cnt, prefix: ", cnt, prefix)
            # print("is answer None?", answer)
            if answer != '':
                return
            if not here.isLeaf():
                for e in here.cEdges:
                    if answer != '':
                        return
                    p = e.getPrefix()
                    p = p.replace('$', '')
                    if cnt >= N - len(p):
                        answer = prefix + p[:N-cnt]
                        break
                    cnt += len(p)
                    dfs(e.getDestination(), prefix + p)

        dfs(self.head, '')


cnt = 0
answer = ''

if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        tmp = input().split()
        N, word = int(tmp[0]), tmp[1]
        word += '$'

        ST = SuffixTree()
        for i in range(len(word)):
            suffix = word[i:]
            ST.addSuffix(suffix)
        ST.sortTree()
        ST.printTree()
        ST.getNthPrefix(5)
        print("#%d %s %d" % (T, answer[0], len(answer)))