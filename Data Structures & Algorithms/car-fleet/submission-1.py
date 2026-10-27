class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        max_time = 0
        sorted_position_speed = sorted(zip(position,speed), reverse=True)
        for pos, spd in sorted_position_speed:
            time_needed = (target - pos) / spd
            if time_needed > max_time:
                max_time = time_needed
                fleets += 1
        return fleets
        
