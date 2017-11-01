def min_distance(w1, w2):
    len1 = len(w1)
    len2 = len(w2)
    dis = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    for i in range(len1 + 1):
        dis[0][i] = i
    for j in range(len2 + 1):
        dis[j][0] = j
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if w1[j - 1] == w2[i - 1]:
                dis[i][j] = dis[i - 1][j - 1]
            else:
                dis[i][j] = min(dis[i - 1][j - 1], min(dis[i - 1][j], dis[i][j - 1])) + 1
    print dis
    return dis[len2][len1]


print min_distance('bee', 'deep')
