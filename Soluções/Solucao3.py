import bisect

class Solution:
    def maxTwoEvents(self, events):
        # Ordena eventos por tempo de início
        events.sort(key=lambda x: x[0])

        # Lista só com (endTime, value) para busca binária e dp
        end_events = sorted([(e[1], e[2]) for e in events], key=lambda x: x[0])

        ends = [e[0] for e in end_events]
        values = [0] * len(end_events)
        # Preprocessar para dp: values[i] é o máximo valor até o evento i (ordenado por endTime)
        max_val = 0
        for i, (end, val) in enumerate(end_events):
            max_val = max(max_val, val)
            values[i] = max_val

        ans = 0
        for start, end, val in events:
            # Busca índice do último evento que termina antes do start atual (end[j] < start)
            idx = bisect.bisect_left(ends, start) - 1
            if idx >= 0:
                ans = max(ans, val + values[idx])
            else:
                ans = max(ans, val)

        return ans