import time
import random

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    a_list.sort()

def generate_random_list(size):
    return [random.randint(0, 1000) for i in range(size)]

def main():
    for size in [500, 1000, 10000]:
        total_insertion_time = 0
        total_shell_time = 0
        total_python_time = 0

        for i in range(100):
            a_list = generate_random_list(size)

            start = time.time()
            insertion_sort(a_list)
            end = time.time()
            total_insertion_time += (end - start)

            a_list = generate_random_list(size)

            start = time.time()
            shell_sort(a_list)
            end = time.time()
            total_shell_time += (end - start)

            a_list = generate_random_list(size)

            start = time.time()
            python_sort(a_list)
            end = time.time()
            total_python_time += (end - start)

        average_insertion_time = total_insertion_time / 100
        average_shell_time = total_shell_time / 100
        average_python_time = total_python_time / 100

        print(f"The Insertion Sort takes around {average_insertion_time:.10f} seconds to run")
        print(f"The Shell Sort takes around {average_shell_time:.10f} seconds to run.")
        print(f"The Python Sort takes around {average_python_time:.10f} seconds to run.")
        print("\n")

if __name__ == "__main__":
    main()
