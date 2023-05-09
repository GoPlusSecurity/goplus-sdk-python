from goplus.base import Base
from swagger_client.api.dapp_controller_api import DappControllerApi


class Dapp(Base):
    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = DappControllerApi()

    def dapp_security(self, url: str, **kwargs):
        return self.api.get_dapp_info_using_get(url=url, **self.authorization, **kwargs)
