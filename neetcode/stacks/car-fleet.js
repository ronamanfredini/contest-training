// URL - https://neetcode.io/problems/car-fleet

/**
initialize all fleets

each fleet has its own speed

iterate over the array of fleets
    update their positions according to the speed
    if some fleet reached the position of another fleet, they become the same fleet
    if the fleet reached the destination, pop from te fleet array and increemnt the fleetcounter
 */


class Fleet {
    speed
    position
    cars

    constructor(speed, position, cars) {
        this.speed = speed
        this.position = position
        this.cars = cars
    }
}

class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        const fleets = [];
        let fleetCount = 0;
        for (let i = 0; i < position.length; i++) {
            const fleet = new Fleet(speed[i], position[i], 1);
            fleets.push(fleet)
        }

        while (fleets.length > 0) {
            for (let i = 0; i < fleets.length; i++) {
                const fleet = fleets[i];
                fleet.position += fleet.speed;

                const fleetAhead = fleets[i + 1];
                if (fleetAhead) {
                    if (fleet.position >= fleetAhead.position) {
                        fleetAhead.cars += fleet.cars;
                        fleets.splice(i, 1);
                        i--;
                        continue;
                    }
                }

                if (fleet.position >= target) {
                    fleets.splice(i, 1);
                    i--;
                    fleetCount++;
                    continue;
                }
            }
        }

        return fleetCount
    }
}

// const target = 10, position = [1,4], speed = [3,2];
const target = 10, position = [4,1,0,7], speed = [2,2,1,1]

const s = new Solution();

console.log(s.carFleet(target, position, speed))