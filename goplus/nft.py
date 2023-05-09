from goplus.base import Base
from swagger_client.api.nft_controller_api import NftControllerApi


class Nft(Base):
    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = NftControllerApi()

    def nft_security(self, chain_id: str, address: str, **kwargs):
        return self.api.get_nft_info_using_get1(
            chain_id=chain_id,
            contract_addresses=address,
            **self.authorization,
            **kwargs
        )
