

class Base:
    def __init__(self, access_token=None):
        self.access_token = access_token
        if access_token is not None:
            self.authorization = {'authorization': access_token}
        else:
            self.authorization = {}
