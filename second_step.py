class SecondStep:

    # Complete list of coordinates
    complete_coord = []

    def __init__(self, maze):
        self.maze = maze

    def print_output(self):
        print()
        for i in range(len(self.maze) * 2): print("=", end = "")
        
        print()
        print()
        print("0: Empty cell")
        print("1: Block")
        print("9: Path to follow")
        print("B. Cells in which you cannot move, aka 'Black Holes'")
        print()
        print()
            
        for i in self.maze:
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

        print("!!! ERROR !!!")
        print()
        print("Could not find a valid cell around position with values:")
        print("X: " + str(current_x))
        print("Y: " + str(current_y))
        print()
        print("Aborting...")

        raise Exception()
    
    def __on_new_move(self, x, y):
        self.complete_coord.append([x, y])
        self.maze[y][x] = 9
    
    def __is_valid_cell(self, x, y):
        is_within_wall = x < len(self.maze[0]) and y < len(self.maze) \
               and x > -1 and y > -1
        if not is_within_wall: return False

        already_visited = [x, y] in self.complete_coord
        if already_visited: return False
        
        return self.maze[y][x] == 'X'
        
