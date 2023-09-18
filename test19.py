def target_founder(h,t):
    target = 0
    for hour in h:
        if hour >= t:
            target += 1
    return target


result = target_founder([0,1,2,3,4],2)
print(result)