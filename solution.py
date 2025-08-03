class Solution:
    # @param A: integer
    # @return an integer
    def findEnergy(self, A):
        if A == 1:
            return 0

        dp = [0] * (A + 1)

        for i in range(2, A + 1):
            dp[i] = i
            j = 2
            while j * j <= i:
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
                    dp[i] = min(dp[i], dp[i // j] + j)
                j += 1

        return dp[A]
