def draw_cells(cell_list, padx=2, pady=2):

    max_x = max([cell[0] for cell in cell_list]) + padx
    min_x = min([cell[0] for cell in cell_list]) - padx
    max_y = max([cell[1] for cell in cell_list]) + pady
    min_y = min([cell[1] for cell in cell_list]) - padx

    for i in range(min_y, max_y+1):
        cells_on_row = [cell for cell in cell_list if cell[1] == i]

        for j in range(min_x, max_x+1):
            if j in [cell[0] for cell in cells_on_row]:
                print("#", end="")
            else:
                print(".", end="")

        print("\n", end="")


def cell_near(comp_cell, update_cell):
    x = False
    y = False

    if update_cell[0] - 2 < comp_cell[0] < update_cell[0] + 2:
        x = True

    if update_cell[1] - 2 < comp_cell[1] < update_cell[1] + 2:
        y = True

    return x and y


def update(cell_list):
    for update_cell, i in cell_list:
        cells_around = [cell for cell in cell_list if cell_near(cell, update_cell)]

        if len(cells_around) < 3:
            cell_list.pop(i)
