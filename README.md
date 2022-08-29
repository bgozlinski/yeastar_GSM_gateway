# Python script to interact with Yeastar SMS Gateway:

* connecting,
* authenticating with,
* sending SMS messages via any of the 8 connected SIM cards 

Tested on Yeastar TG800 VoIP
https://www.yeastar.com/voip-gsm-gateway/#specifications-acr


## Getting Started
In order to use API on Yeastar you need to define the IP address or IP section which is allowed to use API in SMS -> API Settings

You need to create .env file locally that contains decouple Encodings:

```
APIUSERNAME=apiusername
SECRET=apipassword
```

TODO:
-[x] Usage of SIM ports
-[ ] Receive incoming SMS
