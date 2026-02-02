from collections import deque

def sol(students, sandwiches):
    student_queue = deque(students)
    sandwich_stack = deque(sandwiches)
    
    failed = 0
    
    while student_queue:
        if student_queue[0] == sandwich_stack[0]:
            student_queue.popleft()
            sandwich_stack.popleft()
            failed = 0
        else:
            student_queue.append(student_queue.popleft())
            failed += 1
        if failed == len(student_queue):
            break
            
    return len(student_queue)


# Example usage:
print(sol([1,1,0,0], [0,1,0,1]))  # Output: 0
print(sol([1,1,1,0,0,1], [1,0,0,0,1,1]))  # Output: 3
