def straight_merge(container):
    if len(container) < 2:
        return container[:]
    else:
        middle = int(len(container) / 2)
        left = straight_merge(container[:middle])
        right = straight_merge(container[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i].relation() < right[j].relation():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result