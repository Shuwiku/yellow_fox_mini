import requests
import scripts


def response(res_url):  # Запрос на Сервер
    res = requests.get(res_url)
    return res


def response_url(server, res_data):  # Генерация ссылки для Запроса
    res_url = f'{server}/data/?'
    for key, val in list(res_data.items()):
        value = '-'.join(val.split())
        res_url += f'{key}={value}&'
    return res_url


def response_handler(action, server, app, ip, data, data_type):  # Обработчик
    res_data = {
        'action': action,
        'app': app,
        'ip': ip,
        'data': data,
        'type': data_type
    }

    if (action == 'create'):
        res_data = {
            **res_data,
            **scripts.user_pc()
        }

    res_url = response_url(server, res_data)
    res = response(res_url)
    return res
