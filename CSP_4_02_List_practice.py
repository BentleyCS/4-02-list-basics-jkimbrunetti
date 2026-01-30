
def bookends(li: list):
    first = li.pop(0)
    last = li.pop(len(li) - 1)
    return [first, last]

def inOrder(li : list):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False
    return True



def find(li: list, target : int):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1


def removeLowest(li):
    lowest_index = 0
    for i in range(1, len(li)):
        if li[i] < li[lowest_index]:
            lowest_index = i
    li.pop(lowest_index)
    return li


def keepOrder(li: list, value):
    inserted = False
    for i in range(len(li)):
        if value <= li[i]:
            li.insert(i, value)
            inserted = True
            break
    if not inserted:
        li.append(value)
    return li


def merge(l1:list, l2:list):
    return sorted(l1+l2)
