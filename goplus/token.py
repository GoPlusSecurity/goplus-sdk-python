from goplus.base import Base
from swagger_client.api.token_controller_v_1_api import TokenControllerV1Api


class Token(Base):
    """
    Token Security
    """

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = TokenControllerV1Api()

    @staticmethod
    def __check(addresses):

        if not isinstance(addresses, list):
            raise TypeError("contract_addresses must be of list type!")

        if len(addresses) == 0:
            raise ValueError("invalid contract_addresses")

    def token_security(self, chain_id: str, addresses: list, **kwargs):

        self.__check(addresses)

        return self.api.token_security_using_get1(
            chain_id=chain_id,
            contract_addresses=",".join(addresses),
            **self.authorization,
            **kwargs
        )
