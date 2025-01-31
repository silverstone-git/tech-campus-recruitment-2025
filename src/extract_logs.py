# ASSUMING SORTED LOGS
from sys import argv
import subprocess
from datetime import datetime

def get_line(line_number, file):
    original_position = file.tell()
    try:
        if line_number < 0:
            file.seek(0)
            line = file.readline()
            return line.strip() if line else None
        
        file.seek(0)  # Start from beginning for line iteration
        last_line = None
        for current_line_number, line in enumerate(file):
            last_line = line
            if current_line_number == line_number:
                return line.strip()
        
        # Return last line if line_number exceeds total lines
        return last_line.strip() if last_line else None
    finally:
        file.seek(original_position)  # Restore original file position


def get_logs_by_date(target_date, file_path):
    # return logs by daate

    found_index, total_lines= find_log_index(target_date, file_path)

    # appends while running backwards and then, backwards

    res = []
    with open(file_path, 'r') as file:

        for i in range(found_index - 1, -1, -1):
            cur_line = get_line(i, file)
            # print(i)
            # print(cur_line)
            if cur_line.split()[0] == target_date:
                res.append(cur_line)
            else:
                break

        # print("forwards:")

        for i in range(found_index, total_lines):
            cur_line = get_line(i, file)
            # print(i)
            # print(cur_line)
            if cur_line.split()[0] == target_date:
                res.append(cur_line)
            else:
                break

    # print()
    return res


def find_log_index(target_date, file_path):
    left = 0
    # right = system('wc -l ' + file_path)
    cmd_out = subprocess.check_output(['wc', '-l', file_path])

    right = int(cmd_out.decode().split()[0])
    total_lines = right
    # print("right : ", right, type(right))

    with open(file_path, 'r') as file:
        while left <= right:
            mid = (left + right) // 2
            # print("mid is: ", mid)
            
            # Seek to the middle position and read the date
            line = get_line(mid, file)
            # print("line at mid, ", mid, " is ", line)
            line_date = line.split()[0].strip()
            # print("line date at mid, ", mid, " is ", line_date)
            
            if line_date == target_date:
                return mid, total_lines
            elif datetime.strptime(line_date, "%Y-%m-%d") < datetime.strptime(line_date, "%Y-%m-%d"):
                left = mid + 1
            else:
                right = mid - 1

    return left, total_lines


if __name__ == "__main__":

    # Starts with binary search, resorts to linear to append lines when date found
    print(get_logs_by_date(argv[1], './logs.log'))

