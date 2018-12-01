def save_file(str_file_name, bytes_array):
    open(str_file_name, 'wb').write(bytes_array)


def save_mas_file(str_prefix_name, file_type, list_bytes_array):
    for i in range(0, len(list_bytes_array)):
        str_file_name = '{}_{}.{}'.format(str_prefix_name, i, file_type)
        save_file(str_file_name, list_bytes_array[i])
