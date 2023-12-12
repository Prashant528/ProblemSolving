def feedDog(hunger_level, biscuit_size):
    biscuit_size.sort()
    hunger_level.sort()
    i = 0
    j = 0
    count = 0
    while i < len(hunger_level) and j < len(biscuit_size):
        if hunger_level[i] <= biscuit_size[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

hunger_level = [1,2,3]
biscuit_size = [1,1]
print(feedDog(hunger_level, biscuit_size))

hunger_level = [1,2]
biscuit_size = [1,2,3]
print(feedDog(hunger_level, biscuit_size))

hunger_level = [5,8,9]
biscuit_size = [4,6,7,8]
print(feedDog(hunger_level, biscuit_size))
