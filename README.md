example:
```python
if __name__ == "__main__":
    c = Yeastar('192.168.221.161', 5038, 'apiuser', 'apipassword')
    c.connect_to_yeastar()
    c.send_sms(
        sim_port=1,
        phone_number='+48572720038',
        message='pozdrowienia z Yeastar'
    )
    
