def knapsack(items, weight_limit):
    if weight_limit <= 0:
        return 0
    if len(items)==1:
        if weight_limit>=items[0][0]:
            return items[0][1]
        else:
            return 0
    
    if(items[-1][0]>weight_limit):
        return knapsack(items[:-1], weight_limit)
    else:
        return max(knapsack(items[:-1], weight_limit), knapsack(items[:-1], weight_limit-items[-1][0]) + items[-1][1])


#input = list of (weight, value) of each item
items = [[2,7], [1,1], [2,6], [5,18], [6,22], [7,28]]
weight_lim = 15
print(knapsack(items, weight_lim))