from datetime import datetime
from random import randint


def send_sms(connect, sim_port: int, phone_number: str, message: str):
    connect.send_command(f'Action: smscommand\r\ncommand: gsm send sms '
                         f'{sim_port + 1} '
                         f'{phone_number} '
                         f'{message} '
                         f'{generate_id}\r\n\r\n'.encode(), timeout=5)


def generate_id():
    now = datetime.now()
    dt_string = now.strftime('%Y%m%d%H%M%S')
    return (dt_string + randint(1, 10000).__str__()).__str__()


def sim_port_spans(connect):
    connect.send_command(f'Action: smscommand\r\ncommand: gsm show spans\r\n\r\n'.encode(), timeout=5)
