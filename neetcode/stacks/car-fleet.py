class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleet_count = 0
        sorted_fleet = []
        
        for i in range(len(position)):
            t = [position[i], speed[i]]
            sorted_fleet.append(t)

        sorted_fleet = sorted(sorted_fleet, key=lambda x: x[0])

        while len(sorted_fleet) > 0:
            reached_destination = False
            for i in range(len(sorted_fleet) -1, -1, -1):
                if i == len(sorted_fleet) - 1:
                    sorted_fleet[i][0] += sorted_fleet[i][1]
                    if sorted_fleet[i][0] >= target:
                        reached_destination = True
                        sorted_fleet.pop()
                else:
                    sorted_fleet[i][0] += sorted_fleet[i][1]
                    if sorted_fleet[i][0] >= sorted_fleet[i + 1][0]:
                        sorted_fleet.pop(i)
                
            if reached_destination:
                fleet_count += 1

        return fleet_count



s = Solution()
# print(s.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))
print(s.carFleet(target=10,position=[8,3,7,4,6,5],speed=[4,4,4,4,4,4]))


# print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # Output: 3
# print(s.carFleet(10, [1, 4],[3,2]))