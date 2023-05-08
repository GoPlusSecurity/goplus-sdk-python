from swagger_client.api.approve_controller_v_1_api import ApproveControllerV1Api
from goplus.base import Base


class Address(Base):

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = ApproveControllerV1Api()

    def address_security(self, address: str, chain_id=None, **kwargs):

        if chain_id is not None:
            kwargs["chain_id"] = chain_id

        return self.api.address_contract_using_get1(address=address, **self.authorization, **kwargs)
