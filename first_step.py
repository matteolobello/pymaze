class FirstStep:

    # Complete list of coordinates
    complete_coord = []

    __black_holes = []

    def __init__(self, maze):
        self.maze = maze
        self.maze_output = maze

    def print_output(self):
        print()
        for i in range(len(self.maze) * 2): print("=", end = "")

        print()
        print()
        print("0: Empty cell")
        print("1: Block")
        print("X: Path to follow")
        print("B. Cells in which you cannot move, aka 'Black Holes'")
        print()
        print()
            
        for i in self.maze_output:
            for j in i:
                print(j, end = " ")
            print()

        print()            
        for i in range(len(self.maze) * 2): print("=", end = "")

        print()
        print()

    def compute_next_move(self, current_x, current_y, end_x, end_y):
        if self.__is_valid_cell(current_x, current_y + 1):
             self.__on_new_move(current_x, current_y + 1)
             return current_y + 1, current_x

        if self.__is_valid_cell(current_x + 1, current_y):
            self.__on_new_move(current_x + 1, current_y)
            return current_y, current_x + 1

        if self.__is_valid_cell(current_x, current_y - 1):
            self.__on_new_move(current_x, current_y - 1)
            return current_y - 1, current_x
            
        if self.__is_valid_cell(current_x - 1, current_y):
            self.__on_new_move(current_x - 1, current_y)
            return current_y, current_x - 1

        self.maze[current_y][current_x] = 'B'
        self.__black_holes.append([current_x, current_y])

        # Return previous position as we already analyzed
        # the countours and we could not do anything
        xy = self.complete_coord[len(self.complete_coord) - 1]

        self.complete_coord.pop()
        return xy[1], xy[0]
    
    def __on_new_move(self, x, y):
        self.complete_coord.append([x, y])
        self.maze_output[y][x] = 'X'
    
    def __is_valid_cell(self, x, y):
        is_within_wall = x < len(self.maze[0]) and y < len(self.maze) \
               and x > -1 and y > -1
        if not is_within_wall: return False

        already_visited = [x, y] in self.complete_coord
        if already_visited: return False

        is_block = self.maze[y][x] == 1
        if is_block: return False

        is_in_a_black_hole = [x, y] in self.__black_holes
        if is_in_a_black_hole: return False
        
        return True
