import math

def calculate_total_area(num_sets):
    # Calculate the area of a single square and a single triangle
    edge_length = 1  # Assuming the edge length is 1 unit
    square_area = edge_length ** 2
    triangle_area = (edge_length ** 2) * math.sqrt(3) / 4

    # Calculate the total area of all shapes
    total_area = num_sets * (2 * square_area + triangle_area)
    return total_area

def arrange_shapes(num_sets):
    # Calculate the total area of all shapes
    total_area = calculate_total_area(num_sets)

    # Initialize the grid dimensions
    grid_width = math.ceil(math.sqrt(total_area))
    grid_height = math.ceil(total_area / grid_width)

    # Initialize the grid
    grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

    # Arrange the shapes in the grid
    for i in range(num_sets):
        # Arrange two squares
        for j in range(2):
            x, y = find_empty_space(grid)
            grid[x][y] = 1  # Mark the space as occupied
            grid[x][y+1] = 1  # Mark the adjacent space as occupied

        # Arrange an equilateral triangle
        x, y = find_empty_space(grid)
        grid[x][y] = 2  # Mark the space as occupied

    return grid

def find_empty_space(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return None

def calculate_gap_area(grid):
    gap_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                gap_area += 1
    return gap_area

num_sets = 30
arrangement = arrange_shapes(num_sets)
gap_area = calculate_gap_area(arrangement)
print("Total gap area:", gap_area)