import random

def setup_game(size, max_alive):
    empty_grid = get_empty_grid(size)
    fill_grid_random(empty_grid,max_alive)

def create_grid(size):
    new_list = []
    for i in range(size):
        list_in_list = []
        for n in range(size):
            list_in_list.append("-")
        new_list.append(list_in_list)
    return new_list


def rand_alive():
    number = random.randint(1,2)
    if number == 1:
        return True
    else:
        return False 


def fill_grid_random(a_grid, max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        for c_i in range(size):
            if rand_alive() == True and remaining != 0:
                a_grid[r_i][c_i] = "x"
                remaining = remaining - 1
            else:
                a_grid[r_i][c_i] = "-"


def print_grid(a_grid):
    size = len(grid)
    for r_i in range(size):
        for c_i in range(size):
            print(a_grid[r_i][c_i], end="")
        print(" ")

a_grid = get_empty_grid(a_grid)
fill_grid_random(a_grid, 10)
print(a_grid)

list_a = [3,2,5,2,5,2]
list_b = [2,3,5,7,8,4]

def is_duplicate_there(list_a,list_b):
    count = 0
    for i in list_a:
        for n in list_b:
            if i == n:
                count = count + 1
    if count != 0:
        return True
#fastest way!
def is_duplicate_there(list_a,list_b):
    return (set(list_a).intersection(list_b) == 0):
is_duplicate_there(list_a,list_b)

def is_different(list_a, list_b):
    difference_list = []
    for i in list_a:
        for n in list_b:
            if i == n:
                difference_list.append(i)
            else:
                pass
    list_a += list_b
    final_list = list_a - difference_list
    return final_list

is_different(list_a,list_b)