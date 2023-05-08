from swagger_client.api.dapp_controller_api import DappControllerApi

from goplus.base import Base


class Dapp(Base):

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)

    def dapp_security(self, url: str, **kwargs):
        return DappControllerApi().get_dapp_info_using_get(url=url, **self.authorization, **kwargs)
