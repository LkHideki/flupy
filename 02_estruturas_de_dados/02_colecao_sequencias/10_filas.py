from collections import deque

dq = deque([3, 2, 4, 5, "a", False, 19])

dq.extend(dq)
dq.rotate(2)
dq.pop()
dq.popleft()



