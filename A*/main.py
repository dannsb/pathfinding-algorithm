from heapq import heappop, heappush
from time import time

graph = {
    "Shiraz": {"Isfahan": 450, "Ahvaz": 520},
    "Isfahan": {"Shiraz": 450, "Ahvaz": 480, "Yazd": 320, "Qom": 220},
    "Ahvaz": {"Shiraz": 520, "Isfahan": 480},
    "Yazd": {"Isfahan": 320, "Qom": 340},
    "Qom": {"Isfahan": 220, "Yazd": 340, "Tehran": 150},
    "Tehran": {"Qom": 150},
}

heuristic = {
    "Shiraz": 900,
    "Isfahan": 340,
    "Yazd": 400,
    "Ahvaz": 650,
    "Qom": 150,
    "Tehran": 0,
}


priorityQueue = []
targetNode = "Tehran"
initNode = "Shiraz"
initH = heuristic[initNode]
initF = 0 + initH
initG = 0
visited = []

heappush(
    priorityQueue,
    (
        initF,
        initNode,
        initG,
    ),
)

startTime = time()
while priorityQueue:
    # heappop() : Pop the smallest item based on first element by default
    f, activeNode, g = heappop(priorityQueue)

    if activeNode in visited:
        continue

    visited.append(activeNode)

    if activeNode == targetNode:
        break

    for nearCity, distance in graph[activeNode].items():
        if nearCity not in visited:
            newG = g + distance
            h = heuristic[nearCity]
            f = newG + h
            heappush(
                priorityQueue,
                (
                    f,
                    nearCity,
                    newG,
                ),
            )

endTime = time()

print(f"Time taken: {endTime - startTime:.10f} seconds")
print(f"Route-> {visited}")
