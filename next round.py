

# CodeForces A. Next Round solved by me

# Problem Link ====> https://codeforces.com/problemset/problem/158/A



passed = 0
places = input()
places = places.split()
players = places[0]
cut = places [1]

standings = input()
standings = standings.split()
points = standings[int(cut)-1]
points = int(points)
 

for p in standings:
    if int(p) >= points and int(p) > 0:
        passed = passed + 1
    
print(passed)

