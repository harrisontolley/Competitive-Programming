class SegmentTree:
    def __init__(self, data):
        self.data = data
        # Use an identity value for multiplication
        self.tree = [1] * (4 * len(data))  

        if data:
            self.build(0, len(data) - 1, 0)

    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.data[start]
            return self.data[start]

        mid = (start + end) // 2
        # Store the product of the two halves in the node
        self.tree[node] = self.build(start, mid, 2 * node + 1) * self.build(mid + 1, end, 2 * node + 2)
        return self.tree[node]

    def update(self, idx, value):
        self._update_recursive(0, len(self.data) - 1, idx, value, 0)

    def query(self, start, end):
        return self._query_recursive(0, len(self.data) - 1, start, end, 0)

    def _update_recursive(self, start, end, idx, value, node):
        if start == end:
            self.data[idx] = value
            self.tree[node] = value
            return value

        mid = (start + end) // 2
        if idx <= mid:
            left_product = self._update_recursive(start, mid, idx, value, 2 * node + 1)
        else:
            left_product = self.tree[2 * node + 1]

        if idx > mid:
            right_product = self._update_recursive(mid + 1, end, idx, value, 2 * node + 2)
        else:
            right_product = self.tree[2 * node + 2]

        self.tree[node] = left_product * right_product
        return self.tree[node]

    def _query_recursive(self, start, end, l, r, node):
        if r < start or l > end:
            return 1  # Return the identity value

        if l <= start and r >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_product = self._query_recursive(start, mid, l, r, 2 * node + 1)
        right_product = self._query_recursive(mid + 1, end, l, r, 2 * node + 2)
        return left_product * right_product
