# https://leetcode.com/problems/car-fleet/
# this problem is not about speed or distance it's about the time.
# if a car is behind a car which can reach the destination before the previous car than its considers as a fleet because of the description.
# we want to find the distinct fleet among the cars.

def sol(positions, speed, target):
    speed_cars = sorted(zip(positions, speed), reverse=True)
    max_fleets = 0
    max_time = 0

    for p, s in speed_cars:
        time = (target - p)/s  # time takes to reach the destination

        if time > max_time:  # compare whether curr car can join the fleet or not, if not it's a new fleet
            max_fleets += 1
            max_time = time  # update the time of new fleet

    return max_fleets

