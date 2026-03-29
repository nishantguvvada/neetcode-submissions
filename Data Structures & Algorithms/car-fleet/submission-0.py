class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [(p, s) for p, s in zip(position, speed)]
        sorted_speed = sorted(fleets, reverse=True, key=lambda x: x[0])
        time = [(target - p) / s for p, s in sorted_speed]
        stack = []
        fleet = 0
        for t in time:
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)