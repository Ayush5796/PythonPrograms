from collections import deque

list = ['a','b','c','d']
deq = deque(list)
print(deq)

deq.append('e')
print(deq)
deq.popleft()
print(deq)
print(deq.clear())