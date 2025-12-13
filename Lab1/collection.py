from collections import deque

queue = deque()

elements = [5, 1, 3, 2, 4]

for element in sorted(elements):
    queue.append(element)

print("Erembelsen daraalal:", queue)
