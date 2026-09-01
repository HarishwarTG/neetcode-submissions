import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        slow = 0
        fleet = 0
        cars = sorted(zip(position, speed), reverse = True)

        for p, s in cars:
            time = (target - p) / s

            if time > slow:
                fleet += 1
                slow = time

        return fleet 
