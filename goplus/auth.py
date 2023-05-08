import hashlib
import time

from swagger_client.api.token_controller_api import TokenControllerApi


class Auth(object):

    def __init__(self, key, secret):
        self.__check(key, secret)
        self.key = key
        self.secret = secret

    @staticmethod
    def __check(key, secret):
        if not (key and secret):
            raise ValueError('invalid key')

    @staticmethod
    def __sign(key, secret, t):
        s = key + str(t) + secret
        sha1 = hashlib.sha1()
        sha1.update(s.encode('utf-8'))
        return sha1.hexdigest()

    def get_access_token(self, **kwargs):
        t = int(time.time())
        return TokenControllerApi().get_access_token_using_post(self.key, self.__sign(self.key, self.secret, t),
                                                                t, **kwargs)
