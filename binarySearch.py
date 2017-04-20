class BinarySearch(list):
    def __init__(self, a, b):
        self.array = [x for x in range(b, a * b + 1, b)]
        super(BinarySearch, self).__init__(self.array)
        self.length = len(self.array)

    def search(self, param):
        count = 0
        array = self.array
        lower = 0
        upper = len(array)

        while lower < upper:
            count += 1
            mid = lower + (upper - lower) // 2
            value = self.array[mid]
            if param == value:
                return {"count": count, "index": mid}
            elif param > value:
                if lower == mid:
                    break
                lower = mid
            else:
                upper = mid - 1
        return {"count": count, "index": -1}

mySearch = BinarySearch(100, 10)
print(mySearch)
print(mySearch.search(10000))

# elif param > self.array[upper - 1]:
#                     return {"count": count, "index": -1}