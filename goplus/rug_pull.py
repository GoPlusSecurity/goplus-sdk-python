from goplus.base import Base
from swagger_client.api.defi_controller_api import DefiControllerApi


class RugPull(Base):
    """
    Rug-pull detection
    """

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = DefiControllerApi()

    def rug_pull_security(self, chain_id: str, address: str, **kwargs):
        return self.api.get_defi_info_using_get(
            contract_addresses=address,
            chain_id=chain_id,
            **self.authorization,
            **kwargs
        )
