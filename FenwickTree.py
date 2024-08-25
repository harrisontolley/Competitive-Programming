class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Move to the next index that i contributes to.

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index  # Move to the parent index.
        return sum

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)