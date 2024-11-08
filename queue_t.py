import queue

q = queue.PriorityQueue()
q.put(3)
q.put(1)
q.put(2)

print(q.get())
print(q.get())
print(q.get())
