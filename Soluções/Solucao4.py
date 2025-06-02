import bisect

class Solution:
    def maxTaxiEarnings(self, n, rides):
        # Ordena corridas pelo ponto final
        rides.sort(key=lambda x: x[1])

        # Extrai os pontos finais para busca binária
        ends = [ride[1] for ride in rides]
        dp = [0] * (len(rides) + 1)

        for i in range(1, len(rides) + 1):
            start, end, tip = rides[i - 1]
            profit = end - start + tip

            # Busca última corrida j com end[j] <= start[i]
            j = bisect.bisect_right(ends, start)  # posição que start poderia ser inserido
            dp[i] = max(dp[i - 1], dp[j] + profit)

        return dp[-1]