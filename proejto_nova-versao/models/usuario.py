class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate(self, username, password):
        return self.username == username and self.password == password

