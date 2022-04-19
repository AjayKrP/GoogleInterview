"""
1. have given profit & weight array
2. sort by profit/weight(P/E) in ascending order
3. Now select weight which has more P/E value with capacity <= max_capacity of sack
"""


def knapsack(profit, weight, max_capacity):
    pe = {}
    for i in range(len(profit)):
        pe[i] = profit[i] / weight[i]
    pe = sorted(pe.items(), key=lambda x: x[1], reverse=True)
    res = []
    curr_weight = 0
    max_profit = 0
    for item in pe:
        if curr_weight + weight[item[0]] <= max_capacity:
            res.append(weight[item[0]])
            curr_weight += weight[item[0]]
            max_profit += profit[item[0]]
    return res, curr_weight, max_profit


max_capacity = 15
pft = [10, 5, 15, 7, 6, 18, 3]
wght = [2, 3, 5, 7, 1, 4, 1]
print(knapsack(pft, wght, max_capacity))

val = [60, 100, 120]
wt = [10, 20, 30]
ttl = 50
print(knapsack(val, wt, ttl))
