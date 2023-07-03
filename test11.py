a = int(input())
b = [int(i) for i in input().split(" ")]
player = []
for i in range (0,len(b)):
    player.append(int(b[i]))

counter = 0
for i in range(0,len(player)):
    if player[i]==0 or player[i]==1 or player[i]==2:
        counter += 1
print("You can make",int(counter/3),"team with this conditions!")
