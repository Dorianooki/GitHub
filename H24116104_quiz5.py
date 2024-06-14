#輸入盤面大小
size = input("Enter the size of the grid:")

#建立盤面
grid = []
i = 0
while i < int(size):
    print("_")

grid_str = ""
i = 0
while i < int(size):
    row = grid[i:int(size)+1]
    grid_str += " ".join(row) + "\n"
    i += int(size)
print(grid_str)

#讓使用者輸入盤面相關值
while True:
    cc = input("Enter the cell coordinates to edit:")
    row, col = map(cc.split('.'))
    v = input("Enter the value for the cell:")



    if v == "done":
        break

























