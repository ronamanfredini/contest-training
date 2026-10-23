def sol(nums):
    pairs = {}
    triplets = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue

            key = (nums[i] + nums[j]) * -1
            arr = pairs.get(key)
            if not arr:
                arr = set()
                arr.add(i)
                arr.add(j)
                pairs[key] = arr
    
    for i in range(len(nums)):
        if nums[i] in pairs:
            if i not in pairs[nums[i]]:
                pairs[nums[i]].add(i)
                if len(pairs[nums[i]]) == 3:
                    i, j, k = tuple(pairs[nums[i]])
                    triplets.add((nums[i], nums[j], nums[k]))

    return triplets




print(sol([-1,0,1,2,-1,-4]))