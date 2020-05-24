count, length = list(map(int, input().strip().split(" ")))
lights = sorted(list(map(int, input().strip().split(" "))))

dists = []
for i in range(count-1):
    dist = lights[i+1] - lights[i]
    dists.append(dist/2)
dists.append(lights[0])
dists.append(length - lights[-1])

print("%.2f" % (sorted(dists)[-1]))
