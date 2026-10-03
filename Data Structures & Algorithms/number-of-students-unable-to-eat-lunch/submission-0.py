from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        count = 0
        while len(q) > 0 and count < len(q):
            if q[0] == sandwiches[0]:
                q.popleft()
                sandwiches.pop(0)
                count = 0
            else:
                go_back = q.popleft()
                q.append(go_back)
                count += 1
        return len(sandwiches)
            