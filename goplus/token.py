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
from swagger_client.api.token_controller_v_1_api import TokenControllerV1Api
from swagger_client.api.token_security_api_for_solana__beta_api import (
    TokenSecurityAPIForSolanaBetaApi,
)
from swagger_client.api.token_security_api_for_sui_api import TokenSecurityAPIForSuiApi


class Token(Base):
    """
    Token Security
    """

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = TokenControllerV1Api()
        self.solana_api = TokenSecurityAPIForSolanaBetaApi()
        self.sui_api = TokenSecurityAPIForSuiApi()

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

    def solana_token_security(self, addresses: list, **kwargs):

        self.__check(addresses)

        return self.solana_api.solana_token_security_using_get(
            contract_addresses=",".join(addresses), **self.authorization, **kwargs
        )

    def sui_token_security(self, addresses: list, **kwargs):

        self.__check(addresses)

        return self.sui_api.sui_token_security_using_get(
            contract_addresses=",".join(addresses), **self.authorization, **kwargs
        )
