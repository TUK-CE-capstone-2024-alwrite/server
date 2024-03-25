import pyrebase
import json

class Database:
    def __init__(self):
        with open('secret_info/authentication/firebase_auth.json') as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()