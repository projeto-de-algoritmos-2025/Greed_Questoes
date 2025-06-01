# Knapsack problem with jobs

import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        starts = [job[0] for job in jobs]
        ends = [job[1] for job in jobs]

        dp = [0] * (n + 1)  # dp[i]: lucro max considerando primeiros i jobs

        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            # Encontrar índice j onde jobs[j].end <= s, usando busca binária
            j = bisect.bisect_right(ends, s)  # pega posição onde s poderia ser inserido
            dp[i] = max(dp[i - 1], dp[j] + p)

        return dp[n]

        