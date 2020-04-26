def read_names(file_path: str) -> list:
    names_file = open(file_path, 'r')
    names_list = names_file.readlines()
    names_list = [name[:-1] for name in names_list]
    return names_list


master_list = read_names('master_list')

attendance_list = read_names('sessions/save-users-list-1587463546037.txt')
print(attendance_list)
