import random
User=input("enters players name sepearted by comma:")
players=User.split(",")
print("so your total no. of players :")
print(len(players))
first=random.choice(players)
print("who will play first")
print(first)
players.remove(first)

second=random.choice(players)
print("who will play second")
print(second)
players.remove(second)

third=random.choice(players)
print("who will play third")
print(third)
players.remove(third)

fourth=random.choice(players)
print("who will play fourth")
print(fourth)
players.remove(fourth)

fifth=random.choice(players)
print("who will play fifth")
print(fifth)
players.remove(fifth)

sixth=random.choice(players)
print("who will play sixth")
print(sixth)
players.remove(sixth)

seventh=random.choice(players)
print("who will play seventh")
print(seventh)
players.remove(seventh)

eight=random.choice(players)
print("who will play eighth")
print(eight)
players.remove(eight)

nineth=random.choice(players)
print("who will play nineth")
print(nineth)
players.remove(nineth)

tenth=random.choice(players)
print("who will play tenth")
print(tenth)
players.remove(tenth)

eleventh=random.choice(players)
print("who will play eleventh")
print(eleventh)
players.remove(eleventh)

print("no. players left")
print(len(players))
print(players)