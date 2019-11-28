def getSkyline(buildings):
    if not buildings: return []
    if len(buildings) == 1:
        return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
    mid = len(buildings) // 2
    left = getSkyline(buildings[:mid])
    right = getSkyline(buildings[mid:])
    return merge(left, right)

def merge(left, right):
    # 记录目前左右建筑物的高度
    lheight = rheight = 0
    # 位置
    l = r = 0
    res = []
    while l < len(left) and r < len(right):
        if left[l][0] < right[r][0]:
            cp = [left[l][0], max(left[l][1], rheight)]
            lheight = left[l][1]
            l += 1
        elif left[l][0] > right[r][0]:
            cp = [right[r][0], max(right[r][1], lheight)]
            rheight = right[r][1]
            r += 1
        else:
            cp = [left[l][0], max(left[l][1], right[r][1])]
            lheight = left[l][1]
            rheight = right[r][1]
            l += 1
            r += 1
        # 和前面高度比较，不一样才加入
        if len(res) == 0 or res[-1][1] != cp[1]:
            res.append(cp)
        # 剩余部分添加进去
    res.extend(left[l:] or right[r:])
    return res

print(getSkyline([[1,5,11], [2,7,6], [3,9,13], [12,16,7], [14,25,3], [19,22,18], [23,29,13],[24,28,4]]))