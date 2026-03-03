from collections import deque

TOTAL_M = 3
TOTAL_C = 3

# Check if state is valid
def is_valid(state):
    M_left, C_left, boat = state
    M_right = TOTAL_M - M_left
    C_right = TOTAL_C - C_left

    if M_left < 0 or C_left < 0 or M_left > TOTAL_M or C_left > TOTAL_C:
        return False

    if M_left > 0 and C_left > M_left:
        return False

    if M_right > 0 and C_right > M_right:
        return False

    return True


# Generate possible moves
def get_next_states(state):
    M_left, C_left, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    next_states = []

    for m, c in moves:
        if boat == 1:  # Boat on left
            new_state = (M_left - m, C_left - c, 0)
        else:  # Boat on right
            new_state = (M_left + m, C_left + c, 1)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states


# BFS
def bfs():
    visited = set()
    queue = deque([((3,3,1), [])])

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == (0,0,0):
            print("BFS Solution:")
            for step in path:
                print(step)
            print("Nodes explored:", len(visited))
            return

        for next_state in get_next_states(state):
            queue.append((next_state, path))


# DFS
def dfs():
    visited = set()
    stack = [((3,3,1), [])]

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == (0,0,0):
            print("DFS Solution:")
            for step in path:
                print(step)
            print("Nodes explored:", len(visited))
            return

        for next_state in get_next_states(state):
            stack.append((next_state, path))


if __name__ == "__main__":
    bfs()
    print("-------------------")
    dfs()
