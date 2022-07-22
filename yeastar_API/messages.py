import datetime
from random import randint


def send_sms(connection, sim_port: int, phone_number: str, message: str):
    return connection.send(f'Action: smscommand\r\ncommand: gsm send sms {sim_port+1} {phone_number} "{message}"'
                           f' {generate_id()}\r\n\r\n'.encode(), 6)


def generate_id():
    now = datetime.datetime.now()
    dt_string = now.strftime('%Y%m%d%H%M%S')
    return (dt_string + randint(1, 10000).__str__()).__str__()


def sim_port_status(connection, sim_port: int):
    return connection.send(f'Action: smscommand\r\ncommand: gsm show span {sim_port+1}\r\n\r\n'.encode(), 6)



