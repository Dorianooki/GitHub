import random

def generate_path(N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly. Exceptions for TypeError 
    # and KeyError are handled.

    # your code here
    #先做出地圖
    maze = {}
    #將地圖裡面塞滿0
    for i in range(N):
        for j in range(M):
            maze[(i, j)] = 0
    #開頭和起點設為2
    maze[(0, 0)] = 2
    maze[(N-1, M-1)] = 2
    current_position = (0, 0)
    #設置路徑 並設為2
    while current_position != (N-1, M-1):
        next_moves = []
        if current_position[0] < N - 1:
            next_moves.append((current_position[0] + 1, current_position[1]))
        if current_position[1] < M - 1:
            next_moves.append((current_position[0], current_position[1] + 1))
        next_position = random.choice(next_moves)
        maze[next_position] = 2
        current_position = next_position
    return maze



def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.

    # your code here
    #檢查迷宮中為0的點
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze[(i, j)] == 0]
    obstacles_added = 0
    #隨機設置障礙
    while obstacles_added < min_obstacles:
        try:
            cell = random.choice(empty_cells)
            maze[cell] = 1
            empty_cells.remove(cell)
            obstacles_added += 1
        except KeyError:
            print("Error: Failed to set obstacle at", cell)


def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    try:
        #輸入要設定障礙的點
        obs = input ("Enter the coordinates to set a obstacle(i,j): ")
        i = int(obs.split(",")[0])
        j = int(obs.split(",")[1])
        #檢查有沒有超出範圍
        if i < 0 or i >= N or j < 0 or j >= M:
            raise KeyError("Please input coordinates within range.")
        #檢查有沒有在路徑上
        if maze[(i, j)] == 2:
            print("Error: Cannot set obstacle on the path.")
        #檢查有沒有障礙
        elif maze[(i, j)] == 1:
            print("Error: Obstacle already present in the specified cell.")
        #設置障礙
        else:
            maze[(i, j)] = 1
            print("Obstacle set successfully.")
    
    except ValueError:
        print("ValueError in set_obstacle function: Need to be coordinates.")
    
    except KeyError as e:
        print("KeyError in set_obstacle function:", str(e))


def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    try:
        #輸入移除障礙的點 內容與上面設置障礙一樣
        obs = input ("Enter the coordinates to set a obstacle(i,j): ")
        i = int(obs.split(",")[0])
        j = int(obs.split(",")[1])
        
        if i < 0 or i >= N or j < 0 or j >= M:
            raise KeyError("Please input coordinates within range.")
        
        if maze[(i, j)] == 2:
            print("Error: Cannot remove obstacle from the path.")
        elif maze[(i, j)] == 0:
            print("Error: No obstacle present in the specified cell.")
        else:
            maze[(i, j)] = 0
            print("Obstacle removed successfully.")
    
    except ValueError:
        print("ValueError in set_obstacle function: Need to be coordinates.")
    
    except KeyError as e:
        print("KeyError in set_obstacle function:", str(e))


def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells. If a KeyError occurs while trying to access a cell, it is 
    # caught and a message is printed.

    # your code here
    #印出地圖
    for i in range(N):
        for j in range(M):
            try:
                cell = maze[(i, j)]
                if cell == 0:
                    print('   ', end='')
                elif cell == 1:
                    print(' X ', end='')
                elif cell == 2:
                    print(' O ', end='')
            except KeyError:
                print('Error: Cell not found.', end='')
        print()



def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.

    # your code here
    while True:
        try:
            #輸入地圖名稱
            F = input("Enter the file name:")
            with open("F", 'r') as file:
                if F == "grid77.txt":
                    N = 7
                    M = 7
                if F == "grid99.txt":
                    N = 9
                    M = 9
            #最小障礙物
            min_obstacles = int(input("Enter the minimum number of obstacles: "))
            maze = generate_path(N, M)
            add_obstacles(maze, min_obstacles, N, M)
            #主要輸入用的東東
            while True:
                print("\nMenu:")
                print("1. Set obstacle")
                print("2. Remove obstacle")
                print("3. Print maze")
                print("4. Exit")
                choice = input("Enter your choice (1-4): ")
                if choice == '1':
                    set_obstacle(maze, N, M)
                elif choice == '2':
                    remove_obstacle(maze, N, M)
                elif choice == '3':
                    print("Current maze:")
                    print_maze(maze, N, M)
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("ValueError occured in main function: Invalid input.")
        except IOError:
            print("IOError occured in main function: File not found Please input a vaild file name.")
        except NameError:
            print("NameError occured in main function: Maze dimensions not specified.")
    
main()
