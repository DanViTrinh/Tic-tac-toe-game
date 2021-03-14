# creating a tic tac toe pvp game to put in main game later.

#layout of board and intro
line1 = "     |     |     "
line2 = "  1  |  2  |  3  "
line3 = "-----|-----|-----"
line4 = "  4  |  5  |  6  "
line5 = "-----|-----|-----"
line6 = "  7  |  8  |  9  "
line7 = "     |     |     "


print("Tic Tac Toe PvP")
print("Chose spacing between guide and game (recommended spacing number = 10)")
n = input("Spacing number: ")

space = str(int(n)*" ") #spacing number

print("         ")
print("     |     |     ")
print("  1  |  2  |  3  ")
print("-----|-----|-----")
print("  4  |  5  |  6  ")
print("-----|-----|-----")
print("  7  |  8  |  9  ")
print("     |     |     ")
print("Insert number to play pvp")

# creating a function for board
cords = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def board():
    print("         ")
    print("     |     |     "+space+line1)
    print("  " + cords[0] + "  |  " + cords[1] + "  |  " + cords[2] + "  "+space+line2)
    print("-----|-----|-----"+space+line3)
    print("  " + cords[3] + "  |  " + cords[4] + "  |  " + cords[5] + "  "+space+line4)
    print("-----|-----|-----"+space+line5)
    print("  " + cords[6] + "  |  " + cords[7] + "  |  " + cords[8] + "  "+space+line6)
    print("     |     |     "+space+line7)

# creating function for x move/p1
def move_x():
    move = input("p1 move: ")

    if move == "1":
        cords[0] = "X"
    if move == "2":
        cords[1] = "X"
    if move == "3":
        cords[2] = "X"
    if move == "4":
        cords[3] = "X"
    if move == "5":
        cords[4] = "X"
    if move == "6":
        cords[5] = "X"
    if move == "7":
        cords[6] = "X"
    if move == "8":
        cords[7] = "X"
    if move == "9":
        cords[8] = "X"

    board()
    #condition for winning
    if cords[0] == "X" and cords[1] == "X" and cords[2] == "X" \
            or cords[3] == "X" and cords[4] == "X" and cords[5] == "X" \
            or cords[6] == "X" and cords[7] == "X" and cords[8] == "X" \
            or cords[0] == "X" and cords[4] == "X" and cords[8] == "X" \
            or cords[2] == "X" and cords[4] == "X" and cords[6] == "X" \
            or cords[0] == "X" and cords[3] == "X" and cords[6] == "X" \
            or cords[1] == "X" and cords[4] == "X" and cords[7] == "X" \
            or cords[2] == "X" and cords[5] == "X" and cords[8] == "X" :
        print("p1 wins!")
        quit()

# creating function for O move/p2
def move_o():
    move = input("p2 move: ")

    if move == "1":
        cords[0] = "O"
    if move == "2":
        cords[1] = "O"
    if move == "3":
        cords[2] = "O"
    if move == "4":
        cords[3] = "O"
    if move == "5":
        cords[4] = "O"
    if move == "6":
        cords[5] = "O"
    if move == "7":
        cords[6] = "O"
    if move == "8":
        cords[7] = "O"
    if move == "9":
        cords[8] = "O"

    board()

    #condition for O winning
    if cords[0] == "X" and cords[1] == "X" and cords[2] == "X" \
            or cords[3] == "O" and cords[4] == "O" and cords[5] == "O" \
            or cords[6] == "O" and cords[7] == "O" and cords[8] == "O" \
            or cords[0] == "O" and cords[4] == "O" and cords[8] == "O" \
            or cords[2] == "O" and cords[4] == "O" and cords[6] == "O" \
            or cords[0] == "O" and cords[3] == "O" and cords[6] == "O" \
            or cords[1] == "O" and cords[4] == "O" and cords[7] == "O" \
            or cords[2] == "O" and cords[5] == "O" and cords[8] == "O" :
        print("p2 wins!")
        quit()

#p1 move 1
move_x()

#p2 move 1
move_o()

#p1 move 2
move_x()

#p2 move 2
move_o()

#p1 move 3
move_x()

#p2 move 3
move_o()

#p1 move 4
move_x()

#p2 move 4
move_o()

#p1 move 5
move_x()

print("Draw! ")
quit()

















