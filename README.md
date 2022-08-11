example:
```python
if __name__ == "__main__":
    connection = Connection('192.168.221.161', 5038, 'apiuser', 'apipassword')
    send_sms(connection, 1, '+48123456789', 'pozdrowienia z Yeastar')
