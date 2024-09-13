from collections import deque

queue = deque([1,2,'hola',])
queue.popleft()
queue.append(12)
lista1 = queue[1]
print(lista1)
