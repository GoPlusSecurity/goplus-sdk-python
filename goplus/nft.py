from swagger_client.api.nft_controller_api import NftControllerApi

from goplus.base import Base


class Nft(Base):

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)

    def nft_security(self, chain_id: str, address: str, **kwargs):
        return NftControllerApi().get_nft_info_using_get1(chain_id=chain_id, contract_addresses=address,
                                                          **self.authorization, **kwargs)
