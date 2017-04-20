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

        if param is array[upper - 1]:
            return {"count": count, "index": upper - 1}
        if param is array[lower]:
            return {"count": count, "index": lower}

        while lower < upper:
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
            count += 1
        return {"count": count - 1, "index": -1}
