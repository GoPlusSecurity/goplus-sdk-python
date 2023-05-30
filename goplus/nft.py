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
