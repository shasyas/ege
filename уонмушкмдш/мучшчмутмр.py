def which_cluster(point, task):
    x, y = point
    match task:
        case 1:
            return 6 * y - 7 * x > 6
        case 2:
            if x > 7 and y < 6:
                return 0
            elif 9 * x + 7 * y > 63:
                return 1
            return 2

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


base = ''
files = ['27a.txt', '27b.txt']
nums_cls = [2, 3]

for task in (1, 2):
    fd = open(base + files[task-1])
    fd.readline()
    clusters = [[], [], []]
    num_cl = nums_cls[task-1]

    for line in fd:
        point = [float(d) for d in line.replace(',', '.').split()]
        clusters[which_cluster(point, task)].append(point)

    centers = []
    for i in range(num_cl):
        dmin = 10**1000
        for p in clusters[i]:
            d = sum(dist(p, p1) for p1 in clusters[i])
            if d < dmin:
                c = p
                dmin = d
        centers.append(c)
    px = sum(p[0] for p in centers) / 2 * 10000
    py = sum(p[1] for p in centers) / 2 * 10000
    print(int(px), int(py))