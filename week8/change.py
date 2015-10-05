def change(goal_sum, coins):
    sums = [0 for x in range(goal_sum + 1)]
    sums[0] = 1
    for j in coins:
        for i in range(goal_sum + 1):
            if i + j <= len(sums) - 1:
                sums[i + j] += sums[i]

    return sums[goal_sum]
print(change(25, [1, 2, 5, 10, 20, 50, 100]))
