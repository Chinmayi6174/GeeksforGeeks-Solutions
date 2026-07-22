class minHeap:
    def __init__(self):
        self.heap = []

    def push(self, x: int):
        self.heap.append(x)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return -1
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self) -> int:
        return self.heap[0] if self.heap else -1

    def size(self) -> int:
        return len(self.heap)

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[parent] > self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._heapify_up(parent)

    def _heapify_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)
