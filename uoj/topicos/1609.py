cases = int(input())

for i in range(cases):
    trash = input()
    unique = {}
    nums = input().split(' ')
    for j in range(len(nums)):
        num = int(nums[j])
        if not unique.get(num):
            unique[num] = True
    
    print(len(unique))
