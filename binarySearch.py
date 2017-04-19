class BinarySearch(list):
    def __init__(self, a, b):
        self.array = [x for x in range(0, a, b)]
        self.length = len(self.array)

    def search(self, param):
        print(self.array)
        result = {}
        high = self.length
        low = 0
        count = 0

        while low < high:
            count += 1
            half = (high + low) // 2
            if self.array[half] < param:
                low = half + 1
            else:
                high = half
            if self.array[low] == param:
                return {"count": count, "index": low}
            elif self.array[low] != param:
                continue
        return {"count": count, "index": None}

mySearch = BinarySearch(10000, 2)
print(mySearch.search(3))
