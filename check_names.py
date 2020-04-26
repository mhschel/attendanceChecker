master_list_file = open('master_list', 'r')
master_list = master_list_file.readlines()

master_list = [name[:-2] for name in master_list]
print(master_list)
