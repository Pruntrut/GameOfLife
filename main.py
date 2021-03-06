

def draw_cells(cell_list, world=(0, 0, 0, 0)):
    cell_world = create_world(cell_list)
    
    new_world = get_biggest_world(cell_world, world)

    # Print generation seperators
    print("\n", end="")
    for i in range(abs(new_world[0] - new_world[2]) + 1):
        print("%", end="")
    print("\n", end="")
    
    print("\n", end="")
    
    for i in range(new_world[1], new_world[3] + 1):
        cells_on_row = [cell for cell in cell_list if cell[1] == i]

        for j in range(new_world[0], new_world[2] + 1):
            if j in [cell[0] for cell in cells_on_row]:
                print("#", end="")
            else:
                print(".", end="")

        print("\n", end="")
        
    return new_world


def create_world(cell_list, padx=2, pady=2):
    max_x = max([cell[0] for cell in cell_list]) + padx
    min_x = min([cell[0] for cell in cell_list]) - padx
    max_y = max([cell[1] for cell in cell_list]) + pady
    min_y = min([cell[1] for cell in cell_list]) - padx

    return min_x, min_y, max_x, max_y


def get_biggest_world(world1, world2):
    new_world = [0] * 4

    # Get rightmost and leftmost x coords
    x_list = []

    for i in range(0, 4, 2):
        x_list.append(world1[i])
        x_list.append(world2[i])

    new_world[0] = min(x_list)
    new_world[2] = max(x_list)

    y_list = []

    for i in range(1, 4, 2):
        y_list.append(world1[i])
        y_list.append(world2[i])

    new_world[1] = min(y_list)
    new_world[3] = max(y_list)

    return new_world


def cell_near(comp_cell, update_cell):
    x = False
    y = False

    if update_cell[0] - 2 < comp_cell[0] < update_cell[0] + 2:
        x = True

    if update_cell[1] - 2 < comp_cell[1] < update_cell[1] + 2:
        y = True

    return x and y


def get_neighbours(update_cell):
    surrounding_cells = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            x = update_cell[0] + i
            y = update_cell[1] + j

            if (x, y) != update_cell:
                surrounding_cells.append((x, y))

    return surrounding_cells


def check_neighbours(update_cell, cell_list):
    neighbours = get_neighbours(update_cell)
    new_cell_list = []

    for c in neighbours:
        cells_around = [cell for cell in cell_list if cell_near(cell, c)]

        if len(cells_around) == 3 and c not in cell_list:
            new_cell_list.append(c)

    return new_cell_list


def update(cell_list):
    delete_cell_list = []
    create_cell_list = []

    for i, update_cell in enumerate(cell_list):
        cells_around = [cell for cell in cell_list if cell_near(cell, update_cell)]
        if len(cells_around) < 3:
            delete_cell_list.append(update_cell)
        elif len(cells_around) > 4:
            delete_cell_list.append(update_cell)

        create_cell_list.append(check_neighbours(update_cell, cell_list))

    # Delete dead cells
    new_cell_list = [cell for cell in cell_list if cell not in delete_cell_list]

    # Add new cells
    for list_of_cell_list in create_cell_list:
        for cell in list_of_cell_list:
            if cell not in new_cell_list:
                new_cell_list.append(cell)

    return new_cell_list


# --- Main ---
if __name__ == "__main__":

    cell_list = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
    world = draw_cells(cell_list)

    for i in range(30):
        print("Generation %d" % (i + 1))
        cell_list = update(cell_list)
        world = draw_cells(cell_list, world)
        print("World: ", world)

