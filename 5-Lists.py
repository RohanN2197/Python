players = [45,67,8,9,12]
print(players[2])
players[2] = 44
print(players)
players.append(78)
print(players)
print(players[0:3])
players[:2] = [0,0]
print(players)
players[:2] = [] #delete items from list
print(players)
players[:] = [] #deleting full list
print(players)
