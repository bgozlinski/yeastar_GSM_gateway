from decouple import config
from yeastar._Connection import Yeastar
from yeastar._Messages import send_sms, sim_port_spans

SMS = False
SPAN = True

if __name__ == "__main__":
    c = Yeastar('192.168.221.161', 5038, config('APIUSERNAME'), config('SECRET'))
    c.connect_to_yeastar()
    if SMS:
        send_sms(
            connect=c,
            sim_port=1,
            phone_number='+48572720038',
            message='pozdrowienia z Yeastar'
        )

    if SPAN:
        sim_port_spans(
            connect=c
        )
