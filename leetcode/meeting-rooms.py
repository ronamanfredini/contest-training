def sol(meetings):
    meetings = sorted(meetings, key=lambda meeting: meeting[0])
    for i in range(len(meetings) - 1):
        meeting = meetings[i]
        next_meeting = meetings[i + 1]
        if meeting[1] > next_meeting[0]:
            return False
        
    return True

print(sol([[0, 30], [5, 10], [15, 20]]))
print(sol([[0, 4], [5, 10], [15, 20]]))
print(sol([[7,10], [2,4]]))