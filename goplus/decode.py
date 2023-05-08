from swagger_client.api.contract_abi_controller_api import ContractAbiControllerApi

from goplus.base import Base


class Decode(Base):

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = ContractAbiControllerApi()

    def signature_data_decode(self, chain_id: str, data: str, address=None, signer=None, **kwargs):

        body = {
            "chain_id": chain_id,
            "data": data
        }

        if address is not None:
            body["contract_address"] = address

        if signer is not None:
            body["signer"] = signer

        return self.api.get_abi_data_info_using_post(body=body, **self.authorization, **kwargs)
