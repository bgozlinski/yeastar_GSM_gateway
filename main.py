from yeastar_API.connect import Connection
from yeastar_API.messages import send_sms, sim_port_status


if __name__ == "__main__":
    connection = Connection('192.168.221.161', 5038, 'isander', '075TovoneL')
    # send_sms(connection, 1, '+48572720038', 'pozdrowienia z Yeastar')
    sim_port_status(connection, 1)
