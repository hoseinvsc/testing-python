#771: Jewels and Stones,Leetcode.com
def JewelsStones(J, S):
    count = 0
    for stone in S:
        if stone in J:
            count += 1
    return count

J = "aA"
S = "aAAAA"
result = JewelsStones(J, S)
print(result)
