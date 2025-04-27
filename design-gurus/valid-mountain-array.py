def is_mountain(arr):
    if len(arr) <= 2:
        return False

    is_increasing = True
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return False
        if is_increasing and arr[i] > arr[i - 1]:
            continue
        if is_increasing and arr[i] < arr[i - 1]:
            is_increasing = False
            continue
        if not is_increasing and arr[i] >= arr[i - 1]:
            return False
    return True
