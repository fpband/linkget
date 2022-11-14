import os

class Config:
    API_ID = int( os.getenv("api_id","3335796") )
    API_HASH = os.getenv("api_hash","138b992a0e672e8346d8439c3f42ea78")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001645543494") )
    CHANNEL_USERNAME = os.getenv("channel_username","dlchin")
    TOKEN = 1996499923:AAGVCjT4msY1AOHb-qtalwMsrwu0dD65k7g
    DOMAIN  = os.getenv("domain","https://newfastlink70.osc-fr1.scalingo.io/")
