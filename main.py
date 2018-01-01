from first_step import FirstStep
from second_step import SecondStep

def print_coordinates(coordinates):
    print("X: " + str(coordinates[1]) + ", "  + "Y: " + str(coordinates[0]))

maze = [
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0]
]

init_x = 1
init_y = 0

end_x = 7
end_y = 7

current_coord = [init_y, init_x]

######### FIRST STEP #########
    
first_step = FirstStep(maze)
first_step.complete_coord.append([current_coord[1], current_coord[0]])

print_coordinates(current_coord)
while (current_coord[0] != end_y or current_coord[1] != end_x):
    current_coord = first_step.compute_next_move(current_coord[1], current_coord[0], end_x, end_y)
    print_coordinates(current_coord)
    
first_step.print_output()

first_step_output = first_step.maze_output

######### SECOND STEP #########

current_coord = [init_y, init_x]
second_step = SecondStep(first_step_output)
second_step.complete_coord.append([current_coord[1], current_coord[0]])

print_coordinates(current_coord)
while (current_coord[0] != end_y or current_coord[1] != end_x):
    current_coord = second_step.compute_next_move(current_coord[1], current_coord[0], end_x, end_y)
    print_coordinates(current_coord)

second_step.print_output()
