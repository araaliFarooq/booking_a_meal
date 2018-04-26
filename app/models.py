class Admin(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return(self.username)