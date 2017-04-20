class BinarySearch(list):
    def __init__(self, a, b):
        self.array = [x for x in range(b, a * b, b)]
        self.length = len(self.array)

    def search(self, param):
        count = 0
        print(self.array)

        array = self.array
        lower = 0
        upper = len(array)

        while lower < upper:
            try:
                count += 1
                mid = lower + (upper - lower) // 2
                value = self.array[mid]
                if param == value:
                    return {"count": count, "index": mid}
                elif param > value:
                    if lower == mid:
                        break
                    lower = mid + 1
                else:
                    upper = mid - 1
            except:
                break
        return {"count": count, "index": -1}
        # print(self.array)

mySearch = BinarySearch(100, 10)
print(mySearch.search(1000))

# elif param > self.array[upper - 1]:
#                     return {"count": count, "index": -1}