# Copyright 2023 The GoPlus. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import time

from swagger_client.api.token_controller_api import TokenControllerApi


class Auth(object):
    def __init__(self, key, secret):
        self.__check(key, secret)
        self.key = key
        self.secret = secret
        self.api = TokenControllerApi()

    @staticmethod
    def __check(key, secret):
        if not (key and secret):
            raise ValueError("invalid key")

    @staticmethod
    def __sign(key, secret, t):
        s = key + str(t) + secret
        sha1 = hashlib.sha1()
        sha1.update(s.encode("utf-8"))
        return sha1.hexdigest()

    def get_access_token(self, **kwargs):
        t = int(time.time())
        body = {
            "app_key": self.key,
            "sign": self.__sign(self.key, self.secret, t),
            "time": t,
        }
        return self.api.get_access_token_using_post(**{"body": body}, **kwargs)
