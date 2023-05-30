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

from goplus.base import Base
from swagger_client.api.approve_controller_v_1_api import ApproveControllerV1Api
from swagger_client.api.approve_controller_v_2_api import ApproveControllerV2Api


class Approve(Base):
    """
    Approve Security
    """

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = ApproveControllerV1Api()
        self.api_v2 = ApproveControllerV2Api()

    def approve_security_v1(self, chain_id: str, address: str, **kwargs):
        """
        Approve Security V1
        """
        return self.api.approval_contract_using_get(
            chain_id=chain_id,
            contract_addresses=address,
            **self.authorization,
            **kwargs
        )

    def token_approve_security(self, chain_id: str, address: str, **kwargs):
        """
        Token Approve Security
        """

        return self.api_v2.address_token_approve_list_using_get1(
            chain_id=chain_id, addresses=address, **self.authorization, **kwargs
        )

    def erc721_approve_security(self, chain_id: str, address: str, **kwargs):
        """
        ERC721 Approve Security
        """

        return self.api_v2.address_nft721_approve_list_using_get1(
            chain_id=chain_id, addresses=address, **self.authorization, **kwargs
        )

    def erc1155_approve_security(self, chain_id: str, address: str, **kwargs):
        """
        ERC1155 Approve Security
        """

        return self.api_v2.address_nft1155_approve_list_using_get1(
            chain_id=chain_id, addresses=address, **self.authorization, **kwargs
        )
