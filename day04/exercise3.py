# A treasure map

map = [
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️']
]
row1, row2, row3 = map[0], map[1], map[2]
print(f"{row1}\n{row2}\n{row3}")
spot = input("Where do you want to put the treasure? ")
column = int(spot[0])
row = int(spot[1])
map[row - 1][column - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
