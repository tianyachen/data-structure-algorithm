class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_indices = sorted(range(len(position)), key = lambda i : -position[i])

        sorted_position = [position[i] for i in sorted_indices]
        sorted_speed = [speed[i] for i in sorted_indices]

        times = [(target - pos) / s for pos, s in zip(sorted_position, sorted_speed)]

        stack = []

        for time in times:
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)

        return len(stack)