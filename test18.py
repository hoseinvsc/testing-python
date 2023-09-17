def JewelsStones(J, S):
    count = 0
    for stone in S:
        if stone in J:
            count += 1
    return count

J = "aA"
S = "aAAbbbb"
result = JewelsStones(J, S)
print(result)
