#tic tac toe game brain

#game layout


print("Tic Tac Toe")
print("Chose a number")
print("         ")
print("     |     |     ")
print("  1  |  2  |  3  ")
print("-----|-----|-----")
print("  4  |  5  |  6  ")
print("-----|-----|-----")
print("  7  |  8  |  9  ")
print("     |     |     ")


#coordinates


row = ["A","B","C"]
column = ["1","2","3"]



#person move

move = input("Enter a number: ")

#   conversion

if move == "1":
    move_row = 1
    move_column = 1

if move == "2":
    move_row = 1
    move_column = 2

if move == "3":
    move_row = 1
    move_column = 3

if move == "4":
    move_row = 2
    move_column = 1

if move == "5":
    move_row = 2
    move_column = 2

if move == "6":
    move_row = 2
    move_column = 3

if move == "7":
    move_row = 3
    move_column = 1

if move == "8":
    move_row = 3
    move_column = 2

if move == "9":
    move_row = 3
    move_column = 3

#end of conversion
#player move 1 - the hidden board



board = row[int(move_row)-1]+column[int(move_column)-1]



rowcord = board[0]
columncord = board[1]

#   layout "PAUSED HERE CONTINUE HERE"
space = "         "
vertical1 = "     |     |     "
line1 = "  "+A1+"  |  "+rowcord+columncord+"  |  "+rowcord+columncord+"  "
horizontal1 = ("-----|-----|-----")
line2 = ("  "+rowcord+columncord+"  |  "+rowcord+columncord+"  |  "+edge+"  ")
horizontal2 = ("-----|-----|-----")
line3 = ("  "+corner+"  |  "+edge+"  |  "+corner+"  ")
vertical2 = ("     |     |     ")



#player move 1 printout







#round 1 cpu
if rowcord == "A":
    cpurow = "left"

if rowcord == "B":
    cpurow = "center"

if rowcord == "C":
     cpurow = "right"

#column
if columncord == "1":
    cpucolumn = "top"

if columncord == "2":
    cpucolumn = "middle"

if columncord == "3":
    cpucolumn = "bottom"





