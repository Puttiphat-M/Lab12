# def binsearch(dataList, key):
#     first = 0
#     count = len(dataList)
#     while 0 < count:
#         step = count / 2
#         mid = first + step
#
#         if dataList[mid] > key:
#             mid += 1
#             first = mid
#             count -= step + 1
#         else:
#             count = step
#
#     return first

class InvalidArgument(Exception): pass


def binsearch(dataList, key):
    if not isinstance(dataList, list):
        raise InvalidArgument("dataList is not a list")

    for i in dataList:
        if not isinstance(i, int):
            raise InvalidArgument(f"{i} is not an integer")

    first = 0
    count = len(dataList)
    while 0 < count:
        step = count // 2
        mid = first + step

        if dataList[mid] < key:
            mid += 1
            first = mid
            count -= step + 1
        elif dataList[mid] > key:
            count = step
        else:
            return mid

    return None


if __name__ == "__main__":
    knownValues = ((((10, 20, 30), 20), 1),
                   (((10, 20, 30), 30), 2),
                   (((10, 20, 30), 5), None),
                   (((10, 30, 50, 60, 70), 50), 2),
                   (((10, 20, 30, 40, 70, 80), 80), 5),
                   (((10, 20, 30, 50, 60, 90), 30), 2),
                   (((10, 30, 50, 80, 90), 30), 1),
                   (((10, 40, 50, 60, 70, 80, 90, 100), 100), 7),
                   (((20, 30, 40, 60, 70), 20), 0),
                   (((30, 40, 50, 60), 5), None),
                   (((10, 20, 30, 30, 30), 30), 2),
                   (((10, 20, 30, 30, 30, 30), 30), 2),
                   (((20, 20, 20, 20), 20), 1),
                   (((20, 20, 20, 20, 20, 20), 20), 2),
                   (((10, 20, 30, 40, 50, 50, 60), 30), 2))

    for v, idx in knownValues:
        if idx is None:
            continue
        if v[0][binsearch(list(v[0]), v[1])] == v[0][idx]:
            print("yep")
        else:
            print(binsearch(list(v[0]), v[1]))
