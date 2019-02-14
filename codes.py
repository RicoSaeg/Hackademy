import os

a_list = []

def my_sum(a_list):
    total = 0
    for n in a_list:
        total = total + n
    return total


def my_prod(a_list):
    total = 1
    for n in a_list:
        total = total * n
    return total


def my_count(a_list):
    count = 0
    for n in a_list:
        count = count + 1
    return count


def my_count_less_5(a_list):
    count = 0
    for n in a_list:
        if n < 5:
            count = count + 1
    return count


def my_count_1(a_list):
    count = 0
    for n in a_list:
        if n == 1:
            count = count + 1
    return count

def my_count_max(a_list):
    count = 0
    for n in a_list:
        if n > count:
            count = n
    return count

def get_filename(a_dirname):
    list_of_files = os.listdir(a_dirname)
    print("list of the file name: ")
    print(list_of_files)
    all_files = []
    for n in list_of_files:
        full_path = os.path.join(a_dirname,n)
        all_files.append(full_path)
    return all_files

def flatten(a_list_with_lists):
    new_list = []
    for n in a_list_with_lists:
        if isinstance(n, list):
            for i in n:
                new_list.append(i)
        else:
            new_list.append(n)
    return new_list


list_in_list = [12,[3,4],36]
#12
#3 4
#36


def print_right(a_list_with_lists):
    for n in a_list_with_lists:
        if isinstance(n, list ):
            for i in n:
                print(i, end=" ")
            print(" ")
        else:
            print(n)
        

    

def single_row_star(number):
    for n in range(number):
        if n % 2 == 0:
            print("*" , end=" ")
        else:
            print("/", end=" ")



a = int(input("numb"))
b = input("hello")
def single_row_of(number, string):
   for n in range (number):
       print(string, end=" ")


# list_by_two = []
def square_of_stars(num):
    for i in range(num):
        for n in range(num):
            print("*", end ="")
        print(" ")

l = [2,3,4]

def list_by_two(list):
    new_list = []
    for n in list:
        new_list.append()
    return new_list

def list_opposite(a_list):
    new_list = []
    for i in a_list:
        new_list.insert(0, i)
    return new_list

