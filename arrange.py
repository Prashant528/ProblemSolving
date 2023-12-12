# def arrange(n):
#     if n==0 or n==1:
#         return 1
#     return arrange(n-1)+arrange(n-2)

def arrange(n, memo={}):
    if n in memo:
        return memo[n]
    elif n==0:
        memo[0] = 1
        return memo[0]
    elif n==1:
        memo[1] = 1
        return memo[1]
        
    memo[n] = arrange(n-1)+arrange(n-2)
    return memo[n]

print(arrange(4))