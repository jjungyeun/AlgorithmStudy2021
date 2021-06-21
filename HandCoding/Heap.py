class MaxHeap:
    def __init__(self):
        self.my_list = [None]

    def append(self, data):
        self.my_list.append(data)
        idx = len(self.my_list) - 1

        # 추가한 노드가 부모 노드보다 크면 바꿔가면서 위치 찾아가기
        while idx > 1 and self.my_list[idx // 2] < self.my_list[idx]:
            self.my_list[idx // 2], self.my_list[idx] = self.my_list[idx], self.my_list[idx // 2]
            idx = idx // 2

    def delete(self):
        if len(self.my_list) < 2:
            res = self.my_list[-1]
            self.my_list = [None]
            return res

        # 루트노드와 마지막노드의 위치를 바꾼 뒤 삭제
        self.my_list[1], self.my_list[-1] = self.my_list[-1], self.my_list[1]
        res = self.my_list.pop()

        # 루트노드에 올라온 값의 알맞은 위치를 찾아가기
        self.heapify(1)
        return res

    def heapify(self, root):
        size = len(self.my_list)
        largest = root
        left, right = root * 2, root * 2 + 1

        if left < size and self.my_list[left] > self.my_list[largest]:
            largest = left

        if right < size and self.my_list[right] > self.my_list[largest]:
            largest = right

        if largest != root:
            self.my_list[largest], self.my_list[root] = self.my_list[root], self.my_list[largest]
            self.heapify(largest)


h = MaxHeap()
h.append(39)
h.append(6)
h.append(5)
h.append(45)
h.append(355)

for i in range(5):
    print(h.delete())