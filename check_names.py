import sys
import getopt
import re


def read_names(file_path: str) -> list:
    names_file = open(file_path, 'r')
    names_list = names_file.readlines()
    names_list = [name[:-1] for name in names_list]
    return names_list


def get_last_name_from_attendance(attendance_list):
    regx = re.compile('(\w+\s)')
    return [regx.search(name).group(0)[:-1] for name in attendance_list]


def get_last_name_from_master(master_list):
    regx = re.compile('(^[^,]*)')
    return [regx.search(name).group(0) for name in master_list]


def check_attendance(master_list, attendance_list):
    return [name for name in master_list if not name in attendance_list]


if __name__ == "__main__":
    master_list = read_names('master_list')
    master_names = get_last_name_from_master(master_list)

    attendance_list = read_names(sys.argv[1])
    attendance_names = get_last_name_from_attendance(attendance_list)

    missing_names = check_attendance(master_names, attendance_names)

    for name in missing_names:
        print("Not marked present: {}".format(name))
