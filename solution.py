class Solution:
    #@param A: list of integers
    #@param B: integer
    #@return an integer
    def solve(self, A, B):
        max1 = 0
        max2 = 0
        for x in A:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x

        if B <= max1:
            return 1

        total_damage_per_two_moves = max1 + max2

        num_cycles = B // total_damage_per_two_moves
        remaining_health = B % total_damage_per_two_moves

        if remaining_health == 0:
            return 2 * num_cycles
        elif remaining_health <= max1:
            return 2 * num_cycles + 1
        else:
            return 2 * num_cycles + 2
