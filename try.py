class WrappedList(list):
    def __init__(self):
        super(WrappedList, self).__init__(self.list)

    def __getitem__(self, item):
        return self.list[item]

w = WrappedList()
print(w[1])