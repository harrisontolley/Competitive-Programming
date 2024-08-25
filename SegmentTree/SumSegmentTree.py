class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * (4 * len(data))

        if data:
            self.build(0, len(data) - 1, 0)


    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.data[start]
            return self.data[start]

        mid = (start + end) // 2
        self.tree[node] = self.build(start, mid, 2 * node + 1) + self.build(mid + 1, end, 2 * node + 2)
        return self.tree[node]


    def update(self, idx, value):
        # Update the value at index 'idx' to a new value and make appropriate adjustments in the segment tree.
        self._update_recursive(0, len(self.data) - 1, idx, value, 0)

    def query(self, start, end):
        # Inclusive of both start and end
        return self._query_recursive(0, len(self.data) - 1, start, end, 0)

    def _update_recursive(self, start, end, idx, value, node):
        if start == end:
            self.data[idx] = value
            self.tree[node] = value
            return value

        mid = (start + end) // 2
        if idx <= mid:
            self.tree[node] = self._update_recursive(start, mid, idx, value, 2 * node + 1) + self.tree[2 * node + 2]
        else:
            self.tree[node] = self.tree[2 * node + 1] + self._update_recursive(mid + 1, end, idx, value, 2 * node + 2)

        return self.tree[node]

    def _query_recursive(self, start, end, l, r, node):
        if r < start or l > end:
            return 0
        
        if l <= start and r >= end:
            return self.tree[node]
        
        mid = (start + end) // 2
        return self._query_recursive(start, mid, l, r, 2 * node + 1) + self._query_recursive(mid + 1, end, l, r, 2 * node + 2)

